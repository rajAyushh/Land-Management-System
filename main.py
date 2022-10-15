class Node{
    int ids;
    int stake;
};
    
class Transaction{
    int buyer_id;
    int seller_id;
    int property_id;
    int timestamp;
};

void add_node(){
    cout<<"Enter your id";
    cin>>ids;
    cout<<"Enter your stake";
    cin>>stake;
};

class Blockchain(){
  int last_block;
  int previous_hash;
  int block;
};

class pool(){
  int length;
}


void transaction(){
    cout<<"Enter seller ID";
    cin>>id_1;
    cout<<"Enter buyer ID";
    cin>>id_2;
    
    for(int i=0;i<n;i++){
        if(id_1 == nodes[i].id){
            p_id = nodes[i].stake;
        }
    }
    
    dateTime timestamp = dateTime(now);
    
    if(verify_trans(id_1,id_2,p_id,timestamp)){
        add_block(id_1,id_2,p_id,timestamp);
    }
}


void transaction(){
    cout<<"Enter seller ID";
    cin>>id_1;
    cout<<"Enter buyer ID";
    cin>>id_2;
    
    for(int i=0;i<n;i++){
        if(id_1 == nodes[i].id){
            p_id = nodes[i].stake;
        }
    }
    
    timestamp = dateTime(now);
    
    if(verify_trans(id_1,id_2,p_id,timestamp)){
        add_block(id_1,id_2,p_id,timestamp);
    }
}
// voting and all dekho ke karo

bool verify(int id_1, int id_2, int p_id, dateTime timestamp){
    
    //code copied from other website in python
    
     def add_vote(self):
        self.all_nodes = list(self.nodes)

        for x in self.all_nodes:
            y=list(x)
            y.append(x[1] * randint(0,100))
            self.voteNodespool.append(y)

        print(self.voteNodespool)
    

    # Method for selecting top three nodes based on results produced by voting

    def selection(self):
        self.starNodespool = sorted(self.voteNodespool, key = lambda vote: vote[2],reverse = True)
        print(self.starNodespool)

        for x in range(3):
            self.superNodespool.append(self.starNodespool[x])
        print(self.superNodespool)

        for y in self.superNodespool:
            self.delegates.append(y[0])
        print(self.delegates)
           

}



int main(){
  /* Implement a switch here in place of 30 entries */
  Node nodes[30];
  for(int i=0;i<30;i++){
    nodes[i].add_node();
  }
  
  
  
}
