import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    // TODO edit this code, this code is for
    // https://atcoder.jp/contests/practice/tasks/practice_1

    // param
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    sc.close();

    // answer
    System.out.println(s.charAt(0)==s.charAt(2)?"Yes":"No");
  }

}