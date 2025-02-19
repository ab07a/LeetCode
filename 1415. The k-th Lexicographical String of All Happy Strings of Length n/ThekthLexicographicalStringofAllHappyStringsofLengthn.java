import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ThekthLexicographicalStringofAllHappyStringsofLengthn {
    int n,k,l=0;
    String[] sol;
    Map<String, List<String>> map = new HashMap<>();
    
    void happyString(String s, String c){
        if (s.length() == n-1) {
            sol[l] = s+c;
            l++;
        }else{
            happyString(s+c, map.get(c).get(0));
            happyString(s+c, map.get(c).get(1));
        }
    }

    public String getHappyString(int n, int k) {
        this.n = n;
        map.put("a", Arrays.asList("b", "c"));
        map.put("b", Arrays.asList("a", "c"));
        map.put("c", Arrays.asList("a", "b"));
        int temp = 3*(int) (Math.pow(2, n-1));
        this.sol = new String[temp];
        if (sol.length<k){
            return "";
        }
        happyString("", "a");
        happyString("", "b");
        happyString("", "c");
        return sol[k-1];
    }
    public static void main(String[] args) {
        ThekthLexicographicalStringofAllHappyStringsofLengthn tLengthn = new ThekthLexicographicalStringofAllHappyStringsofLengthn();
        System.out.println(tLengthn.getHappyString(3, 9));
    }
}
