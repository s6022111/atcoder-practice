#スペース区切りで整数値を入力
a, b = map(int, input().split())

#a*bの値が奇数(Odd)か偶数(Even)か判定
if (a*b) % 2 == 0:
    print("Even")
else:
    print("Odd")