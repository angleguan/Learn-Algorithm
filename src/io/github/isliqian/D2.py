print("输入三个数，由小到大进行输出")
a, b, c = input("输入a,b,c(空格分隔)").split()
a, b, c = int(a), int(b), int(c)
maxNo = max(a, b, c)
minNo = min(a, b, c)
print(maxNo, a+b+c-maxNo-minNo, minNo)