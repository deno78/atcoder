
class Main {
    public static void main(String[] args){
        String s = new java.util.Scanner(System.in).next();
        int ans=0;
        if(s.contains("RRR")){
            ans=3;
        }else if(s.contains("RR")){
            ans=2;
        }else if(s.contains("R")){
            ans=1;
        }
        System.out.println(ans);
    }
}
