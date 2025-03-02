import java.util.*;

public class MergeTwo2DArraysbySummingValues {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        Map<Integer, Integer> map = new TreeMap<>();

        for (int[] num : nums1) {
            map.put(num[0], map.getOrDefault(num[0], 0) + num[1]);
        }
        for (int[] num : nums2) {
            map.put(num[0], map.getOrDefault(num[0], 0) + num[1]);
        }

        int[][] res = new int[map.size()][2];
        int count = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()){
            res[count][0] = entry.getKey();
            res[count][1] = entry.getValue();
            count++;
        }
        return res;
    }
}
