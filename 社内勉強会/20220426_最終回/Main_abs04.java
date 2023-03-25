import java.util.*;

public class Main_abs04{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        List<Integer> alist = new ArrayList();
        for(int i=0;i<n;i++){
            alist.add(Integer.valueOf(sc.next()));
        }
        int ans=0;
        while(true){
            for(int i=0;i<n;i++){
                if(alist.get(i)%2==0){
                    alist.set(i,alist.get(i)/2);
                }else{
                    System.out.println(ans);
                    System.exit(0);
                }
            }
            ans++;
        }
    }
}