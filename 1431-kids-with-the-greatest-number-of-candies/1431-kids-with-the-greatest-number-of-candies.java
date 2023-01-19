class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> list=new ArrayList<>();
        int mx=0;
        for (int i: candies){
            mx=Math.max(mx,i);
        }
        for (int j: candies){
            if (mx>(j+extraCandies))
                list.add(false);
            else
                list.add(true);
        }return list;
    }
}