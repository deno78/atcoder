import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<Integer> a = new ArrayList<Integer>();
        a.add(sc.nextInt());
        a.add(sc.nextInt());
        a.add(sc.nextInt());
        List<Integer> a2 = new ArrayList<Integer>(a);
        Collections.sort(a2);
        Collections.reverse(a2);
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                 if(a.get(i)==a2.get(j)){
                    System.out.println(j+1);
                    break;
                }
            }
        }
    }
}