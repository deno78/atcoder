import java.util.*;


public class Main_ABC161_B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        int m = Integer.valueOf(sc.next());
        int sum=0;
        List<Integer> alist= new ArrayList<Integer>();
        for(int i=0;i<n;i++){
            int a=Integer.valueOf(sc.next());
            alist.add(a);
            sum+=a;
        }
        int over=0;
        int sum_m=(int) sum/4/m;
        if(sum%(4*m)!=0){
            sum_m+=1;
        }
        for(Integer a : alist){
            // System.out.println(a.toString() + "/" + Integer.toString(sum_m));
            if(a>=sum_m){
                over++;
            }
        }
        if(over>=m){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }

    }
    
}
