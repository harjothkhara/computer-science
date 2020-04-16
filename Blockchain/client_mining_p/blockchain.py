# Paste your version of blockchain.py from the basic_block_gp
# folder here

import random
import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        A block should have:
        * Index/height
        * Timestamp to say when this block was created
        * List of current transactions
        * The proof used to mine this block (the salt we're sprinkling on to check our hash)
        * The hash of the previous block which will make it unmodifiable.

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        # ---- not needed but used to add the current_hash to the block so we can see our leading 0's
        if len(self.chain) > 0:
            block_string = json.dumps(self.last_block, sort_keys=True)
            guess = f'{block_string}{proof}'.encode()
            current_hash = hashlib.sha256(guess).hexdigest()  # *
        else:
            current_hash = ""
        # -----
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            # for genesis block otherwise pass in hash of last block
            # hash of the last block which is validating that block
            'previous_hash': previous_hash or self.hash(self.last_block),
            'hash': current_hash  # * hash that our proof of work came up with
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the block to the chain
        self.chain.append(block)
        # Return the new block
        return block

    def hash(self, block):  # e.g s or salt
        """
        Creates a SHA-256 hash of a Block

        :param block": <dict> Block
        "return": <str>
        """
        # Use json.dumps to convert json into a string
        # Use hashlib.sha256 to create a hash
        # It requires a `bytes-like` object, which is what
        # .encode() does.
        # It converts the Python string into a byte string.
        # We must make sure that the Dictionary is Ordered, https://www.geeksforgeeks.org/ordereddict-in-python/
        # or we'll have inconsistent hashes

        # sort_keys = make sure our hash will show up in the same order
        # TODO: Create the block_string
        string_object = json.dumps(block, sort_keys=True)  # alphabetical order
        # turns to a byte string (sha256 requirement)
        block_string = string_object.encode()

        # TODO: Hash this string using sha256
        raw_hash = hashlib.sha256(block_string)

        # By itself, the sha256 function returns the hash in a raw string
        # that will likely include escaped characters.
        # This can be hard to read, but .hexdigest() converts the
        # hash to a string of hexadecimal characters, which is
        # easier to work with and understand
        hash_string = raw_hash.hexdigest()
        # TODO: Return the hashed block string in hexadecimal format
        return hash_string

    @property  # decorators that treats this function an object property. instead of calling last_block as a function we can call it as '@property'
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):  # takes in last block  e.g print(result)
        """
        Simple Proof of Work Algorithm
        Stringify the block and look for a proof.
        Loop through possibilities, checking each one against `valid_proof`
        in an effort to find a number that is a valid proof
        :return: A valid proof for the provided block
        """
        # TODO # sort_keys = make sure our hash will show up in the same order                  # self.last_block
        block_string = json.dumps(block, sort_keys=True)
        proof = 0  # pick a number, using integer proofs. guess
        while self.valid_proof(block_string, proof) is False:
            # don't have to do it this way, randomize it may be better because by incrementing from 0 you'll be slower at competing with others to forge new block with faster machines.
            proof += 1
        return proof

    @staticmethod  # 'e.g 0000'
    def valid_proof(block_string, proof):  # check to see if out pow is actually a valid hash
        """
        Validates the Proof:  Does hash(block_string, proof) contain 3
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        # TODO
        print(f"I will now check if {proof} is valid")
        guess = block_string + str(proof)  # salt it with our proof
        guess = guess.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:3] == '000000'
        # return True or False


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def hello_world():
    response = {
        'text': 'hello world'
    }
    return jsonify(response), 200


# now validating new proof sent by client
@app.route('/mine', methods=['POST'])
def mine():
    # pulling data out of POST
    data = request.get_json()
    print("DATA: ", data)
    # check that 'proof' and 'id' are present
    if data is not None:
        if data["id"] is False or data["proof"] is False:
            response = {
                "message": "missing id and/or proof"
            }
            # return a 400 error using jsonify(response) with a 'message' if no proof or id
            return jsonify(response), 400

    # for our valid proof function -> convert last block from json into a string for the valid proof function, make sure last block dict is ordered so we don't have inconsistent hashes
    last_block_string = json.dumps(blockchain.last_block, sort_keys=True)

    # check if whats being sent is a valid proof -  return True or False
    if blockchain.valid_proof(last_block_string, data["proof"]):
        # hash the previous block
        previous_hash = blockchain.hash(blockchain.last_block)
        # append new block to the chain with validated proof (from client) and previous hash added to the block
        block = blockchain.new_block(data["proof"], previous_hash)
        # success message to client
        response = {
            "message": "new block has been forged",
            "block": block
        }
       # if not and proof is not valid, sent back an invalid response message
    else:
        response = {
            "message": "Proof is invalid"
        }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():  # gives us our total chain so we can see, we can process it.
    response = {
        # TODO: Return the chain and its current length
        'len': len(blockchain.chain),  # length of chain
        'chain': blockchain.chain  # chain itself
    }
    return jsonify(response), 200

# Add an endpoint called last_block that returns the last block in the chain
@app.route('/lastblock', methods=['GET'])
def last_block():
    response = {
        # returns the last block in the chain
        'last block': blockchain.last_block
    }
    return jsonify(response), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# proof of work example: (above, do the same with block instead of s)
# looking for a hash with 3 leading zeros
# result = "123456"
# while result[:4] != "0000":
#     s = str(random.random())
#     result = hashlib.sha256(s.encode()).hexdigest()  # hash in string format
#     print(result)  # all the work the computer is doing, trying all these different hashes. the blockchain is asking for proof of all this work

# # hashed key string and resulting hash output.
# print(f"{s} - {result}")

# s is going to be our salt, we're hashing our salt until we get to that proof with 3 leading zeros.
# if we want to make it even more difficult, we could add on another digit. this is proof of work.
# this all bitcoin mining is just trying different strings, picking a random number, trying a different string and hashing it until you get to the 19 leading zeros for bitcoin.
