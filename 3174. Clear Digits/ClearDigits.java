public class ClearDigits {
    String clearDigits(String s){
        String sol = "";
        int temp = 0;
        for (int i=s.length()-1; i>=0; i--){
            if (Character.isDigit(s.charAt(i))) {
                temp++;
                continue;
            }
            if (temp == 0) {
                sol = s.charAt(i)+sol;
            }else{
                temp--;
            }
        }
        return sol;
    }
    public static void main(String[] args) {
        ClearDigits cd = new ClearDigits();
        System.out.println(cd.clearDigits("cba34"));
    }
}
