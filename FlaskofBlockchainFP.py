from flask import Flask, request, jsonify, render_template
from web3 import Web3

app = Flask(__name__, template_folder='~/Implications/templates')

# Initialize Web3 with the local Ganache node URL
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:5000'))

# Example contract ABI (replace with your actual ABI)
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

# Example contract address (replace with your actual contract address)
contract_address = '0xBc4E27023fD699Fe4CD1247676220EB206C1a7CC'

# Connect to the contract using its ABI and address
contract = web3.eth.contract(address=web3.to_checksum_address(contract_address), abi=contract_abi)
#@app.route('/')
#def index():
    #return render_template('FPAppInterface.html')

# Endpoint for creating digital identity
@app.route('/create_identity', methods=['POST'])
def create_identity():
    # Get data from request body
    data = request.json
    name = data.get('name')

    # Perform necessary actions to create identity
    # Example: Insert data into the database
    # Example: Call Ethereum smart contract to register identity

    return jsonify({'message': 'Identity created successfully'}), 200


@app.route('/')
def index():
    return render_template('FPAppInterface.html')

# Endpoint for verifying digital identity
@app.route('/verify_identity', methods=['POST'])
def verify_identity():
    # Get data from request body
    data = request.json
    address = data.get('address')

    # Check if address is provided
    if not address:
        return jsonify({'error': 'Address is required'}), 400

    # Check if provided address matches the target address
    if address == contract_address:
        return jsonify({'message': 'Identity verified successfully'}), 200
    else:
        return jsonify({'error': 'Invalid address'}), 400

    # Perform necessary actions to verify identity
    # Example: Query database to check if identity exists
    # Example: Call Ethereum smart contract to verify identity

    return jsonify({'message': 'Identity verified successfully'}), 200

if __name__ == '__main__':
    # Run Flask application on localhost (127.0.0.1) and port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)
