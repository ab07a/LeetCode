public class FindMissingAndRepeatedValues {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length, sum = 0;
        n*=n;
        int[] visited = new int[n], sol = new int[2];
        for (int[] row:grid){
            for(int nums:row){
                if(visited[nums-1] == 1){
                    sol[0] = nums;
                    sum-=nums;
                }
                visited[nums-1] = 1;
                sum+=nums;
            }
        }
        sol[1] = n*(n+1)/2 - sum;
        return sol;
    }
    public static void main(String[] args) {
        FindMissingAndRepeatedValues fValues = new FindMissingAndRepeatedValues();
        System.out.println(fValues.findMissingAndRepeatedValues(new int[][]{{1, 3},{2, 2}}));
    }
}
