public class CountTotalNumberofColoredCells {
    public long coloredCells(int a) {
        long n = a;
        return n*n+(n-1)*(n-1);
    }
    public static void main(String[] args) {
        CountTotalNumberofColoredCells cells = new CountTotalNumberofColoredCells();
        System.out.println(cells.coloredCells(10));
    }
}
