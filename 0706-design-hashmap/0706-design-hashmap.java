import java.util.ArrayList;
import java.util.List;

class ListNode {
    int key;
    int value;
    ListNode next;
    public ListNode(int _key, int _val) {
        key=_key;
        value=_val;
    }
}

class MyHashMap {
    int m;
    List<ListNode> h;
    public MyHashMap() {
        m = 1000;
        h = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            h.add(null);
        }
    }
    
    
    public void put(int key, int value) {
        int index = key % m;
        if (h.get(index) == null) {
            h.set(index, new ListNode(key, value));
        } else {
            ListNode cur = h.get(index);
            ListNode pre= null;
            while (cur!=null) {
                if (cur.key == key) {
                    cur.value = value;
                    return;
                }
                pre=cur;
                cur = cur.next;
            }
            pre.next = new ListNode(key, value);
        }
    }
    
    
    
    public int get(int key) {
        int index = key % m;
        ListNode cur = h.get(index);
        if (cur!=null){
        while (cur != null) {
            if (cur.key == key) {
                return cur.value;
            }
            cur = cur.next;
        }}
        return -1;
    }
    
    public void remove(int key) {
        int index = key % m;
        ListNode cur = h.get(index);
        if (cur == null) return;
        else if (cur.key == key) {
            h.set(index, cur.next);
            cur.next=null;
        } else {
            ListNode prev = null;
            while (cur != null) {
                if (cur.key == key) {
                    prev.next = cur.next;
                    break;
                }
                prev = cur;
                cur = cur.next;    
            }
        }
    }
}
