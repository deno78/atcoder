class Main {
    public static void main(String[] args){
        String s = new java.util.Scanner(System.in).next();
        System.out.println(
            s.endsWith("s")?s+"es":s+"s"
        );
    }
    
}
