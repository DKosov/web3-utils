from eth_typing import ChecksumAddress
from web3 import Web3
from web3_utils.types import ChainId
from web3_utils.utils import encode_hex_fn_abi
from web3_utils.multicall.abi import tryAggregate_abi

tryAggregate_selector = encode_hex_fn_abi(tryAggregate_abi)
tryAggregate_output_types = ['(bool,bytes)[]']

MULTICALL_ADDRESSES: dict[ChainId, ChecksumAddress] = {
    ChainId.ETHEREUM: Web3.to_checksum_address("0x5ba1e12693dc8f9c48aad8770482f4739beed696"),
    ChainId.BSC: Web3.to_checksum_address("0x15dc8b5ed578AA7a019dd0139B330cfD625cA795"),
    ChainId.POLYGON: Web3.to_checksum_address("0x176730799C812d70C6608F51aEa6C7e5cdA7eA50"),
    ChainId.OPTIMISM: Web3.to_checksum_address("0xdf9Cd648823d2715E130705EDe230d2Fad47f2b9"),
    ChainId.XDAI: Web3.to_checksum_address("0x08612d3C4A5Dfe2FaaFaFe6a4ff712C2dC675bF7"),
    ChainId.FUSE: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.BOBA: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.ASTAR: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.HARMONY: Web3.to_checksum_address("0xdDCbf776dF3dE60163066A5ddDF2277cB445E0F3"),
    ChainId.AVAX: Web3.to_checksum_address("0xdDCbf776dF3dE60163066A5ddDF2277cB445E0F3"),
    ChainId.ARBITRUM: Web3.to_checksum_address("0x80C7DD17B01855a6D2347444a0FCC36136a314de"),
    ChainId.CELO: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.FANTOM: Web3.to_checksum_address("0x22D4cF72C45F8198CfbF4B568dBdB5A85e8DC0B5"),
    ChainId.CRONOS: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.KCC: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.MOONBEAM: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.MOONRIVER: Web3.to_checksum_address("0x270f2F35bED92B7A59eA5F08F6B3fd34c8D9D9b5"),
    ChainId.AURORA: Web3.to_checksum_address("0xe0e3887b158F7F9c80c835a61ED809389BC08d1b"),
    ChainId.CUBE: Web3.to_checksum_address("0x511b6bdf973bccda108059f082807bc5f2ef6b8b"),
    ChainId.BASE: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
    ChainId.UNICHAIN: Web3.to_checksum_address("0xcA11bde05977b3631167028862bE2a173976CA11"),
}
