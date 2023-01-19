class Solution {
    public int mostWordsFound(String[] s) {
        int max=0;
        for(int i=0; i<s.length; i++) {
            max = Math.max(max,(s[i].split(" ")).length);
        }
        return max;
    }
}