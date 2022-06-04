import json
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = json.loads('[{"inputs": [],"name": "Greeter","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "getGreeting","outputs": [{"internalType": "string","name": "","type":"string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "string","name": "message","type": "string"}],"name": "setGreeting","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
address = web3.toChecksumAddress("0xd1BF368125f51A3A80A702d57c2FFC969c80604a")

contract = web3.eth.contract(address=address,abi=abi)
print(contract.functions.getGreeting().call())

tx_hash = contract.functions.setGreeting("New greeting").transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated greeting: {}'.format(
    contract.functions.getGreeting().call()
))
