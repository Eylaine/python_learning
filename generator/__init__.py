def container(start, end):
    while start < end:
        yield start
        start += 1


c = container(0, 5)
# 输出类型
print(type(c))
# 输出生成器下一个元素0
print(next(c))
# 遍历生成器下一个元素1，但是此时没有输出
next(c)
# 开始遍历生成器剩余的元素，从2开始
for i in c:
    print(i)
