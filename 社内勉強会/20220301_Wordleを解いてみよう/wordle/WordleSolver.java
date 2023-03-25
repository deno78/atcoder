/**
 * 最近流行りのwordleを解くアルゴを考えてみよう
 *
 * https://octokatherine.github.io/word-master/
 *
 */
import java.util.*;
import java.io.*;

public class WordleSolver{

	public static void main(String[] args){
		int WORD_LENGTH=5;	// 推理する文字列の長さ
		try{
			// 単語リスト
			List<String> words=new ArrayList<String>();

			// 辞書ファイルから単語を読み込む。
			String dicPath="dic.txt";
			BufferedReader reader = new BufferedReader(new FileReader(dicPath));
			String line = reader.readLine();
			while(line != null){
				if(line.length()==WORD_LENGTH){
					words.add(line);
				}
				line = reader.readLine();
			}

			// 条件ファイルを読み込んで条件を絞り込む
			String collect = "";	// 合っている文字
			String miss    = "";	// 含まれない文字
			List<String> wrong   = new ArrayList<String>();	// 含まれているが文字位置が異なる
			String inputPath="input.txt";
			reader = new BufferedReader(new FileReader(inputPath));
			line = reader.readLine();
			int lineCount=0;
			while( line != null){
				if(lineCount==0){
					collect=line;
				}else if(lineCount==1){
					miss=line;
				}else{
					wrong.add(line);
				}
				line = reader.readLine();
				lineCount++;
			}

			// 候補を表示する
			List<String> ans=new ArrayList<String>();
			for(String word : words){
				boolean ok=true; // 条件を満たすか

				// 1文字づつ合っている文字列と照合
				for(int j=0;j<WORD_LENGTH;j++){
					if(collect.charAt(j) !='-' && word.charAt(j)!=collect.charAt(j)){
						ok=false;
					}
				}
				// 1文字づつ含まれているが文字位置が異なる文字列と照合
				for(String w : wrong){
					for(int j=0;j<WORD_LENGTH;j++){
						if(w.charAt(j)!='-'){
							if(word.charAt(j)==w.charAt(j)){
								ok=false;
							}
							if(!word.contains(w.substring(j,j+1))){
								ok=false;
							}
						}
					}
				}
				// 含まれない文字のチェック
				for(int j=0;j<miss.length();j++){
					if(word.contains(miss.substring(j,j+1))){
						ok=false;
					}
				}

				// 条件に合致していれば候補に追加
				if(ok){
					ans.add(word);
				}
			}
			// 候補先頭10件を表示する
			for(int i=0;i<10;i++){
				if(i>=ans.size()){break;}
				System.out.println(ans.get(i));
			}

		}catch(Throwable e){
			e.printStackTrace();
		}
	}
}
