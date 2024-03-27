import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        int x=0;
        int y=0;
        String abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        List<List<String>> map =new ArrayList<List<String>>();
        String ans = "";
        for(int i=0;i<h;i++){
            map.add(new ArrayList<String>());
            for(int j=0;j<w;j++){
                String s = sc.next();
                if(s.equals("snuke")){
                    ans= Character.toString(abc.charAt(j))+Integer.toString(i+1);
                }
            }
        }
        System.out.println(ans);
    }
}