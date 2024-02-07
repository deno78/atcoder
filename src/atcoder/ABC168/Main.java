import java.util.*;

class Main {
    public static void main(String[] a){
        String s = new Scanner(System.in).next();
        String c = Character.toString(s.charAt(s.length()-1));
        if("3".contains(c)){
            System.out.println("bon");
        }else if("0168".contains(c)){
            System.out.println("pon");
        }else{
            System.out.println("hon");
        }
    }
}