import java.util.Scanner;

public class abc069_a {

  public static void main(String[] args) {

    // TODO edit this code, this code is for
    // https://atcoder.jp/contests/practice/tasks/practice_1

    // param
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.next());
    int m = Integer.parseInt(sc.next());
    sc.close();

    // resolve
    int ans = (n-1)*(m-1);

    // answer
    System.out.println(ans);
  }

}