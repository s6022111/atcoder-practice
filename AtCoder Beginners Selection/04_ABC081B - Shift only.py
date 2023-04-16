# 整数値を入力
n = int(input())

#スペース区切りで整数値を入力
a = [int(z) for z in input().split()] 
#num = list(map(int, input().split())) でもOKらしい

#要素ごとに偶数か判定して処理を行う
num = []
for i in a:

    #偶数ならば2で割り続けてその回数をカウント
    if i % 2 == 0:
        b = len(bin(i)) - bin(i).rfind("1") - 1
        num.append(b)

    #奇数ならば"0"を出力
    else:
        (print(0))
        exit()

#リストnum内の最小値を出力
print(min(num))