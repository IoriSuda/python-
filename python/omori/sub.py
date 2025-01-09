class Sub():
    def __init__(self): #コンストラクタ 書けば最初に勝手に呼び出される。初期化の目的で使う
        print("subの__init__が実行されました")


    def func(self, name):
        self.name = name
        print("subのfuncが実行されました")
        print("{}です" .format(name))