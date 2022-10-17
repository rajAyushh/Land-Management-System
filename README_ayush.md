Blockchain Project Assignment  1

Objective
●	This assignment to build a land management system with the following features:
1.	To register new users to the system with previously owned property
2.	The user should be able to buy and sell the property.
3.	To improve the security of the blockchain, incorporate a consensus algorithm that has been assigned to the group.
4.	Implementation of Merkle root to calculate the hash of all the transactions in a block.
5.	To be able to view the transaction history that is related to a property.
●	This assignment focuses on implementing the consensus algorithm - Delegated Proof of Stake.

Team members - (Group 48)
1.	Ayush Raj (2020AAPS0439H)
2.	Manan Gupta (2020A2PS2420H)
3.	Anant Kumar (2020A3PS2211H)
4.	Saksham Sinha (2020AA0421H)


Basic functionalities of our program-

1.	Register New User

2.	View Transaction History

3.	Vote for Witness

4.	Witness Registration

5.	Buy property

6.	Sell property

7.	Mint Block

8.	Exit

9.	Clear

 


All the methods are properly defined in the Blockchain class of blockchain.py
 

Delegated Proof of Stake (DPoS) algorithm
Delegated proof of stake (DPoS) is a verification and consensus mechanism in the blockchain . It competes with other proof of work and proof of stake models as a way to verify transactions and promote blockchain organization.
A trustworthy, strong, scalable, and effective consensus method for blockchain technology is DPoS. It is an improvement above the common Proof of Stake (PoS). In DPoS, each node with a stake in the system has the ability to vote to assign other nodes the responsibility of validating transactions.
Here, in DPoS ,user's vote weight is proportional to their stake rather than block mining being tied to the stakeholders' total tokens.

Implementation of DPoS in Land Management System's Blockchain

●	Implemented the option to be a witness if the user wants (DPOS)
 
●	New transaction dpos implementation-
 
●	A simple program to print the list of all witnessess.
 


 







Methods in blockchain.py
●	We made a class named block and implemented the features in it.

●	Following is the basic skeleton of the block for initialising a new transaction.
 


●	Resgister a new user (Basic feature)

 
●	The following is responsible for adding a new transaction. This takes buyer id, seller id, property id and timestamp as input. (Basic feature)

 



●	We used the following code for getting the hash of the transaction. We made a transaction hash calculator. For this we used inbult python library and function. ( hashlib.sha256 )  
 


●	What is the SHA-256 Algorithm?
●	SHA 256 is a part of the SHA 2 family of algorithms, where SHA stands for Secure Hash Algorithm. Published in 2001, it was a joint effort between the NSA and NIST to introduce a successor to the SHA 1 family, which was slowly losing strength against brute force attacks.
●	The significance of the 256 in the name stands for the final hash digest value, i.e. irrespective of the size of plaintext/cleartext, the hash value will always be 256 bits.


 
Merkle Tree
In cryptography and computer science, a hash tree or Merkle tree is a tree in which every "leaf" (node) is labelled with the cryptographic hash of a data block, and every node that is not a leaf (called a branch, inner node, or inode) is labelled with the cryptographic hash of the labels of its child nodes. A hash tree allows efficient and secure verification of the contents of a large data structure. A hash tree is a generalization of a hash list and a hash chain.
Demonstrating that a leaf node is a part of a given binary hash tree requires computing a number of hashes proportional to the logarithm of the number of leaf nodes in the tree. Conversely, in a hash list, the number is proportional to the number of leaf nodes itself. A Merkle tree is therefore an efficient example of a cryptographic commitment scheme, in which the root of the tree is seen as a commitment and leaf nodes may be revealed and proven to be part of the original commitment.
 
Merkle Tree Implementation
We implemented a merkle tree hash function that takes our transaction object as input and produces a hash of the same.
 

