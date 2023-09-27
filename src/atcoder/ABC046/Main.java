import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Set ans = new HashSet();
        for(int i=0;i<3;i++){
            ans.add(sc.nextInt());
        }
        System.out.println(ans.size());
    }
}
