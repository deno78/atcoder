import java.util.*;

public class Main_ABC162_B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
	long n=Long.valueOf(sc.next());
	long sum=0;
	for(long i=1;i<=n;i++){
		if(i%3==0 && i%5==0){
		}else if(i%3==0){
		}else if(i%5==0){
		}else{
			sum+=i;
		}
	}
	System.out.println(sum);
    }
}
