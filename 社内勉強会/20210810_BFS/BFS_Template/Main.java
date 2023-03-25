import java.util.*;

public class Main {
	public static void main(String[] args) {
		// マップのサイズ
		int r = 5;
		int c = 5;
		// スタート地点
		int sy = 0;
		int sx = 0;

		// スタートから何手かかるか、を記録する歩数マップ。
		int[][] steps = new int[r][c];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				steps[i][j] = -1;
			}
		}
		// スタート地点の歩数を設定。
		steps[sy][sx] = 0;

		// 今いるポジションを記録するキュー
		Queue<List<Integer>> pos = new ArrayDeque<List<Integer>>();
		pos.add(Arrays.asList(sy, sx));

		// 上下左右に動くパターンを先に作っておく
		List<int[]> moves = new ArrayList<int[]>();
		moves.add(new int[] { -1, 0 });
		moves.add(new int[] { 1, 0 });
		moves.add(new int[] { 0, -1 });
		moves.add(new int[] { 0, 1 });

		// 全部の場所を踏むまでループ
		while (pos.size() > 0) {
			// キューから1個取り出す
			List<Integer> yx = pos.remove();
			int y1 = yx.get(0);
			int x1 = yx.get(1);
			int step = steps[y1][x1];
			// その上下左右を調べる
			for (int[] m : moves) {
				int y2 = y1 + m[0];
				int x2 = x1 + m[1];
				// 座標を飛び出していないかチェック
				if (y2 >= 0 && x2 >= 0 && y2 < r && x2 < c) {
					// まだ歩数計測していない
					if (steps[y2][x2] == -1) {
						// 1歩進める
						steps[y2][x2] = step + 1;
						// 次に調べるべき場所として記録しておく
						pos.add(Arrays.asList(y2, x2));

						System.out.println("現在位置：" + y1 + "/" + x1 + "[" + step + "]" + "→移動先：" + y2 + "/" + x2 + "["
								+ (step + 1) + "]");
						for (int i = 0; i < r; i++) {
							for (int j = 0; j < c; j++) {
								System.out.print(String.format("[%d]", steps[i][j]));
							}
							System.out.println("");
						}
						System.out.println("----------------------------");
					}
				}
			}
		}
	}
}
