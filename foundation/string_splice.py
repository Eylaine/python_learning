
# 字符串拼接

str_a = "Hello"
str_b = " World"    # 前面有个空格

# 直接两个字符串相加
str_c = str_a + str_b
print(str_c)    # Hello World

# format
str_d = "{}{}".format(str_a, str_b)
print(str_d)    # Hello World

# f
str_e = f"{str_a}{str_b}"
print(str_e)    # Hello World

# join
list_a = list()
list_a.append(str_a)
list_a.append(str_b)
str_f = "".join(list_a)
print(str_f)    # Hello World

# 注意join的使用，有坑
print(" ".join(str_a))  # H e l l o
print(" ".join(str_b))
#   W o r l d(注意W之前有两个空格)

# %
str_g = "%s%s" % (str_a, str_b)
print(str_g)    # Hello World
