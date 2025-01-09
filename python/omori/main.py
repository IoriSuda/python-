from sub import Sub
from sunny.sunny_status import Sunny

def main():
    sub = Sub()#インスタンス化しないと使えない
    sunny = Sunny()
    sub.func("omori")
    sunny.sunny()


#main
if __name__ == "__main__":
    main()