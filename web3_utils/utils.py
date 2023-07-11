from typing import Any, Callable, cast, Union
from eth_typing import HexStr
from eth_utils import encode_hex, function_abi_to_4byte_selector
from web3.types import ABIFunction


ABIFunctionOrDict = Union[dict[str, Any], ABIFunction]
encode_hex_fn_abi: Callable[[ABIFunctionOrDict], HexStr] = lambda fn_abi: encode_hex(
    function_abi_to_4byte_selector(cast(dict[str, Any], fn_abi))
)
