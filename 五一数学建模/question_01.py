import math

arm = [44, 20, 16, 28, 64, 24, 20, 28]  # 机械臂
container = [11, 5, 4, 7, 16, 6, 5, 7]  # 容器艇
initial_arm = 50  # 初始机械臂数量
initial_container = 13  # 初始容器艇数量
weeks_arm = []  # 存储需要购买机械臂的周数
weeks_container = []  # 存储需要购买容器艇的周数
maintenance_costs_arm, maintenance_costs_container = 0, 0
num1 = 0
num2 = 0
add_arm = []  # 新增的机械臂数量
add_container = []  # 新增的容器艇数量
total_cost = 0  # 总成本

for i in range(len(arm)):
    if (i + 1 < len(arm)):
        s = arm[i] + arm[i + 1]
        if (s > initial_arm):  # 机械臂
            num1 = s - initial_arm
            add_arm.append(num1)
            initial_arm = s
            weeks_arm.append(i)

        if (container[i] > initial_container):  # 容器艇
            num2 = container[i] - initial_container
            add_container.append(num2)
            initial_container = container[i]
            weeks_container.append(i - 1)
    maintenance_costs_arm = maintenance_costs_arm + (initial_arm - arm[i]) * 5
    maintenance_costs_container = maintenance_costs_container + (initial_container - container[i]) * 10  # 容器艇的保养费用
maintenance_costs_arm = maintenance_costs_arm - sum(add_arm) * 5  # 机械臂的保养费用

for i in range(len(weeks_arm)):
    print("第", weeks_arm[i] + 1, "周购买的机械臂数量为：", add_arm[i])
for i in range(len(weeks_container)):
    print("第", weeks_container[i] + 1, "周购买的容器艇数量为：", add_container[i])

expenses_arm = (initial_arm - 50) * 100  # 机械臂的购买费用
expenses_container = (initial_container - 13) * 200  # 容器艇的购买费用
training_expenses_arm = (initial_arm - 50) * 10 + math.ceil(sum(add_arm) / 10) * 5  # 训练机械臂的费用

total_cost = expenses_arm + expenses_container + training_expenses_arm + maintenance_costs_arm + maintenance_costs_container
print("总成本：", total_cost, "元")

