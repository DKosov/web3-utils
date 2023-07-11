from dataclasses import dataclass
from typing import Any, Callable, Union
from eth_typing import ChecksumAddress, Decodable, HexStr
from eth_abi.codec import ABICodec


@dataclass
class Call:
    address: ChecksumAddress
    data: Union[bytes, HexStr]
    decode_handler: Callable[[ABICodec, Decodable], Any]
