# 整数値を入力
a = int(input())

# スペース区切りで整数値を入力
b, c = map(int, input().split())

# 文字列を入力
s = input()

# 出力
print("{} {}".format(a+b+c, s))