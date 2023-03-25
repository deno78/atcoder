import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Main_116_c{

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n= Integer.valueOf(sc.next());
		List hlist=new ArrayList();
		int m=0;
		for(int i=0;i<n;i++){
			int h=Integer.valueOf(sc.next());
			hlist.add(h);
			m=Math.max(m,h);
		}
		String[] hmap=new String[m];
		for(int i=0;i<m;i++){
			hmap[i]="";
			for(int j=0;j<n;j++){
				int h=(int) hlist.get(j);
				if(h>i){
					hmap[i]+="1";
				}else{
					hmap[i]+="0";
				}
			}
		}		
		int ans=0;
		for(String line:hmap){
			List[] results=groupby(line);
			for(Object obj : results[0]){
				if(obj.toString().equals("1")){
					ans+=1;
				}
			}
		}
		System.out.println(ans);
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
