import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        List<Integer> a = new ArrayList<Integer>();
        for(int i=0;i<5;i++){
            a.add(s.nextInt());
        }
        int k=s.nextInt();
        for(int a1 : a){
            for(int a2:a){
                int d=a1-a2;
                if(a1<a2){
                    d=a2-a1;
                }
                if(d > k){
                    System.out.println(":(");
                    System.exit(0);
                }
            }
        }
        System.out.println("Yay!");
    }
}