import java.util.*;

public class Main {
    static int[] parents;
    static void init(int size){
        parents=new int[size];
        for(int i=0;i<size;i++){
            parents[i]=i;
        }
    }
    static int find(int a){
        if(parents[a]==a){
            return a;
        }else{
            int p = find(parents[a]);
            parents[a]=p; // 経路更新→圧縮
            return p;
        }
    }
    static void unite(int a,int b){
        int pa=find(a);
        int pb=find(b);
        if(pa<pb){
            parents[pb]=pa;
        }else{
            parents[pa]=pb;
        }
    }
    static int getRootCount(){
        Set s = new HashSet();
        for(int i=0;i<parents.length;i++){
            s.add(parents[i]);
        }
        return s.size();
    }
    static void print(){
        for(int i=0;i<parents.length;i++){
            System.out.print(parents[i]);
            System.out.print(",");
        }
        System.out.println("");
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=Integer.valueOf(sc.next());
        int m=Integer.valueOf(sc.next());
        int[][] routes=new int[m][2];
        for(int i=0;i<m;i++){
            int a=Integer.valueOf(sc.next())-1;
            int b=Integer.valueOf(sc.next())-1;
            routes[i]=new int[]{a,b};
        }
        int count=0;
        for(int i=0;i<m;i++){
            init(n);
            for(int j=0;j<m;j++){
                if(i!=j){
                    int[] ab=routes[j];
                    unite(ab[0],ab[1]);
                }
            }
            for(int j=0;j<n;j++){
                find(j);
            }
            if(getRootCount()!=1){
                count++;
            }
        }
        System.out.println(count);
    }
}
