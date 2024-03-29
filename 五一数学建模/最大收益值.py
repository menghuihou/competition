sumx = 0  # 前j周购买的容器艇总和
sumy = 0  # 前i周购买的操作手总和
a, b = 0, 0  # a为购买的容器艇保养费，b为省的钱
c, d = 0, 0  # c为购买的操作手保养费，d为省的钱
container = [11, 5, 4, 7, 16, 6, 5, 7,
        13, 6, 5, 7, 12, 5, 4, 6,
        9, 5, 5, 11, 29, 21, 17, 20,
        27, 13, 9, 10, 16, 6, 5, 7,
        11, 5, 5, 6, 12, 7, 7, 10,
        15, 10, 9, 11, 15, 10, 10, 16,
        26, 21, 23, 36, 50, 45, 45, 49,
        57, 43, 40, 44, 52, 43, 42, 45,
        52, 41, 39, 41, 48, 35, 34, 35,
        42, 34, 36, 43, 55, 48, 54, 65,
        80, 70, 74, 85, 101, 89, 88, 90,
        100, 87, 88, 89, 104, 89, 89, 90,
        106, 96, 94, 99, 109, 99, 96, 102]

arms = []
for i in range(len(container)):
    arms.append(4 * container[i])


weekX = []
weekY = []
priceX = []
priceY = []
# for i in range(0,10):
for j in range(0, 104):  # 1-104周
    sumx += container[j]  # sumx一定>10
    a = a + container[j] * 10 * j  # 容器艇在第一周购买时的保养费
    b = (sumx - 10) * 40 - a  # 省下来的钱
    priceX.append(b)
    weekX.append(sum(priceX))

print(priceX)
#print(weekX)

for i in range(0,104):
    sumy += arms[i]  #sumy>40
    c = c + arms[i] * 5 * i
    d = (sumy - 40) * 20 - c
    priceY.append(d)
    weekY.append(sum(priceY))
print(priceY)
#print(weekY)
