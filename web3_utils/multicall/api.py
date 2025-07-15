from typing import Any, Iterable, Optional
from web3.types import TxParams
from eth_typing import ChecksumAddress
from eth_abi.codec import ABICodec
from eth_utils import to_hex
from hexbytes import HexBytes
from web3_utils.multicall import constants
from web3_utils.types import Chain
from web3_utils.multicall.types import Call


def build_multicall(
    codec: ABICodec,
    contract_address: ChecksumAddress,
    data: Iterable[Any],
) -> TxParams:
    tx_data = codec.encode(
        ['bool', '(address,bytes)[]'],
        [False, data],
    )
    return {"to": contract_address, "data": to_hex(HexBytes(constants.tryAggregate_selector) + tx_data)}


async def get(chain: Chain, calls: list[Call], tx: Optional[TxParams] = None) -> list[Any]:
    if tx is None:
        tx = build_multicall(
            codec=chain.web3.codec,
            contract_address=constants.MULTICALL_ADDRESSES[chain.chain_id],
            data=[(i.address, i.data) for i in calls]
        )
    tx_raw_data = await chain.web3.eth.call(tx) # type: ignore
    output_data_multi: Iterable[tuple[bool, bytes]] = chain.web3.codec.decode(constants.tryAggregate_output_types, tx_raw_data)[0]  # 0.0005030632019042969
    res = [
        call.decode_handler(chain.web3.codec, output_data[1])
        if output_data[0]
        else None
        for call, output_data in zip(calls, output_data_multi)
    ]
    return res
