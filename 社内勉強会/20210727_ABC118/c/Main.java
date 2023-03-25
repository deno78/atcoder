import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        List<Long> alist = new ArrayList<Long>();
        for(int i=0;i<n;i++){
            alist.add(Long.valueOf(sc.next()));
        }
        Long ans=alist.get(0);
        for(int i=1;i<alist.size();i++){
            ans=gcd(ans,alist.get(i));
        }
        System.out.println(ans);
    }

    /**
     * ユークリッドの互助法で最大公約数を求める
     * @param a
     * @param b
     * @return
     */
    public static long gcd(long a,long b){
        if(b==0){
            System.out.println("GCD[" + a + "]");
            return a;
        }else{
            System.out.println("GCD["+ a + "/" + b+"] => "+ b + "/" + a%b + "]");
            return gcd(b,a%b);
        }
    }
}
