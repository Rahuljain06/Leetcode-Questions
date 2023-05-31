import java.util.ArrayList;

class MyHashSet {
    private int size = 1000;
    private ArrayList<Integer>[] val;

    public MyHashSet() {
        val = new ArrayList[size];
    }

    private int hash(int key) {
        return key % size;
    }

    public void add(int key) {
        int h = hash(key);
        if (val[h] == null) {
            val[h] = new ArrayList<>();
        }
        if (!val[h].contains(key)) {
            val[h].add(key);
        }
    }

    public void remove(int key) {
        int h = hash(key);
        if (val[h] != null) {
            val[h].remove(Integer.valueOf(key));
        }
    }

    public boolean contains(int key) {
        int h = hash(key);
        return val[h] != null && val[h].contains(key);
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