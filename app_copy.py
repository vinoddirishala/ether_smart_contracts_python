from eth_account import Account
from eth_typing import abi
from web3 import Web3
import secrets
import os
import json
from dotenv import load_dotenv

load_dotenv()

priv = secrets.token_hex(32)
private_key = "0x"+priv
#print("PrivateKey of your wallet:::"+private_key)
acc = Account.from_key(private_key)
#print("Your Public Wallet Address of Etherium:::"+acc.address)


abi = {}


web3 = Web3(Web3.HTTPProvider(os.environ['RPC_URL']))

if web3.isConnected():

    account1 = "0x2bB82C830Efe707C864b5bfEad7e5610459AB240"
    account2 = "0xd8bFc5271635C6EbBaAEab564A734F478dB52850"
    privateKey = "b7d578d85714801883979093479417801a9c15a682c8eb5cf7e556a9cbb54ed8"

    nonce = web3.eth.getTransactionCount(account1)


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


    web3.eth.contract(address=account1,abi=abi)




else:
    print("Connect to wallet to continue")




