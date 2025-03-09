public class AlternatingGroupsII {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        int temp = -1, n = colors.length, r = colors[k-1], sol = 1;
        for (int i=1; i<k; i++){
            if (colors[i] == colors[i-1]){
                temp = i;
                sol = 0;
            }
        }
        for (int i = 1; i<n; i++){
            if (i==temp){
                temp = -1;
            }
            if (colors[(i+k-1)%n]==r){
                temp = (i+k-1)%n;
            }
            r = colors[(i+k-1)%n];
            if(temp == -1){
                sol++;
            }
        }
        return sol;

    }
    public static void main(String[] args) {
        AlternatingGroupsII aIi = new AlternatingGroupsII();
        System.out.println(aIi.numberOfAlternatingGroups(new int[]{0,1,0,1,0}, 3));
    }
}
