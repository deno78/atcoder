import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n=Integer.valueOf(sc.next());
		int[] d=new int[n];
		for(int i=0;i<n;i++){
			d[i]=Integer.valueOf(sc.next());
		}
		int ans=0;
		for(int i=0;i<n-1;i++){
			for(int j=i+1;j<n;j++){
				ans+=d[i]*d[j];
			}
		}
		System.out.println(ans);
	}
}
