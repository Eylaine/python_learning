# -*- coding: utf-8 -*-
# Time   : 2019/10/29 2:12 下午
# Author : Eylaine
# File   : demo.py


def func():
    """生成器函数"""
    n = 0
    while True:
        s = yield n
        if s is None:
            break
        n += 1
    return n


def deligate():
    """委派生成器"""
    result = yield from func()
    print("the result is : %s" % result)


def main():
    """调用方"""
    g = deligate()
    print(next(g))
    for i in range(3):
        print(g.send(i))
    # 在这里发送None给生成器，生成器不会产出值而抛出StopIteration异常
    try:
        g.send(None)
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
