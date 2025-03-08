public class MinimumRecolorsToGetKConsecutiveBlackBlocks {
    public int minimumRecolors(String blocks, int k) {
        int count=0,sol,n = blocks.length();
        for(int i = 0;i<k; i++){
            if(blocks.charAt(i)=='W'){
                count++;
            }
        }
        sol = count;
        for(int i = k;i<n;i++){
            if(blocks.charAt(i)=='W'){
                count++;
            }
            if(blocks.charAt(i-k)=='W'){
                count--;
            }
            sol = Math.min(count,sol);
        }
        return sol;
    }
    public static void main(String[] args) {
        MinimumRecolorsToGetKConsecutiveBlackBlocks mBlocks = new MinimumRecolorsToGetKConsecutiveBlackBlocks();
        System.out.println(mBlocks.minimumRecolors("WWBWBWBWBW", 2));
    }
}
