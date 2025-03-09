def char_value(name):
    return sum(ord(char) for char in name)

# 輸入玩家名字
name1 = input("Player 1's name ：")
name2 = input("Player 2's name ：")

# 計算名字的 ASCII 總和
score1 = char_value(name1)
score2 = char_value(name2)

for i in range(len(name1)):
    print(f"{name1[i]} = {ord(name1[i])}",end=" ")
print(f" => {score1}")

for i in range(len(name2)):
    print(f"{name2[i]} = {ord(name2[i])}",end=" ")
print(f" => {score2}")

# 判斷誰先開始
if score1 > score2:
    print(f"{name1} Starts first！")
elif score2 > score1:
    print(f"{name2} Starts first！")
else:
    print("Tie！")
