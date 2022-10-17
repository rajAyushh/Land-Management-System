# Blockchain Project Assignment  1



## Objective

●	This assignment to build a land management system with the following features:
1.	To register new users to the system with previously owned property
2.	The user should be able to buy and sell the property.
3.	To improve the security of the blockchain, incorporate a consensus algorithm that has been assigned to the group.
4.	Implementation of Merkle root to calculate the hash of all the transactions in a block.
5.	To be able to view the transaction history that is related to a property.
●	This assignment focuses on implementing the consensus algorithm - Delegated Proof of Stake.



## Team members - (Group 48)

1.	Ayush Raj (2020AAPS0439H)
2.	Manan Gupta (2020A2PS2420H)
3.	Anant Kumar (2020A3PS2211H)
4.	Saksham Sinha (2020AA0421H)



## Basic functionalities of our program-

### 1.	Register New User

### 2.	View Transaction History

### 3.	Vote for Witness

### 4.	Witness Registration

### 5.	Buy property

### 6.	Sell property

### 7.	Mint Block

### 8.	Exit

### 9.	Clear



 <img width="468" alt="image" src="https://user-images.githubusercontent.com/87355361/196222686-8d03bbd5-57c3-4df1-a27a-678a0356bb50.png">




# All the methods are properly defined in the Blockchain class of blockchain.py


 
 <img width="468" alt="image" src="https://user-images.githubusercontent.com/87355361/196222731-fcded486-1729-4390-8073-c710b0422663.png">





# Delegated Proof of Stake (DPoS) algorithm


Delegated proof of stake (DPoS) is a verification and consensus mechanism in the blockchain . It competes with other proof of work and proof of stake models as a way to verify transactions and promote blockchain organization.
A trustworthy, strong, scalable, and effective consensus method for blockchain technology is DPoS. It is an improvement above the common Proof of Stake (PoS). In DPoS, each node with a stake in the system has the ability to vote to assign other nodes the responsibility of validating transactions.
Here, in DPoS ,user's vote weight is proportional to their stake rather than block mining being tied to the stakeholders' total tokens.



# Implementation of DPoS in Land Management System's Blockchain


●	Implemented the option to be a witness if the user wants (DPOS). 
  We ask the user if they wish to be a witness and if so, then we add their name in a list and initialise a VoteCount list where we put
  0 votes for each one.


<img width="435" alt="image" src="https://user-images.githubusercontent.com/87355361/196222815-37b13057-657f-4f68-b255-258c9a56e05b.png">


## Vote for Witness

● We traverse through the entire list to ask for votes from stakeholders by confirming their public IDs and then asking for their votes. 
  According to their stakes we append the votecount for each stakeholder.


<img width="611" alt="Screenshot 2022-10-17 at 10 36 55 PM" src="https://user-images.githubusercontent.com/87355361/196239793-9027bd60-3d8b-446c-8560-08fa8b285f48.png">



 
●	A simple program to print the list of all witnessess.


<img width="468" alt="image" src="https://user-images.githubusercontent.com/87355361/196222949-f83fea56-0090-49de-8f99-4e52f92addd9.png">



<img width="472" alt="image" src="https://user-images.githubusercontent.com/87355361/196223012-6f4e5250-10b4-4563-bc31-be4e16cd0639.png">




# Methods in blockchain.py


●	We made a class named block and implemented the features in it.


●	Following is the basic skeleton of the block for initialising a new transaction.


 
<img width="432" alt="image" src="https://user-images.githubusercontent.com/87355361/196223049-9897f848-1d18-4c0d-a32b-bf6ffcf956ab.png">




●	Resgister a new user (Basic feature)


 <img width="468" alt="image" src="https://user-images.githubusercontent.com/87355361/196223089-8918e992-dfb5-4e5a-8f0c-2e5f1ff02072.png">
 

 
●	The following is responsible for adding a new transaction. This takes buyer id, seller id, property id and timestamp as input. (Basic feature)


<img width="468" alt="image" src="https://user-images.githubusercontent.com/87355361/196223125-6144c830-74e8-4ca5-8ce0-ddab32289965.png">


 

●	We used the following code for getting the hash of the transaction. We made a transaction hash calculator. For this we used inbult python library and function. ( hashlib.sha256 )  

 
 <img width="468" alt="image" src="https://user-images.githubusercontent.com/87355361/196223175-b6af8384-f6e8-4dc5-bb76-34410232f2d6.png">
 
 



## ●	What is the SHA-256 Algorithm?

●	SHA 256 is a part of the SHA 2 family of algorithms, where SHA stands for Secure Hash Algorithm. Published in 2001, it was a joint effort between the NSA and NIST to introduce a successor to the SHA 1 family, which was slowly losing strength against brute force attacks.
●	The significance of the 256 in the name stands for the final hash digest value, i.e. irrespective of the size of plaintext/cleartext, the hash value will always be 256 bits.


<img width="363" alt="image" src="https://user-images.githubusercontent.com/87355361/196223199-945aaff9-cd24-406b-9da8-f63f1601a797.png">



 
# Merkle Tree

In cryptography and computer science, a hash tree or Merkle tree is a tree in which every "leaf" (node) is labelled with the cryptographic hash of a data block, and every node that is not a leaf (called a branch, inner node, or inode) is labelled with the cryptographic hash of the labels of its child nodes. A hash tree allows efficient and secure verification of the contents of a large data structure. A hash tree is a generalization of a hash list and a hash chain.
Demonstrating that a leaf node is a part of a given binary hash tree requires computing a number of hashes proportional to the logarithm of the number of leaf nodes in the tree. Conversely, in a hash list, the number is proportional to the number of leaf nodes itself. A Merkle tree is therefore an efficient example of a cryptographic commitment scheme, in which the root of the tree is seen as a commitment and leaf nodes may be revealed and proven to be part of the original commitment.
 
 
 <img width="341" alt="image" src="https://user-images.githubusercontent.com/87355361/196223257-9db17a09-03dd-43b8-beac-a8554de51fa3.png">

 
 
 
# Merkle Tree Implementation

We implemented a merkle tree hash function that takes our transaction object as input and produces a hash of the same.
We take the transaction IDs and hadh them. After that we add them in an array and values from that array are passed in Merkle tree Code.
In the Merkle Tree function we are checking if the leaf nodes are even or odd and replicate in case of odd.
After that 2 nested for loops are used to combine every 2 hashes at every layer and give a hash that is again used to combine with other hash.
In such way we keep combining hashes until root is reached, and that hash is returned in the end as Merkle Root.


<img width="407" alt="image" src="https://user-images.githubusercontent.com/87355361/196225062-24a28ce5-e172-4f6d-be7b-7af816723e68.png">

 

