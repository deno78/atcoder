import java.util.*;

public class Main_abs07{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.valueOf(sc.next());
        ArrayList<Integer> alist = new ArrayList<Integer>();
        for(int i=0;i<n;i++){
            alist.add(Integer.valueOf(sc.next()));
        }
    	Collections.sort(alist,new java.util.Comparator<Integer>(){
            @Override
            public int compare(Integer i1,Integer i2) {
            	return i2 - i1;
            }
        });
        int a=0;
        int b=0;
        boolean isA=true;
        while(alist.size()>0){
            if(isA){
                a+=alist.remove(0);
            }else{
                b+=alist.remove(0);
            }
            isA=!isA;
        }
        System.out.println(a-b);
    }
}