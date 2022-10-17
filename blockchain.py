import hashlib
from sqlite3 import Timestamp
import random
import string
import datetime
import pytz
from pytz import timezone
from mktreemcc import MerkleTreeHash

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="raju", passwd="1234", database="land_management")
mycursor = mydb.cursor()



class Block:
    def __init__(self):
        self.transactionsList = []
        self.chain = []
        self.nodes = set()
        # Generate random number to be used as node_id
        self.node_id = "grp48ABCf452"
        # Create genesis block
        self.create_block(0, '00')


# Function for Registration of a new node
    def registerNode(self):
        noOfUsers = noOfUsers+1
        print("Enter Your Name:")
        name = input()
        publicId = name+"_"+noOfUsers
        # code to push name to sql MusicMG
        print("How many Acres of Land do you have? (As confirmed by Land Authority)")
        stake = input()
        propertyId = stake + "grp48".join(random.choices(string.ascii_uppercase + string.digits, k=3))
        privateKey = publicId+"group48"
        privKeyHash=hashlib.sha256(privateKey.encode()).hexdigest()
        # code to push propID to sql MusicMG
        print("Your unique ID(public key) is "+publicId)
        print("Your unique private key is "+privateKey)
        print("Your unique Property ID is "+propertyId)
        print("Your Land Stake is "+stake)
        return


# Function for a new transaction between a seller and a buyer
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        print("Enter Buyer ID: ")
        buyerId = input()
        # checks if buyer Exists MusicMG
        print("Enter Seller ID: ")
        sellerId = input()
        # checks if seller Exists MusicMG
        print("Enter Seller private key: ")
        privateKeyOfSeller = input()
        privateKeyOfSellerHash = hashlib.sha256(privateKeyOfSeller.encode()).hexdigest()
        #Check private key hash
        print("Enter Property ID: ")
        propertyId = input()
        #check if propertyId exists
        print("Enter the Amount Paid")
        amount = input()
        timestamp = datetime.now(pytz.timezone('Asia / Calcutta'))
        transactionList.append(Block.transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp))
        #seller id SQL se nikalo Buyer Id me propID daalo and stake delete karo
        mycursor.execute(f"""INSERT INTO transactions(buyer, seller, property_id, timestamp) 
        values({buyerId},
               {sellerId},
               {propertyId},
               {amount,}
               {timestamp})""")
        # pushes all of the transaction details into sql MusicMG
        #SQL seller ki propID se buyerID 
        return

# Hashing the transaction ID to secure the data
    def transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp):
        transactionStatement = "Group48" + str(buyerId) + str(sellerId) + str(propertyId) + str(amount) + str(timestamp)
        return hashlib.sha256(transactionStatement.encode()).hexdigest()
    

# Function to push hashed transaction list into MerkleTree code    
    def merkle_push(transactionList):
        cls = MerkleTreeHash
        mk = cls.find_merkle_tree(transactionList)
        return mk
    
    
    
# DPoS Implementation
# We have separate functions Registration of Witness from stakeholders and 
# Voting for witnesses, so as to find a weighted vote for the witnesses
    
    def registerForWitness(self):
        witnessList = []
        voteCount = []
        # edit winess field in mysql everytime function called
        for x in range(1, noOfUsers):
            reg = input(
                "Do you want to be a Witness? {0 for No/ any other for yes}")

            if reg == 0:
                continue
            else:
                # Enter public ID
                publicId = input(
                    "Enter your Public Key for Witness registration: ")
                witnessList[x] = publicId
                voteCount[x] = 0
                # push yes in witness field in mysql
        print("Success")
        return


    def voteForWitness(self, witnessList, voteCount):
        for x in range(1, noOfUsers):
            print("Your Public Key is: "+"SQL se nth bande ki public key")
            Block.listPrinter(witnessList)
            stake = "SQL se nth bande ki stake"
            voteNumber = input("Choose your respective candidate")
            voteCount[voteNumber] = voteCount[voteNumber]+stake
        maxValue = max(voteNumber)
        maxIndex = voteNumber.index(maxValue)
        minter = witnessList[maxIndex]
        return minter

    # Function to print the list of witnesses

    def listPrinter(self, witnessList):
        for x in range(0, len(witnessList)):
            print(x+". "+witnessList[x])
        return


# BLOCK MINTING


    @staticmethod
    def new_block(prevBlockHash, ver, merkelRoot):
        ver = ver+1
        if prevBlockHash == 0:
            prevBlockHash = hashlib.sha256("genesisGrp48".encode()).hexdigest()
        block = {
            'version': ver,
            'timestamp': datetime.now(pytz.timezone('Asia / Calcutta')),
            'merkelRoot_CurrentBlockHash': Block.merkle_push(),
            'minter': minter,
            'prevBlockHash': prevBlockHash,
        }
        prevBlockHash = getattr(block, 'merkelRoot_CurrentBlockHash')
        return block

    # Function for printing the block

    def print_block():
        print("Block Version No.: "+ getattr())


# main.py

print('''Welcome to Happy Hearts Land management System
      
Choose one of the following options: 

1. Register New User
2. View Transaction History
3. Vote for Witness
4. Witness Registration
5. Buy property
6. Sell property
7. Mint Block
8. Exit
9. Clear''')

blockchain=[]
noOfUsers = 0
ver = 0
prevBlockHash = 0
minter=""
transactionList=[]
n = input()

if n == 1:
    Block.registerNode()
elif n == 2:
    mycursor.execute("SELECT * from transactions")
elif n == 3:
    Block.voteForWitness()
elif n == 4:
    Block.registerForWitness()
elif n == (5 or 6):
    Block.new_transaction()
elif n == 7:
    Block.print_block()
elif n == 8:
    exit
elif n == 9:
    mycursor.execute("DELETE from transactions")
else:
    print("Kindly choose between 1 to 7")
    exit
