# Basic Rule
- このリポジトリでは日本語で説明を返すこと

# コンテスト準備（ABC用フォルダ・ひな型作成）
ABC（AtCoder Beginner Contest）のフォルダやひな型作成を依頼された場合は、以下の規約に従って作成すること。

- **作成先フォルダ**: `src/atcoder/ABC<番号>/`（例: `src/atcoder/ABC484/`）
- **ファイル名**: `abc<番号>_<問題小文字>.py`（例: `abc484_a.py`, `abc484_b.py`, `abc484_c.py`）
  - 作成する問題範囲の指定がない場合は A〜C を作成する。
- **使用言語・ひな型**: Python を使用し、以下の構造を基本とする。
  - `sys.stdin.readline().rstrip("\r\n")` を返す `input()` 関数を定義する。
  - `main()` 関数と `if __name__ == "__main__": main()` を用意し、`main()` 内に標準的な入力受け取り例をコメントで記載する。
  - C問題以降（再帰を使う可能性がある問題）には `# sys.setrecursionlimit(10**6)` のコメントを含める。
- **テンプレート例**:
  ```python
  import sys

  # sys.setrecursionlimit(10**6)  # C問題以降など再帰を使う場合


  def input():
      return sys.stdin.readline().rstrip("\r\n")


  def main():
      # n = int(input())
      # a, b = map(int, input().split())
      # s = input()
      # alist = list(map(int, input().split()))
      pass


  if __name__ == "__main__":
      main()
  ```
- **確認**: ファイル作成後は `python -m py_compile` で構文エラーがないことを確認する。
