import java.util.*;

public class Main_B {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> hlist = new ArrayList<Integer>();
        for(int i=0;i<n;i++){
            hlist.add(sc.nextInt());
        }
        int highest=-1;
        int ans =0;
        for(int h: hlist){
            if(h >= highest){
                highest = h;
                ans++;
            }
        }
        System.out.println(ans);
    }
    
}
