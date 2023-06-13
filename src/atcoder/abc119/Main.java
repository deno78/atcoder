import java.util.*;
import java.text.*;

public class Main{
    public static void main(String[] args){
        try{
        Date d = new SimpleDateFormat("yyyy/MM/dd").parse(new Scanner(System.in).next());
        Calendar c = Calendar.getInstance();
        c.setTimeZone(TimeZone.getDefault());
        c.set(2019,3,30,0,0,0);
        System.out.println(d.compareTo(c.getTime())<=0?"Heisei":"TBD");
        }catch(Throwable e){            
        }
    }
}