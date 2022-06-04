from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xEE378332872b61a590113314c3158152d0b40DE2"
account_2 = "0x51Ef9631e7102F551BA1521b0b96815301ee3763"

private_key = "da8bb0894e24dadc54c55032fe9af6f9980a073b62f0696f089fc55102168f36"


nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50','gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))