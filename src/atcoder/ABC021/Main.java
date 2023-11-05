import java.util.*;

public class Main{
  public static void main(String[] args){
    int[] a=new int[]{8,4,2,1};
    List ans=new ArrayList();
    int n = new Scanner(System.in).nextInt();
    for(int i=0;i<a.length;i++){
      while(true){
        if(n>=a[i]){
          ans.add(a[i]);
          n-=a[i];
        }else{
          break;
        }
      }
    }
    System.out.println(ans.size());
    for(int i=0;i<ans.size();i++){
      System.out.println(ans.get(i).toString());
    }
  }
}