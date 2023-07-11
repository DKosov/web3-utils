from web3.types import ABIFunction


tryAggregate_abi: ABIFunction = {
    "inputs": [
        {"name": "requireSuccess", "type": "bool"},
        {
            "components": [
                {"name": "target", "type": "address"},
                {"name": "callData", "type": "bytes"},
            ],
            "name": "calls",
            "type": "tuple[]",
        },
    ],
    "name": "tryAggregate",
    "outputs": [
        {
            "components": [
                {"name": "success", "type": "bool"},
                {"name": "returnData", "type": "bytes"},
            ],
            "name": "returnData",
            "type": "tuple[]",
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function",
}
