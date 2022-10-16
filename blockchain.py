import hashlib
from sqlite3 import Timestamp
import random
import string
import datetime
import pytz
from pytz import timezone
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="raju", passwd="1234", database="land_management")
mycursor = mydb.cursor()
# new user wallet generator public/private key
#send and recieve
# transaction addition to block


class Block:
    def __init__(self):
        self.transactionsList = []
        self.chain = []
        self.nodes = set()
        # Generate random number to be used as node_id
        self.node_id = "grp48ABCf452"
        # Create genesis block
        self.create_block(0, '00')
        global noOfUsers
        noOfUsers = 0
        global ver
        ver = 0
        global prevBlockHash
        prevBlockHash = 0
        global minter

    # def verify_transaction_signature(self, sender_address, signature, transaction):
        # DPOS use karna hai

    def registerNode(self):
        noOfUsers = noOfUsers+1
        print("Enter Your Name:")
        name = input()
        nodeId = name+"_"+noOfUsers
        # code to push name to sql MusicMG
        print("How many Acres of Land do you have? (As confirmed by Land Authority)")
        land = input()
        propertyId = land + "".join(random.choices(string.ascii_uppercase + string.digits, k=3))
        # code to push propID to sql MusicMG
        print("Your unique ID(public key) is "+nodeId)
        print("Your unique private key is ")
        print("Your unique Property ID is "+propertyId)

    def registerForWitness(self):
        witnessList = []
        voteCount = []
        # edit winess field in mysql everytime function called
        for x in range(1, "#SQL se no of stakeholders nikalni hai"):
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

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        print("Enter Buyer ID: ")
        buyerId = input()
        # checks if buyer Exists MusicMG
        print("Enter Seller ID: ")
        sellerId = input()
        # checks if seller Exists MusicMG
        print("Enter Property ID: ")
        propertyId = input()
        # checks if propID Exists MusicMG
        print("Enter the Amount Paid")
        amount = input()
        timestamp = datetime.now(pytz.timezone('Asia / Calcutta'))

        mycursor.execute(f"""INSERT INTO transactions(buyer, seller, property_id, timestamp) 
        values({buyerId},
               {sellerId},
               {propertyId},
               {timestamp})""")
        # pushes all of the transaction details into sql MusicMG

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        print("Enter Buyer ID: ")
        buyerId = input()
        # checks if buyer Exists MusicMG
        print("Enter Seller ID: ")
        sellerId = input()
        # checks if seller Exists MusicMG
        print("Enter Property ID: ")
        propertyId = input()
        # checks if propID Exists MusicMG
        print("Enter the Amount Paid")
        amount = input()
        timestamp = datetime.now(pytz.timezone('Asia / Calcutta'))

        mycursor.execute(f"""INSERT INTO transactions(buyer, seller, property_id, timestamp) 
        values({buyerId},
               {sellerId},
               {propertyId},
               {timestamp})""")
        # pushes all of the transaction details into sql MusicMG

    def transactionHashCalculator(self, buyerId, sellerId, propertyId, amount, timestamp):
        transactionStatement = "Group48" + \
            str(buyerId) + str(sellerId) + \
            str(propertyId) + str(amount) + str(timestamp)
        return hashlib.sha256(transactionStatement.encode()).hexdigest()

    def voteForWitness(witnessList, voteCount):
        for x in range(1, "No. Of stakeholders"):
            print("Your Public Key is: "+"SQL se nth bande ki public key")
            listPrinter()
            stake = "SQL se nth bande ki stake"
            voteNumber = input("Choose your respective candidate")
            voteCount[voteNumber] = voteCount[voteNumber]+stake
        maxValue = max(voteNumber)
        maxIndex = voteNumber.index(maxValue)
        minter = witnessList[maxIndex]

    def listPrinter(witnessList):
        for x in range(0, len(witnessList)):
            print(x+". "+witnessList[x])


# BLOCK MINTING


    @staticmethod
    def new_block(prevBlockHash, ver, merkelRoot):
        ver = ver+1
        if prevBlockHash == 0:
            prevBlockHash = hashlib.sha256("genesisGrp48".encode()).hexdigest()
        block = {
            'version': ver,
            'timestamp': datetime.now(pytz.timezone('Asia / Calcutta')),
            'merkelRoot': """merkel root""",
            'minter': minter,
            'prevBlockHash': prevBlockHash,
            'currentBlockHash': merkelRoot,
        }
        prevBlockHash = currentBlockHash
        return block


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
n = input()
if n == 1:
    Block.registerNode()
elif n == 2:
    mycursor.execute("SELECT * from transactions")
elif n == 3:
    # vote fxn
    pass
elif n == 4:
    Block.registerForWitness()
elif n == (5 or 6):
    Block.new_transaction()
elif n == 7:
    blockblockbuster = Block.new_block(prevBlockHash, ver, merkelRoot)
    print("Version No." + blockblockbuster)
elif n == 8:
    exit
elif n == 9:
    mycursor.execute("DELETE from transactions")
else:
    print("Kindly choose between 1 to 7")
    exit
