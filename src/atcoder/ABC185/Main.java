import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] ary=new int[4];
        for(int i=0;i<4;i++){
            ary[i]=sc.nextInt();
        }

        System.out.println(
            Arrays.stream(ary).min().getAsInt()
        );        
    }
    
}
