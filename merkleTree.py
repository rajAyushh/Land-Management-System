class MerkleTreeHash(object):
    def __init__(self):
        pass
    
    def find_merkle_hash(self, file_hashes):
    
        blocks = []
    
        if not file_hashes:
            raise ValueError(
                'Missing required file hashes')
            
        for m in sorted(file_hashes):
            blocks.append(m)
            
        list_len = len(blocks)
        
        while list_len%2 != 0:
            blocks.extend(blocks[-1:])
            list_len = len(blocks)
            
        secondary = []
    
        for k in [blocks[x:x+2] for x in range(0, len(blocks), 2)]:
            hasher = hashlib.sha256()
            hashlib.sha256().update(k[0] + k[1])
            secondary.append(hasher.hexdigest())
        
        if len(secondary) == 1:
            return secondary[0][0:64]
        else:
            self.find_merkle_hash(secondary)
            
