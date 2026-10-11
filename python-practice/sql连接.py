# -*- coding: utf-8 -*-
"""
connect_mysql.py —— 用 Python 连接 MySQL，读取 school 库的数据
==============================================================
这是你第一次把 Python 和数据库连起来。

运行前提：
  1. MySQL 服务正在运行（MySQL80 服务）
  2. PyCharm Terminal 里装过 pymysql：
     python -m pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
  3. school 库已建好（school_建库脚本.sql 执行过）

注意：密码写在代码里只适合本机练习。正式项目要用配置文件或环境变量。
"""

import pymysql

# ---------------------------------------------------------------
# 第 1 步：建立连接（这是"打开数据库的门"）
# ---------------------------------------------------------------
conn = pymysql.connect(
    host='localhost',        # 本机
    port=3306,               # MySQL 默认端口
    user='root',             # 用户名
    password='123456',     # ← 你的 root 密码
    database='school',       # 要操作的库
    charset='utf8mb4'        # 字符集，不加中文会乱码
)

print("连接成功！")

# ---------------------------------------------------------------
# 第 2 步：创建游标（cursor 是"执行 SQL 的手"）
# ---------------------------------------------------------------
cursor = conn.cursor()

# ---------------------------------------------------------------
# 第 3 步：执行 SQL
# ---------------------------------------------------------------
sql = """
SELECT c.name AS class_name, AVG(sc.score) AS avg_score
FROM students s
JOIN classes c ON s.class_id = c.id
JOIN scores  sc ON s.id = sc.student_id
GROUP BY c.name
"""

cursor.execute(sql)          # 执行
results = cursor.fetchall()  # 取回全部结果

# ---------------------------------------------------------------
# 第 4 步：处理结果
# ---------------------------------------------------------------
print(f"\n查到了 {len(results)} 行数据：")
print("-" * 40)

for row in results:
    class_name = row[0]
    avg_score  = row[1]
    print(f"{class_name}  平均分：{avg_score:.2f}")
# ---------------------------------------------------------------
# 第 5 步：关闭连接（好习惯，别漏）
# ---------------------------------------------------------------
cursor.close()
conn.close()
print("-" * 40)
print("连接已关闭")