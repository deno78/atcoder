import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<Integer>();
        for(int i=0;i<3;i++){
            a.add(sc.nextInt());
        }
        Collections.sort(a);
        int ans=0;
        for(int i=1;i<a.size();i++){
            ans+=a.get(i)-a.get(i-1);
        }
        System.out.println(ans);
    }   
}
