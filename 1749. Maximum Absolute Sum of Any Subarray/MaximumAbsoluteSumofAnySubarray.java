public class MaximumAbsoluteSumofAnySubarray {
    public int maxAbsoluteSum(int[] nums) {
        int max = 0, min = 0, sum = 0;
        for (int i: nums){
            sum += i;
            max = Math.max(sum, max);
            min = Math.min(min, sum);
        }
        return max-min;
    }
    public static void main(String[] args) {
        MaximumAbsoluteSumofAnySubarray mSubarray = new MaximumAbsoluteSumofAnySubarray();
        System.out.println(mSubarray.maxAbsoluteSum(new int[]{2,-5,1,-4,3,-2}));
    }
}
