import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<Integer>();
        for(int i=0;i<3;i++){
            a.add(sc.nextInt());
        }
        int ans=301;
        for(int i=0;i<a.size();i++){
            for(int j=0;j<a.size();j++){
                for(int k=0;k<a.size();k++){
                    if(i!=j && j!=k && k!=i){
                        ans=Math.min(ans,
                            Math.abs(a.get(i)-a.get(j))+
                            Math.abs(a.get(j)-a.get(k)));
                    }
                }
            }
        }
        System.out.println(ans);
    }   
}
