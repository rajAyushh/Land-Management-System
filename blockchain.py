import hashlib
from sqlite3 import Timestamp
import random
import string
from datetime import datetime
from this import s
from typing_extensions import Self
import random
import pytz
from merkleTree import MerkleTreeHash

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Mysqlpwd@123", database="land_management")
mycursor = mydb.cursor()

mycursor.execute(f"SELECT COUNT(publicKey) FROM witness")
noOfUsers = mycursor.fetchone()[0]
blockchain = []
ver = 0
prevBlockHash = 0
minter = ""

class Block:
    def __init__(self):
        self.transactionsList = []
        self.witnessList = {}
        self.maxwitness = ""

    

    def new_transaction(self):
        '''Function for a new transaction between a seller and a buyer'''
        # Adds a new transaction to the list of transactions
        print("Enter Buyer ID: ")
        buyerId = input()
        mycursor.execute(f"SELECT COUNT(witness.privateKey) FROM witness WHERE publicKey = '{buyerId}'")
        cnt1 = mycursor.fetchone()[0]
        if (cnt1 == 0):
            print("user not found")
            return

# checks if buyer Exists
        print("Enter Seller ID: ")
        sellerId = input()
        mycursor.execute(f"SELECT COUNT(witness.privateKey) FROM witness WHERE publicKey = '{sellerId}'")
        cnt2 = mycursor.fetchone()[0]
        if (cnt2 == 0):
            print("user not found")
            return

# checks if seller Exists
        print("Enter Seller private key: ")
        privateKeyOfSeller = input()
        privateKeyOfSellerHash = hashlib.sha256(privateKeyOfSeller.encode()).hexdigest()
        mycursor.execute(f"SELECT COUNT(witness.privateKey) FROM witness WHERE witness.privateKey = '{privateKeyOfSellerHash}'")
        cnt3 = mycursor.fetchone()[0]
        if (cnt3 == 0):
            print("user not found")
            return

#Checks private key hash
        print("Enter Property ID: ")
        propertyId = input()
        mycursor.execute(f"SELECT COUNT(witness.propertyId_1) FROM witness WHERE witness.propertyId_1 = '{propertyId}'")
        cnt4 = mycursor.fetchone()[0]
        if (cnt4 == 0):
            print("user not found")
            return
        
#checks if propertyId exists

        print("Enter the Amount Paid")
        amount = input()
        timestamp = datetime.now(pytz.timezone('Asia / Calcutta'))
        self.transactionsList.append(self.transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp))

        mycursor.execute(
            f"SELECT stake FROM witness WHERE publicKey = '{sellerId}'")
        stake = mycursor.fetchone()[0]
        mycursor.execute(
            f"SELECT propertyId_1 FROM witness WHERE publicKey = '{sellerId}'")
        id1 = mycursor.fetchone()[0]
        mycursor.execute(
            f"SELECT stake FROM witness WHERE publicKey = '{buyerId}'")
        stake2 = mycursor.fetchone()[0]
        stake += stake2
        # print(stake,id1)
        mycursor.execute(
            f"UPDATE witness SET stake = NULL, propertyId_1 = NULL WHERE publicKey = '{sellerId}'")
        mycursor.execute(
            f"UPDATE witness SET stake = 'stake', propertyId_2 = 'id1' WHERE publicKey = '{buyerId}'")

        mycursor.execute(
            f"DELETE stake, propertyId FROM witness WHERE publicKey = '{sellerId}'")
        mycursor.execute(f"""INSERT INTO transactions(buyer, seller, property_id, amount, timestamp) 
        values({buyerId},
               {sellerId},
               {propertyId},
               {amount},
               {timestamp})""")
    # pushes all of the transaction details into sql MusicMG
        return

# Hashing the transaction ID to secure the data
    def transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp):
        transactionStatement = "Group48" + str(buyerId) + str(sellerId) + str(propertyId) + str(amount) + str(timestamp)
        return hashlib.sha256(transactionStatement.encode()).hexdigest()


# Function to push hashed transaction list into MerkleTree code

    def merkle_push(transactionsList):
        cls = MerkleTreeHash
        mk = cls.find_merkle_tree(transactionsList)
        return mk


# DPoS Implementation
# We have separate functions Registration of Witness from stakeholders and
# Voting for witnesses, so as to find a weighted vote for the witnesses


    def registerForWitness(self):
        reg = int(input("Do you want to be a Witness? {0 for No/ any other for yes}"))

        if reg == 0:
            print("Selected No")

        else:
            print("Selected Yes")
            # Enter public ID
            publicId = input("Enter your Public Key for Witness registration: ")
            self.witnessList[publicId]=0
            print("Success")
        return

    def voteForWitness(self):
        global minter
        mycursor.execute("SELECT * from witness")
        result = mycursor.fetchall()
        for row in result:
            print(f"Your Public Key is: {row[0]}")
            stake = row[2]
            self.witnessListPrinter()
            candidate = input("Choose your respective candidate: ")
            self.witnessList[candidate] += stake
        minter = max(self.witnessList, key= lambda x: self.witnessList[x])
        print(f"Witness with maximum votes is: {minter}")

    # Function to print the list of witnesses

    def witnessListPrinter(self):
        print("Following are the witnesses: ")
        [print(keys) for keys in self.witnessList]
        return


# BLOCK MINTING

class NewBlock:

    def __init__(self):
        self.timestamp= datetime.now(pytz.timezone('Asia / Calcutta'))
        self.merkleRoot=Block.merkle_push()
        self.nonce = random.randint(10000, 99999)

    def new_block(self):
        ver = ver+1
        if prevBlockHash == 0:
            prevBlockHash = hashlib.sha256("genesisGrp48".encode()).hexdigest()
        block = {
            'version': ver,
            'timestamp': self.timestamp,
            'merkleRoot': Block.merkle_push(),
            'nonce': self.nonce,
            'witness': minter,
            'prevBlockHash': self.prevBlockHash,
            'CurrentBlockHash': hashlib.sha256((str(ver)+str(self.timestamp)+str(self.nonce)+self.merkleRoot+prevBlockHash).encode()).hexdigest(),
        }
        prevBlockHash = getattr(block, 'CurrentBlockHash')


    # Function for printing the block

    def print_block(self):
        print("Block Version: " + getattr(block, 'CurrentBlockHash'))
        print("Timestamp: ")
        print("Block Merkle Root: ")
        print("Block nonce: ")
        print("Block Previous Block Hash: ")
        print("Block Witness: ")
        print("Block Current Block Hash: ")


# Function for Registration of a new node


def registerNode():
    global noOfUsers
#keeps no of users as a variable
    print("Enter Your Name:")
    name = input()
    publicId = name+"_"+str(noOfUsers+1)
    print("How many Acres of Land do you have? (As confirmed by Land Authority)")
    stake = input()
    propertyId = str(stake) + "grp48".join(random.choices(string.ascii_uppercase + string.digits, k=3))
    privateKey = publicId + "group48"
#hashes a private key such that it contains publicId as an input
    privKeyHash = hashlib.sha256(privateKey.encode()).hexdigest()
    print("Your unique ID(public key) is "+publicId)
    print("Your unique private key is "+privateKey)
    print("Your Land Stake is "+stake)
    print("Your unique Property ID is "+propertyId)
    mycursor.execute(f"""INSERT INTO witness(publicKey, privateKey, stake, propertyId_1) 
        values('{publicId}',
            '{privKeyHash}',
            {stake},
            '{propertyId}')""")
    mydb.commit()
    noOfUsers += 1
    return


# main

current_block = Block()

print('''Welcome to Happy Hearts Land management System
      
Choose one of the following options: 

1. Register New User
2. View Transaction History
3. Witness Registration
4. Vote for Witness
5. Buy property
6. Sell property
7. Mint Block
8. Exit
9. Clear''')



while True:
    print("Enter a number between 1 & 9")
    n = int(input())

    if n == 1:
        registerNode()
    elif n == 2:
        mycursor.execute("SELECT * from transactions")
        result = mycursor.fetchall()
        print(result)
    elif n == 3:
        current_block.registerForWitness()
    elif n == 4:
        current_block.voteForWitness()
    elif n == (5 or 6):
        current_block.new_transaction()
    elif n == 7:
        NewBlock.print_block()
    elif n == 8:
        break
    elif n == 9:
        mycursor.execute("DELETE from transactions")
        mycursor.execute("DELETE from witness")
    else:
        print("Kindly choose between 1 to 9")
