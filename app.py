from eth_account import Account
from eth_account.signers.local import LocalAccount
from eth_typing import abi
from web3 import Web3
import secrets
import os
import json
from dotenv import load_dotenv
import string



load_dotenv()

#generate private key and wallet address
privateKeyWithOutPrefix = secrets.token_hex(32)
privateKey = "0x"+privateKeyWithOutPrefix
walletAddress = Account.from_key(privateKey)


#fromPrivateKey = "b7d578d85714801883979093479417801a9c15a682c8eb5cf7e556a9cbb54ed8"
#fromWalletAddress = "0x2bB82C830Efe707C864b5bfEad7e5610459AB240"

privateKey = "5f8970adc9d9fe3d8a8981a848ee7c4bff9fd085d6977f4b4ea7b5cd27da7584"
walletAddress = "0x4E140256a24E42396dF7953Ce76067F97d906788"

#load data from env file
rpcURL = os.environ['RPC_URL']
abiJson = json.loads(os.environ['CONTRACT_ABI'])
byteCode = os.environ['CONTRACT_BYTE_CDOE']

web3 = Web3(Web3.HTTPProvider(rpcURL))



if web3.isConnected():

    #This code is useful to transfer funds from one wallet to other wallet address
    #transactionBody = {
    #    'nonce':web3.eth.getTransactionCount(fromWalletAddress),
    #    'to':walletAddress.address,
    #    'value':web3.toWei(20,'ether'),
    #    'gas':2000000,
    #    'gasPrice':web3.toWei('50','gwei')
    #}

    #signTransaction = web3.eth.account.sign_transaction(transactionBody,fromPrivateKey) 
    #txnHash = web3.eth.sendRawTransaction(signTransaction.rawTransaction)
    #print(web3.toHex(txnHash))


    guess_number = web3.eth.contract(abi=abiJson,bytecode=byteCode)
    print(web3.eth.getTransactionCount(walletAddress))
    transactionBody = {
       # 'nonce':web3.eth.getTransactionCount(walletAddress.address),
        'nonce':web3.eth.getTransactionCount(walletAddress),
        'value':web3.toWei(0.00001,'ether'),
        'gas':2000000,
        'gasPrice':web3.toWei('0.00005','gwei')
    }
    signTransaction = web3.eth.account.sign_transaction(transactionBody,privateKey) 
    txnHash = web3.eth.sendRawTransaction(signTransaction.rawTransaction)
    print(web3.toHex(txnHash))
    


    
else:
    print("Connect to wallet to continue")




