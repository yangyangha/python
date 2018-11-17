import sys

def test_exception():
    #抛异常就不会继续执行
    # fff = open("ddds")

    try:
        f = open("ttt.txt")
    except IOError:
        print("io exception")
    finally:
        print("finally")

    # ff = open("ddd")

if __name__ == '__main__':
        test_exception()