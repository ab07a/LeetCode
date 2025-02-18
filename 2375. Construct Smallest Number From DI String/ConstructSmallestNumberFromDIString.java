
public class ConstructSmallestNumberFromDIString {
    public String smallestNumber(String pattern) {
        int n = pattern.length();
        int[] patternArray = new int[n+1];
        int temp=0, temp2=0;
        boolean flag = false;
        for (int i=n-1; i>-1; i--){
            if (pattern.charAt(i)=='D') {
                temp++;
                patternArray[i] = temp;
            }
            else{
                temp=0;
            }
        }
        
        temp = 1;
        for (int i=0; i<n+1; i++){
            if (patternArray[i] == 0 && !flag) {
                patternArray[i] = temp;
                temp++;
            }else if (patternArray[i] == 0 && flag) {
                patternArray[i] = temp;
                temp = temp2+1;
                flag = false;
            }else{
                patternArray[i] += temp;
                if (!flag) {
                    temp2 = patternArray[i];
                    flag = true;
                }
            }
        }
        String sol="";
        for (int i: patternArray){
            sol+=i;
        }
        return sol;
    }
    public static void main(String[] args) {
        ConstructSmallestNumberFromDIString cDiString = new ConstructSmallestNumberFromDIString();
        System.out.println(cDiString.smallestNumber("IIIDIDDD"));
    }
}
