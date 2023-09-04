import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int[] g1={1,3,5,7,8,10,12};
        int[] g2={4,6,9,11};
        int[] g3={2};
        boolean xa=false;
        boolean ya=false;
        for(int i:g1){
            if(x==i){xa=true;}
            if(y==i){ya=true;}
        }
        boolean xb=false;
        boolean yb=false;
        for(int i:g2){
            if(x==i){xb=true;}
            if(y==i){yb=true;}
        }

        boolean xc=false;
        boolean yc=false;
        for(int i:g3){
            if(x==i){xc=true;}
            if(y==i){yc=true;}
        }
        if(xa&&ya){System.out.println("Yes");}
        else if(xb&&yb){System.out.println("Yes");}
        else if(xc&&yc){System.out.println("Yes");}
        else{System.out.println("No");
        }
    }
}