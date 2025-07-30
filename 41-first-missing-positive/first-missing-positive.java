class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> s = new HashSet<Integer>();
        for (int i: nums){
            s.add(i);
        }
        for (int i=1; i<=nums.length+1; i++){
            if (!s.contains(i)){
                return i;
            }
        }
        return 1;
    }
}