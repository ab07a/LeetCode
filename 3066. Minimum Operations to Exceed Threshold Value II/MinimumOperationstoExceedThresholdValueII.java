import java.util.PriorityQueue;

public class MinimumOperationstoExceedThresholdValueII {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i: nums){
            if (i<k) {
                heap.add(i);
            }
        }    
        int sol = 0;
        int a, b, temp;
        while (heap.size() != 0) {
            if (heap.size() == 1) {
                return sol + 1;
            }
            a = heap.poll();
            b = heap.poll();
            temp = a*2+b;
            if (temp<k && temp>=0) {
                heap.add(a*2+b);
            }
            System.out.println(a+" "+b+" "+heap.size() );
            sol++;
        }
        return sol;
    }
    public static void main(String[] args) {
        MinimumOperationstoExceedThresholdValueII mIi = new MinimumOperationstoExceedThresholdValueII();
        System.out.println(mIi.minOperations(new int[]{999999999,999999999,999999999}, 1000000000));
    }
}
