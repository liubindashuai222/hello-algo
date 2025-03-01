'''
File: time_complexity.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
'''

import sys, os.path as osp
sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from include import *

""" 常数阶 """
def constant(n):
    count = 0
    size = 100000
    for _ in range(size):
        count += 1
    return count

""" 线性阶 """
def linear(n):
    count = 0
    for _ in range(n):
        count += 1
    return count

""" 线性阶（遍历数组）"""
def array_traversal(nums):
    count = 0
    # 循环次数与数组长度成正比
    for num in nums:
        count += 1
    return count

""" 平方阶 """
def quadratic(n):
    count = 0
    # 循环次数与数组长度成平方关系
    for i in range(n):
        for j in range(n):
            count += 1
    return count

""" 平方阶（冒泡排序）"""
def bubble_sort(nums):
    count = 0  # 计数器
    # 外循环：待排序元素数量为 n-1, n-2, ..., 1
    for i in range(len(nums) - 1, 0, -1):
        # 内循环：冒泡操作
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # 交换 nums[j] 与 nums[j + 1]
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3  # 元素交换包含 3 个单元操作
    return count

""" 指数阶（循环实现）"""
def exponential(n):
    count, base = 0, 1
    # cell 每轮一分为二，形成数列 1, 2, 4, 8, ..., 2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 + .. + 2^(n-1) = 2^n - 1
    return count

""" 指数阶（递归实现）"""
def exp_recur(n):
    if n == 1: return 1
    return exp_recur(n - 1) + exp_recur(n - 1) + 1

""" 对数阶（循环实现）"""
def logarithmic(n):
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

""" 对数阶（递归实现）"""
def log_recur(n):
    if n <= 1: return 0
    return log_recur(n / 2) + 1

""" 线性对数阶 """
def linear_log_recur(n):
    if n <= 1: return 1
    count = linear_log_recur(n // 2) + \
            linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count

""" 阶乘阶（递归实现）"""
def factorial_recur(n):
    if n == 0: return 1
    count = 0
    # 从 1 个分裂出 n 个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count


""" Driver Code """
if __name__ == "__main__":
    # 可以修改 n 运行，体会一下各种复杂度的操作数量变化趋势
    n = 8
    print("输入数据大小 n =", n)

    count = constant(n)
    print("常数阶的计算操作数量 =", count)

    count = linear(n)
    print("线性阶的计算操作数量 =", count)
    count = array_traversal([0] * n)
    print("线性阶（遍历数组）的计算操作数量 =", count)

    count = quadratic(n)
    print("平方阶的计算操作数量 =", count)
    nums = [i for i in range(n, 0, -1)]  # [n,n-1,...,2,1]
    count = bubble_sort(nums)
    print("平方阶（冒泡排序）的计算操作数量 =", count)

    count = exponential(n)
    print("指数阶（循环实现）的计算操作数量 =", count)
    count = exp_recur(n)
    print("指数阶（递归实现）的计算操作数量 =", count)

    count = logarithmic(n)
    print("对数阶（循环实现）的计算操作数量 =", count)
    count = log_recur(n)
    print("对数阶（递归实现）的计算操作数量 =", count)

    count = linear_log_recur(n)
    print("线性对数阶（递归实现）的计算操作数量 =", count)

    count = factorial_recur(n)
    print("阶乘阶（递归实现）的计算操作数量 =", count)
