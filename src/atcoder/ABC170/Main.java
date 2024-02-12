import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        for(int i=1;i<6;i++){
            if(i!=sc.nextInt()){
                System.out.println(i);
                System.exit(0);
            }
        }
    }
}