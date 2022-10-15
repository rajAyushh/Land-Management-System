import hashlib
from sqlite3 import Timestamp
import uuid
import random
import string
import datetime
from pytz import timezone
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
        global ver
        ver = 0
        global prevBlockHash
        prevBlockHash = 0

    #def verify_transaction_signature(self, sender_address, signature, transaction):
        #DPOS use karna hai

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
        print("Your unique private key is ")
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
        print("Success")


    
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
        trxnId = self.transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp)
        #put trxnID to pool for merkel root calculation

    
    def transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp):
        transactionStatement="Group48" + str(buyerId) + str(sellerId) + str(propertyId) + str(amount) + str(timestamp)
        return hashlib.sha256(transactionStatement.encode()).hexdigest()


#BLOCK MINTING
    @staticmethod
    def new_block(prevBlockHash, ver, currentBlockHash):
        ver=ver+1
        if prevBlockHash ==0:
            prevBlockHash = hashlib.sha256("genesisGrp48".encode()).hexdigest()
        block = {
            'version': ver,
            'timestamp': datetime.now(pytz.timezone('Asia / Calcutta')),
            'merkelRoot': """merkel root""",
            'witnessAddress': """add public key of stakeholder""",
            'prevBlockHash': prevBlockHash,
            'currentBlockHash':currentBlockHash,
        }
        prevBlockHash=currentBlockHash
        return block

    # TO BE IMPLEMENTED USING DPOS


print('''Choose one of the following options: 
1. Register New User
2. View Transaction History
3. Vote for Witness
4. Witness Registration
5. Buy property
6. Sell property
7. Mint Block
8. Exit
9. Clear''')
n=input()
if n==1:
    Block.registerNode()
elif n==2:
    #give them the SQL file
    pass
elif n==3:
    #vote fxn
    pass
elif n==4:
    Block.registerForWitness()
elif n==(5 or 6):
    Block.new_transaction()
elif n == 7:
    Block.new_block()
elif n==8:
    exit
elif n==9:
    #clear sql database
    pass
else:
    print("Kindly choose between 1 to 9")
    exit
