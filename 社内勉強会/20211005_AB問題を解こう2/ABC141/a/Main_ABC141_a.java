import java.util.*;

public class Main_ABC141_a {
    public static void main(String[] args) {
        String[] w = new String[] { "Sunny", "Cloudy", "Rainy" };
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for(int i=0;i<w.length;i++){
            if(w[i].equals(s)){
                System.out.println(w[(i+1)%3]);
                System.exit(0);
            }
        }
    }
}
