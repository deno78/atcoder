import java.util.Scanner;

public class Main_1{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n=Integer.valueOf(sc.next());
		int[] d=new int[n];
		for(int i=0;i<n;i++){
			d[i]=Integer.valueOf(sc.next());
		}
		System.out.println(d);
	}
}
