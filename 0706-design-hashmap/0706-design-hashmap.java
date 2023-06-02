import java.util.ArrayList;
import java.util.List;

class ListNode {
    int[] pair;
    ListNode next;
    public ListNode(int key, int val) {
        pair = new int []{key, val};
        next=null;
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
                if (cur.pair[0] == key) {
                    cur.pair[1] = value;
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
        while (cur != null) {
            if (cur.pair[0] == key) {
                return cur.pair[1];
            }
            cur = cur.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int index = key % m;
        ListNode cur = h.get(index);
        if (cur == null) return;
        if (cur.pair[0] == key) {
            h.set(index, cur.next);
            cur.next=null;
        } else {
            ListNode prev = cur;
            cur = cur.next;
            while (cur != null) {
                if (cur.pair[0] == key) {
                    prev.next = cur.next;
                    break;
                } else {
                    prev = cur;
                    cur = cur.next;
                }
            }
        }
    }
}
