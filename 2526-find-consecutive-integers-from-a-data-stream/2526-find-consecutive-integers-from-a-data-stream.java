class DataStream {
    int cnt,val,k;
    public DataStream(int value, int k) {
        this.val=value;
        this.k=k;
    }
    
    public boolean consec(int num) {
        if (num==this.val)
            cnt++;
        else
            cnt=0;
        return cnt>=this.k;
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = new DataStream(value, k);
 * boolean param_1 = obj.consec(num);
 */