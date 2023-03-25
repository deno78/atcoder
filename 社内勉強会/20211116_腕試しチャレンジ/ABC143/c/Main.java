import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n=Integer.valueOf(sc.next());
		String s=sc.next();
		int ans=1;
		char[] s2=s.toCharArray();
		char c=s2[0];
		for(int i=1;i<n;i++){
			char c2=s2[i];
			if(c!=c2){
				c=c2;
				ans++;
			}
		}
		System.out.println(ans);
	}
}
