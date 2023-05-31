class MyHashSet {
        int size;
        int[] arr;
    public MyHashSet() {
      size=(int)1e6+1;
      arr = new int[size];
      
    }
    
    public void add(int key) {
        if (arr[key]==0){
            arr[key]=1;
        }
    }
    
    public void remove(int key) {
        if (arr[key]==1){
            arr[key]=0;
        }
    }
    
    public boolean contains(int key) {
        if (arr[key]==1) return true;
        return false;
    }
}



// class MyHashSet:

//     def __init__(self):
//         self.size=1000
//         self.val=[None]*self.size
        
//     def hash(self,key):
        
//         return key % self.size
    
//     def add(self, key: int) -> None:
        
//         h=self.hash(key)
//         if self.val[h]==None:
//             self.val[h]=[key]
//         elif key in self.val[h]:
//             return
//         else:
//             self.val[h].append(key)
        
//     def remove(self, key: int) -> None:
        
//         h=self.hash(key)
//         if self.val[h] is not None and key in self.val[h]:
//             self.val[h].remove(key)
        
//     def contains(self, key: int) -> bool:
        
//         h=self.hash(key)
//         if self.val[h] is not None and key in self.val[h]:
//             return True
//         return False
/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */