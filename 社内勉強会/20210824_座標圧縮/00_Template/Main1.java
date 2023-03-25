import java.util.*;

public class Main1 {
    public static void main(String[] args) {
        List<Integer> alist = Arrays.asList(128,16,2,256,32,4,64,8);

        // �����X�g���d���r�����ă\�[�g�������X�g�����
        List<Integer> vlist = new ArrayList<Integer>(new HashSet<Integer>(alist));
        Collections.sort(vlist);

        // �\�[�g�ς݁��d���r���������X�g�ɏ��ʂ�t���Ēl�����ʂ̘A�z�z��Ɋi�[
        Map<Integer, Integer> amap = new HashMap<Integer, Integer>();
        for (int i = 0; i < vlist.size(); i++) {
            Integer v = (Integer) vlist.get(i);
            amap.put(v, i);
        }

        // �l�����ʂ̘A�z�z��𒲂ׂȂ���\�����Ă���
        for (Integer a : alist) {
            System.out.println(String.format("[%d] : %d",amap.get(a),a));
        }
    }
}
