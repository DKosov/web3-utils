from typing import Optional, TypeVar, cast
from enum import Enum
from typing_extensions import ParamSpec
from eth_typing import ChecksumAddress
from pydantic import BaseModel, ConstrainedStr
from web3.middleware import async_geth_poa_middleware
from web3 import AsyncHTTPProvider, AsyncWeb3, Web3
from web3.eth import AsyncEth


class ChainId(int, Enum):
    LOCAL = 0
    ETHEREUM = 1
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    OPTIMISM = 10
    CRONOS = 25
    KOVAN = 42
    BSC = 56
    OPTIMISM_KOVAN = 69
    SOKOL = 77
    XDAI = 100
    FUSE = 122
    POLYGON = 137
    FANTOM = 250
    BOBA = 288
    KCC = 321
    ASTAR = 592
    CUBE = 1818
    MOONBEAM = 1284
    MOONRIVER = 1285
    ARBITRUM = 42161
    AVAX = 43114
    CELO = 42220
    MUMBAI = 80001
    ARBITRUM_TESTNET = 421611
    AURORA = 1313161554
    HARMONY = 1666600000

    SOLANA = -1
    NEAR = -2

    COSMOS = -100
    OSMOSIS = -101
    SIF = -102

    BTC = -200
    LTC = -201
    BCH = -202


class LowerStr(ConstrainedStr):
    to_lower = True


class Token(BaseModel):
    chain_id: ChainId
    address: LowerStr
    symbol: str
    decimals: int


P = ParamSpec("P")
T = TypeVar("T")


CHAIN_NAMES = {
    ChainId.ARBITRUM: 'arbitrum',
    # ChainId.ASTAR: 'astar',
    # ChainId.AURORA: 'aurora',
    ChainId.AVAX: 'avalanche',
    # ChainId.BOBA: 'boba',
    ChainId.BSC: 'bsc',
    ChainId.CELO: 'celo',
    # ChainId.CRONOS: 'cronos',
    ChainId.ETHEREUM: 'ethereum',
    ChainId.FANTOM: 'fantom',
    # ChainId.FUSE: 'fuse',
    # ChainId.XDAI: 'gnosischain',
    ChainId.HARMONY: 'harmony',
    # ChainId.HECO: 'heco',
    # ChainId.KAVA: 'kava',
    # 'kcc',
    # 'milkomedacardano',
    ChainId.MOONBEAM: 'moonbeam',
    ChainId.MOONRIVER: 'moonriver',
    # ChainId.OKC: 'okc',
    ChainId.OPTIMISM: 'optimism',
    ChainId.POLYGON: 'polygon',
    # 'pulsechain',
    # 'solana',
    # 'stepnetwork',
    # 'syscoin',
    # 'telos'
}


NATIVE_ADDRESS = "0x0000000000000000000000000000000000000000"


class Chain:
    chain_id: ChainId
    web3: AsyncWeb3
    default_weth_address: ChecksumAddress
    # leverager_address: Optional[ChecksumAddress] = None
    gas_price: Optional[int] = None
    seconds_between_updates: float
    _delays: list[float]

    def __init__(
        self, chain_id: ChainId, rpc_url: str, default_weth_address: str,seconds_between_updates: float = .33
    ):
        self.chain_id = chain_id
        self.seconds_between_updates = seconds_between_updates
        self.web3 = AsyncWeb3(Web3.AsyncHTTPProvider(rpc_url, request_kwargs={'timeout': 60}), modules={"eth": (AsyncEth,)}, middlewares=[])
        self.default_weth_address = Web3.to_checksum_address(default_weth_address)
        self.web3.middleware_onion.inject(async_geth_poa_middleware, layer=0)
        self._delays = []

    def set_timeout(self, timeout: float) -> None:
        kwargs = cast(AsyncHTTPProvider, self.web3.provider)._request_kwargs or {}
        kwargs["timeout"] = timeout
        cast(AsyncHTTPProvider, self.web3.provider)._request_kwargs = kwargs
        return None
