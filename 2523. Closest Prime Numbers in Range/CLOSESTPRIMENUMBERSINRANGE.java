public class CLOSESTPRIMENUMBERSINRANGE {
    public int[] closestPrimes(int left, int right) {
        int[] prime = new int[right+1], sol = new int[]{-1,-1};
        int min = Integer.MAX_VALUE, pre = 0;
        for (int i= 2;i<right+1;i++){
            
            if(prime[i] == 0){
                if(i>=left && pre>=left && pre!=0 && i-pre < min){
                    sol[0] = pre; sol[1] = i;
                    min = i-pre;
                }
                pre = i;
            }
            else{
                continue;
            }
            for(int j = i*i;j<right+1 && j>0;j+=i){
                prime[j] = 1;
            }
        }
        return sol;
    }
    public static void main(String[] args) {
        CLOSESTPRIMENUMBERSINRANGE closestprimenumbersinrange = new CLOSESTPRIMENUMBERSINRANGE();
        System.out.println(closestprimenumbersinrange.closestPrimes(10, 19));
    }
}
