"""
simple example of the backend of a blockchain
    The project is mounted in flask, 
    and it only consists of endpoints, 
    that is, the backend part, it is free 
    to add the person you want to the front
"""

from flask import Flask, jsonify
from blockchainClass import Blockchain

app= Flask(__name__) 
blockchain = Blockchain()


# first route: Mining a new block
@app.route('/mine_block', methods = ['GET']) 
def mine_block(): 
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof'] 
    proof = blockchain.proof_of_work(previous_proof) 
    previous_hash = blockchain.hash(previous_block) 
    block = blockchain.create_block(proof, previous_hash) 
    response = {'message': 'Congratulations, you just mined a block!', 
                'index': block['index'], 
                'timestamp': block['timestamp'], 
                'proof': block['proof'], 
                'previous_hash': block['previous_hash']} 
    return jsonify(response), 200


# second route: Getting the full Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        "chain": blockchain.chain,
        "length":len(blockchain.chain)
    }
    return jsonify(response),200

# third route: Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET']) 
def is_valid(): 
    is_valid = blockchain.is_chain_valid(blockchain.chain) 
    if is_valid: 
        response = {'message': 'All good. The Blockchain is valid.'} 
    else: 
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'} 
    return jsonify(response), 200


# Fourth route: hack the blockchain
@app.route('/break_chain', methods = ['GET']) 
def break_chain(): 
    blockchain.breake_chain(blockchain.chain) 
    response = {'message': 'hacker in action'} 
    return jsonify(response), 200



# inicializacion de el servidor
if __name__ == '__main__':
   app.debug = True
app.run('0.0.0.0', port = 5001)










