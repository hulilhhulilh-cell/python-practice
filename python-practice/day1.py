# -*- coding: utf-8 -*-
"""
day1.py —— 第一次独立练习
==========================
目标：从"跟着视频敲"过渡到"自己写出来"

使用方法（重要，请照着做）：
  1. 先运行【示例】部分的代码，看清楚输出（PyCharm 里右键 → Run 'day1'）
  2. 然后逐个做下面的【练习】
  3. 每个练习写完就运行一次，看结果对不对
  4. 全部做完后 git add / commit / push

核心规则：
  ■ 不许复制粘贴示例代码去改，必须自己敲
  ■ 卡住超过 10 分钟再看【提示】，不要直接找答案
  ■ 报错是正常的，先读懂报错最后一行再改
"""

print("=== 示例：打印乘法表 ===")

for i in range(1, 10):          # i 依次等于 1,2,3...9
    for j in range(1, i + 1):   # j 从 1 到 i（写 i+1 是因为 range 不包含右端）
        print(f"{j}x{i}={i*j}", end="\t")   # end="\t" 表示用制表符代替换行
    print()                     # 一行的内容打完了，换行


print("\n=== 练习 1 ===")
i=0
for j in range(1, 101):
    i+=j
print(f"1 到 100 的和是",i)



print("\n=== 练习 2 ===")
i=0
for j in range(1, 101):
    if(j % 2 == 0):
        i+=j
print(f"1 到 100 的偶数和是：",i)


print("\n=== 练习 3 ===")
def calc_sum(start,end):
    i=0
    for j in range(start,end+1):
        i += j
    return i
print(f"1 到 100 的和是: {calc_sum(1, 10)}")

print("\n=== 练习 4 ===")

scores = [85, 90, 78, 92, 88, 85, 60, 95, 90, 75, 90, 88]
total = 0
for score in scores:
    total += score
a=total/len(scores)
print(f"平均分: ",a)

max_score = scores[0]
for j in scores:
    if j > max_score:
        max_score = j
print(max_score)
min_score = scores[0]
for j in scores:
    if j < min_score:
        min_score = j
print(min_score)
count_dict = {}
for s in scores:
    count_dict[s] = count_dict.get(s, 0) + 1
print(count_dict)


print("\n=== 练习 5（挑战）===")
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    print("*"*i)


# 1. 确认整份文件运行没有报错
# 2. 打开 Git Bash，进入这个文件夹，执行：
#      git add .
#      git commit -m "day1: 循环、条件、函数、列表字典练习"
#      git push
# 3. 然后回来告诉我哪几题做出来了、哪题卡住了
