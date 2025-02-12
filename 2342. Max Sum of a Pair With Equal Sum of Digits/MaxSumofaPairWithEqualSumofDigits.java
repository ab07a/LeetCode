import java.util.Arrays;

public class MaxSumofaPairWithEqualSumofDigits {
    public int numberSum(int x){
        int temp = 0;
        while (x != 0) {
            temp += x%10;
            x /= 10;
        }
        return temp;
    }

    public int maximumSum(int[] nums) {
        Arrays.sort(nums);
        int sol = -1, temp = 0;
        int[] numArr = new int[82];

        for(int i : nums){
            temp = numberSum(i);
            if (numArr[temp] != 0) {
                sol = Math.max(sol, numArr[temp]+i); 
            }
            numArr[temp] = i;

        }
        return sol;
    }
    public static void main(String[] args) {
        MaxSumofaPairWithEqualSumofDigits mDigits = new MaxSumofaPairWithEqualSumofDigits();
        System.out.println(mDigits.maximumSum(new int[]{18,43,36,13,7}));
    }
}
