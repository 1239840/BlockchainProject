from flask import Flask, render_template
from web3 import Web3
import blockchain

app = Flask(__name__)

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1'))  # Update with your Ganache URL
contract_address = "0db518832a6153e1c109c7dbe35cf6d7"  # Update with your generate contract address
contract_abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "name",
                "type": "string"
            }
        ],
        "name": "IdentityCreated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "IdentityVerified",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "contractOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_name",
                "type": "string"
            }
        ],
        "name": "createIdentity",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getContractOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "getIdentity",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "identities",
        "outputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "verified",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "verifyIdentity",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Example: Create a new identity
tx_hash = contract.functions.createIdentity("Alice").transact({'from': web3.eth.accounts[0]})
web3.eth.waitForTransactionReceipt(tx_hash)

# Example: Verify an identity
tx_hash = contract.functions.verifyIdentity(web3.eth.accounts[0]).transact({'from': web3.eth.accounts[0]})
web3.eth.waitForTransactionReceipt(tx_hash)

# Get identity details
identity_details = contract.functions.getIdentity(web3.eth.accounts[0]).call()
print("Identity Details:", identity_details)


@app.route('/')
def index():
    return render_template('FPAppInterface.html')

@app.route('/create_identity', methods=['POST'])
def create_identity():
    name = request.form['name']
    # Call the createIdentity function in your blockchain backend
    blockchain.createIdentity(name)
    return redirect('/')

@app.route('/verify_identity', methods=['POST'])
def verify_identity():
    address = request.form['address']
    # Call the verifyIdentity function in your blockchain backend
    blockchain.verifyIdentity(address)
    return redirect('/')

@app.route('/check_identity', methods=['POST'])
def check_identity():
    check_address = request.form['check_address']
    # Call the getIdentity function in your blockchain backend
    identity = blockchain.getIdentity(check_address)
    return render_template('check_identity.html', identity=identity)

if __name__ == '__main__':
    app.run(debug=True)
