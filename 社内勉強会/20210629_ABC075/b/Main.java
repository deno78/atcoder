import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = Integer.valueOf(sc.next());
        int w = Integer.valueOf(sc.next());
        String[][] map = new String[h][w];
        for (int i = 0; i < h; i++) {
            String line = sc.next();
            for (int j = 0; j < w; j++) {
                map[i][j] = Character.toString(line.charAt(j));
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (!map[i][j].equals("#")) {
                    int count = 0;
                    for (int k = 0; k < 9; k++) {
                        int x = k % 3 - 1 + i;
                        int y = ((int) k / 3) - 1 + j;
                        if (x >= 0 && y >= 0 && x < h && y < w && map[x][y].equals("#")) {
                            count++;
                        }
                    }
                    map[i][j] = Integer.toString(count);
                }
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                System.out.print(map[i][j]);
            }
            System.out.println("");
        }
    }
}
