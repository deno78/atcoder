import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int m = Integer.valueOf(sc.next());
        // M種類でそれぞれ0件の連想配列を作る。
        Map<Integer,Integer> data=new HashMap<Integer,Integer>();
        for(int i=0;i<m;i++){
            data.put(i,0);
        }
        // 入力値を受け取る
        for(int i=0;i<n;i++){
            int k=Integer.valueOf(sc.next());
            for(int j=0;j<k;j++){
                // a番目の要素への投票をカウントアップ
                int a=Integer.valueOf(sc.next())-1;
                int c=data.get(a);
                data.put(a,c+1);
            }
        }
        int ans=0;
        for(Map.Entry<Integer,Integer> ent:data.entrySet()){
            // 投票数が総人数と同じなら回答に加える
            if(ent.getValue()==n){
                ans++;
            }
        }
        System.out.println(ans);
    }
}
