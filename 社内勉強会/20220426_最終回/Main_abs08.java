import java.util.*;

public class Main_abs08{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        ArrayList<Integer> alist = new ArrayList<Integer>();
        for(int i=0;i<n;i++){
            alist.add(Integer.valueOf(sc.next()));
        }
        Set<Integer> aset = new HashSet<Integer>();
        for(Integer a : alist){
            aset.add(a);
        }
        System.out.println(aset.size());
    }
}