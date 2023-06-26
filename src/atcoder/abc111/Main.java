import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String n = sc.next();
        for(char c : n.toCharArray()){
            if (c=='9'){
                System.out.print("1");
            }else if (c=='1'){
                System.out.print("9");
            }else{
                System.out.print(c);
            }
        }
        System.out.println("");
    }
}