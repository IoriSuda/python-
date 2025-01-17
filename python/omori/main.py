#sys.path -> 実行ファイルやモジュールを検索するpython標準機能。
#これがないと同ディレクトリにないモジュールを読み込んだときにErrorを起こす(ModuleNotFoundError)

#os.getcwd() -> 実行ファイルまでのディレクトリを絶対パスを出力できる

import sys, os
sys.path.append(str(os.getcwd()) + '/character')

#各モジュールをimportする
from sub import Sub
from character.kel_status import Kel
from character.sunny_status import Sunny


def main():

    #classはインスタンス化しないと使えないので各々インスタンス化する
    sub = Sub()
    sunny = Sunny()
    kel = Kel()

    #インスタンス化したオブジェクトのメソッドを使う
    sub.func("omori")
    sunny.sunny()
    kel.kel()


#main ここでようやく処理が開始する
#sys.pathに記述してあるパスのモジュールはここで読み込まれる

if __name__ == "__main__":
    main()