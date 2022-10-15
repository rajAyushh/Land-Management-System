import hashlib
from sqlite3 import Timestamp
import uuid
import random
import string
import datetime
from pytz import timezone
global ver
ver = 0
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
        global noOfUsers
        noOfUsers=0

    #def verify_transaction_signature(self, sender_address, signature, transaction):
        #DPOS use karna hai
    #registerNOde
#    def registerWitness(self, node_id):
 #       #adding newer nodes to the set of nodes
  #      if node_id.startswith("grp48") and node_id.endswith("f452"):
   #         self.nodes.add(node_id)
    #    else:
    #       raise ValueError('Invalid node id')
    def registerNode(self):
        noOfUsers=noOfUsers+1
        print("Enter Your Name:")
        name=input()
        nodeId=name+"_"+noOfUsers
        #code to push name to sql MusicMG
        print("How many Acres of Land do you have? (As confirmed by Land Authority)")
        land=input()
        propertyId = land+"".join(random.choices(string.ascii_uppercase + string.digits, k=3))
        #code to push propID to sql MusicMG
        print("Your unique ID(public key) is "+nodeId)
        print("Your unique Property ID is "+propertyId)

    def registerForWitness(self):
        #edit winess field in mysql everytime function called
        for x in range(1, "#SQL se no of inputs nikalni hai"):
            reg=input("Do you want to be a Witness? {0 for No/ any other for yes}")
            if reg==0:
                continue
            else:
                pass
                #push yes in witness field in mysql


    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        print("Enter Buyer ID: ")
        buyerId=input()
        #checks if buyer Exists MusicMG
        print("Enter Seller ID: ")
        sellerId=input()
        #checks if seller Exists MusicMG
        print("Enter Property ID: ")
        propertyId=input()
        #checks if propID Exists MusicMG
        print("Enter the Amount Paid")
        amount=input()
        timestamp = datetime.now(pytz.timezone('Asia / Calcutta'))
        #pushes all of the transaction details into sql MusicMG
        trxnId = transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp)

    
    def transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp):
        transactionStatement="Group48" + str(buyerId) + str(sellerId) + str(propertyId) + str(amount) + str(timestamp)
        return hashlib.sha256(transactionStatement.encode()).hexdigest()

    def 

#BLOCK MINTING
    @staticmethod
    def new_block(self, DPOS, prevBlockHash, nonce, ver):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.currentTransactions,
            'nonce': nonce,
            #'treeRoot':,
            #'witnessAddress:,
            'version': ver+1,
            'prevBlockHash': prevBlockHash or "genesisGrp48",
        }
        ver = ver+1
        # Reset the current list of transactions
        self.currentTransactions = []

        self.chain.append(block)
        return block


    @staticmethod
    def hash(self, prevBlockHash, transactionsList, nonce):
        # Hashes a Block
        self.blockData = prevBlockHash+"group48" + \
            ctime(time())+nonce+" ".join(transactionsList)
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

print("Choose one of the following options: "\n)
