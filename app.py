from eth_account import Account
from web3 import Web3
import secrets

priv = secrets.token_hex(32)
private_key = "0x"+priv
#print("PrivateKey of your wallet:::"+private_key)
acc = Account.from_key(private_key)
#print("Your Public Wallet Address of Etherium:::"+acc.address)

rpcURL = "HTTP://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(rpcURL))

if web3.isConnected():

    account1 = "0x2bB82C830Efe707C864b5bfEad7e5610459AB240"
    account2 = "0xd8bFc5271635C6EbBaAEab564A734F478dB52850"
    privateKey = "b7d578d85714801883979093479417801a9c15a682c8eb5cf7e556a9cbb54ed8"

    nonce = web3.eth.getTransactionCount(account1)
    print(web3.toInt(web3.eth.get_balance(account1)))


    tx = {
        'nonce':nonce,
        'to':account2,
        'value':web3.toWei(0.00001,'ether'),
        'gas':2000000,
        'gasPrice':web3.toWei('50','gwei')
    }

    signedTX = web3.eth.account.signTransaction(tx,privateKey)
    txHash = web3.eth.sendRawTransaction(signedTX.rawTransaction)
    print(web3.toHex(txHash))

    print(web3.toInt(web3.eth.get_balance(account1)))

else:
    print("Connect to wallet to continue")




