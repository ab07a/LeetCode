public class ApplyOperationsToAnArray {
    public int[] applyOperations(int[] nums) {
        int n = nums.length, i, count = 0;
        for (i=0;i<n-1;i++){
            if (nums[i] == 0){
                count++;
                continue;
            }
            if (nums[i] == nums[i+1]){
                nums[i] *= 2;
                nums[i+1] = 0;
            }
            nums[i-count] = nums[i];
            if(count!=0){
                nums[i] = 0;
            }
        }
        nums[i-count] = nums[n-1];
        if (count!=0){
            nums[n-1] = 0;
        }

        return nums;
    }
}
