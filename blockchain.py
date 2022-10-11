import hashlib
from time import time, ctime
import uuid
#new user wallet generator public/private key
#send and recieve
#transaction addition to block
class Block:
    def __init__(self):
        
        self.transactionsList = []
        self.chain = []
        self.nodes = set()
        #Generate random number to be used as node_id
        self.node_id = "grp48ABCf452"
        #Create genesis block
        self.create_block(0, '00')

    #def verify_transaction_signature(self, sender_address, signature, transaction):
        #DPOS use karna hai

    def register_node(self, node_id):
        #adding newer nodes to the set of nodes
        if node_id.startswith("grp48") and node_id.endswith("f452"):
            self.nodes.add(node_id)
        else:
            raise ValueError('Invalid node id')
    
    @staticmethod
    def new_block(self, DPOS, prevBlockHash):
        nonce = uuid.uuid3().hex
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.currentTransactions,
            'nonce':nonce,
            'prevBlockHash': prevBlockHash or "genesisGrp48",
        }

        # Reset the current list of transactions
        self.currentTransactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, areaOfLand, propertyID):
        # Adds a new transaction to the list of transactions
        self.currentTransactions.append({
            'sender': sender,
            'recipient': recipient,
            'Area': areaOfLand,
            'propertyID': propertyID,
            'timestamp': time(),
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(self, prevBlockHash, transactionsList):
        # Hashes a Block
        self.blockData = prevBlockHash+"group48" + ctime(time())+Block.new_block.__getattribute__(nonce)+" ".join(transactionsList)
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()
    
    # TO BE IMPLEMENTED USING DPOS

    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def valid_chain(self, chain):
        #determines if the blockchain is valid or malicious

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n_*-*-*-*-*-*-*-*-*_\n")
            # Check that the hash of the block is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    

genesisBlock=Block("",) 