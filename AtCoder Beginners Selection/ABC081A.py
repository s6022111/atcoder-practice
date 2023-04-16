#スペースなしの整数値を入力
num = int(input())

#整数値を1文字ずつ分割してリスト作成
b = [int(a) for a in str(num)]

#リスト内の"1"をカウントして出力
print(b.count(1))