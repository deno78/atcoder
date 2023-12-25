import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        String[] l = new String[]{"Sunny", "Cloudy", "Rainy"};
        for(int i=0;i<l.length;i++){
            if(l[i].equals(s)){
                System.out.println(l[(i+1)%3]);
                System.exit(0);
            }
        }
    }
}