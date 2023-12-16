import java.util.*;

public class Main{
    public static void main(String[] args){
        String s = new Scanner(System.in).next();
        for(int i=0;i<3;i++){
            if(s.charAt(i)==s.charAt(i+1)){
                System.out.println("Bad");
                System.exit(0);
            }
        }
        System.out.println("Good");
    }
}