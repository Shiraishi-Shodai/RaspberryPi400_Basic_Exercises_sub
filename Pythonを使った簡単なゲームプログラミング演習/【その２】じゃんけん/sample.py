import random

# グー, チョキ, パー以外の値が入力された時にエラーを出す例外クラス
class NotInZyanken(Exception):
    pass

# 勝敗を判定する関数
def judge(you, computer) -> str:
    if you == computer:
        return "あいこ"
    elif win_pattern.index(you) == zyanken.index(computer):
        return "勝ち"
    else:
        return "負け"

def main(): 
    ans = "あいこ"
    while ans == "あいこ":
        try:
            you = input("グー, チョキ, パー  の内、どれかを入力してください: ")
            
            if you not in zyanken:
                raise NotInZyanken("グー, チョキ, パー以外の値が入力されました。もう一度実行してください\n")
            else:
                computer = random.choice(zyanken)
                ans = judge(you, computer)
                print(f"あなた: {you}, コンピュータ: {computer}\n結果: {ans}")
        except NotInZyanken as e:
            print(e)

zyanken = ["グー", "チョキ", "パー"]
win_pattern = ["パー", "グー", "チョキ"] #勝ちパターン

if __name__ == "__main__":
        main()
   