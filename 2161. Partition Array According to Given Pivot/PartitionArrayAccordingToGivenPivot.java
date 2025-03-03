public class PartitionArrayAccordingToGivenPivot {
    public int[] pivotArray(int[] nums, int pivot) {
        ArrayList<Integer> less = new ArrayList<>(),equal = new ArrayList<>(),more = new ArrayList<>();
        for (int i:nums){
            if (i<pivot){
                less.add(i);
            }
            else if(i>pivot){
                more.add(i);
            }
            else{
                equal.add(i);
            }
        }
        less.addAll(equal);
        less.addAll(more);
        return less.stream().mapToInt(i -> i).toArray();
    }
}
