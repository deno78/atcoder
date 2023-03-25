import java.util.*;

public class Main_ABC160_B{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x=Integer.valueOf(sc.next());
        int[] happies= new int[]{1000,5};
        int[] prices=new int[]{500,5};
        int happy=0;
        for(int i=0;i<happies.length;i++){
            int sz=(int) x/prices[i];
            x-=sz*prices[i];
            happy+=sz*happies[i];
        }
        System.out.println(happy);
    }
}