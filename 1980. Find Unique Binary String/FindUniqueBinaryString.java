public class FindUniqueBinaryString {
    public String findDifferentBinaryString(String[] nums) {
        String sol = "";
        char curr;
        for (int i=0; i<nums.length; i++){
            curr = nums[i].charAt(i);
            if (curr=='1') {
                sol+='0';
            }else{
                sol+='1';
            }
        }
        return sol;   
    }
    public static void main(String[] args) {
        FindUniqueBinaryString fString = new FindUniqueBinaryString();
        System.out.println(fString.findDifferentBinaryString(new String[]{"111","011","001"}));
    }
}
