public class ZeroArrayTransformationII {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length,l,r,v,sum = 0,k = 0;
        int[] arr = new int[n+1];
        for(int i=0;i<n;i++){
            sum+=arr[i];
            while (sum<nums[i]){
                if (k==queries.length){
                    return -1;
                }
                l = queries[k][0];
                r = queries[k][1];
                v = queries[k][2];
                arr[l] += v;
                arr[r+1] -= v;
                if (l<=i && i<=r){
                    sum+=v;
                }
                k+=1;
            }
        }
        return k;
    }
    public static void main(String[] args) {
        ZeroArrayTransformationII minZeroArray = new ZeroArrayTransformationII();
        System.out.println(minZeroArray.minZeroArray(new int[]{2,0,2}, new int[][]{{0,2,1},{0,2,1},{1,1,3}}));
    }
}
