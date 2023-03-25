import java.util.*;

public class Main_ABC036_C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        List<Integer> alist = new ArrayList<Integer>();
        Set<Integer> aset = new HashSet<Integer>();
        for (int i = 0; i < n; i++) {
            int a = Integer.valueOf(sc.next());
            alist.add(a);
            aset.add(a);
        }
        ArrayList<Integer> vlist = new ArrayList<Integer>(aset);
        Collections.sort(vlist);

        Map<Integer, Integer> amap = new HashMap<Integer, Integer>();
        for (int i = 0; i < vlist.size(); i++) {
            Integer v = (Integer) vlist.get(i);
            amap.put(v, i);
        }
        for (Integer a : alist) {
            System.out.println(amap.get(a));
        }
    }
}