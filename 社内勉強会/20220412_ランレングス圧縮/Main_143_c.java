import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main_143_c{

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n=Integer.valueOf(sc.next());
		String s=sc.next();
		List[] results=groupby(s);
		System.out.println(results[0].size());
	}

	public static List[] groupby(String s){
		List keys=new ArrayList();
		List lengths=new ArrayList();
		keys.add(s.charAt(0));
		lengths.add(1);
		for(int i=1;i<s.length();i++){
			char c=s.charAt(i);
			int j=keys.size()-1;
			if(c==(char) keys.get(j)){
				lengths.set(j,((int) lengths.get(j)) +1);
			}else{
				keys.add(c);
				lengths.add(1);
			}
		}
		List[] result = {keys,lengths};
		return result;
	}

}
