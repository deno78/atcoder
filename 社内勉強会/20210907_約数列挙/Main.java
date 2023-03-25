import java.util.*;

public class Main{
    static List<Integer> make_divisor(int n){
        ArrayList<Integer> low_divisors=new ArrayList<Integer>();
        ArrayList<Integer> upper_divisors=new ArrayList<Integer>();
        int i=1;
        while(i*i<n){
            if(n%i==0){
                low_divisors.add(i);
                upper_divisors.add(n/i);
            }
            i++;
        }
        low_divisors.addAll(upper_divisors);
        return low_divisors;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        for(int d: make_divisor(n)){
            System.out.println(d);
        }
    }

}