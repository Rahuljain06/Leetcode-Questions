class DLLNode{
    int key;
    int value;
    DLLNode next;
    DLLNode prev;
    int nodefreq;
    
    public DLLNode(int key, int value){
        this.key=key;
        this.value=value;
        this.nodefreq=1;
    }
}

class DLL{
    int DLLsize;
    DLLNode head;
    DLLNode tail;
    
    public DLL(){
        
        head = new DLLNode(0,0);
        tail=new DLLNode(0,0);
        head.next=tail;
        tail.prev=head;
        DLLsize=0;
    }
    
    public void removeNode(DLLNode node){
        node.prev.next=node.next;
        node.next.prev=node.prev;
        DLLsize--;
    }
    
    public void addNode(DLLNode node){
        DLLNode nxt=head.next;
        head.next=node;
        node.prev=head;
        nxt.prev=node;
        node.next=nxt;
        DLLsize++;
        
    }
}
class LFUCache {
    
    HashMap<Integer,DLL> freqmap;
    HashMap<Integer,DLLNode> cache;
    int minfreq;
    int capacity;
    int cursize;

    public LFUCache(int capacity) {
        freqmap= new HashMap<>();
        cache= new HashMap<>();
        this.capacity=capacity;
        minfreq=0;
        cursize=0;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)){
            DLLNode node=cache.get(key);
            update(node);
            return node.value;
        }
        return -1;
    }
    
    public void update(DLLNode node){
        int freq=node.nodefreq;
        DLL list=freqmap.get(freq);
        list.removeNode(node);
        
        if (freq==minfreq  && list.DLLsize==0)
            minfreq++;
        
        node.nodefreq++;
        
        DLL newlist=freqmap.getOrDefault(node.nodefreq,new DLL());
        newlist.addNode(node);
        cache.put(node.key,node);
        freqmap.put(node.nodefreq,newlist);
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)){
            DLLNode node= cache.get(key);
            node.value=value;
            update(node);
        }
        else{
            cursize++;
            if (cursize>capacity){
                DLL list=freqmap.get(minfreq);
                cache.remove(list.tail.prev.key);
                list.removeNode(list.tail.prev);
                cursize--;
            }
            
            minfreq=1;
            DLL list=freqmap.getOrDefault(minfreq, new DLL());
            DLLNode newnode= new DLLNode(key,value);
            list.addNode(newnode);
            cache.put(key,newnode);
            freqmap.put(minfreq, list);
            
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */