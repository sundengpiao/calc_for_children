#!/usr/python/bin
# -*- coding: utf-8 -*-

import sys
import random


#2个加法
def get_2add(sum):
    a = random.randint(0,sum)
    b = sum-a
    return ("%d+%d=" %(a,b)),str(sum)


#两个减法
def get_2sub(sum):
    a = random.randint(0,sum)
    b = sum-a
    return ("%d-%d=" %(sum,a)),str(b)


#3个加法
def get_3add(sum):
    a = random.randint(1,sum)
    if a<sum:
        b = random.randint(1,sum-a)
    else:
        b = 0
    c = sum-a-b
    return ("%d+%d+%d=" %(a,b,c)),str(sum)


#三个减法
def get_3sub(sum):
    a = random.randint(1,sum)
    if a<sum:
        b = random.randint(1,sum-a)
    else:
        b = 0
    c = sum-a-b
    return ("%d-%d-%d=" %(sum,a,b)),str(c)


#前加后减
def get_add_sub(sum):
    #前加
    a = random.randint(0,sum)
    b = sum-a
    #后减
    c = random.randint(0,sum)
    d = sum-c
    return ("%d+%d-%d=" %(a,b,c)),str(d)


#前减后加
def get_sub_add(sum):
    sub = random.randint(0,sum)
    a = random.randint(sub,sum)
    b = a-sub
    c = sum-sub
    return ("%d-%d+%d=" %(a,b,c)),str(sum)


#函数功能：主函数
#函数参数：可执行文件全路径，启动时加入的参数
#函数返回：执行成功返回0，否则返回负值的错误码
if __name__ == "__main__":
    need_continue = "y"
    error = "口算训练启动参数：[max] [count]。其中max为数值上线，如100表示100以内的加减法，如此类推；count表示题目数目。"\
        "不带参数情况下启动时，max是100，count是50，即100以内的50道加减法题目。"
    max = 100
    count = 50
    add2_prob = 4000
    sub2_prob = 7000
    add3_prob = 8000
    sub3_prob = 9000
    addsub_prob = 9500
    subadd_prob = 10000

    #检查参数
    if 2<=len(sys.argv) and ("-h"==str(sys.argv[1]).lower() or "help"==str(sys.argv[1]).lower()):
        print(error)
        sys.exit(0)
    if 2<=len(sys.argv):
        if False == str(sys.argv[1]).isdigit() or 0>=int(sys.argv[1]):
            print(error)
            sys.exit(-1)
        max = int(sys.argv[1])
    if 3<=len(sys.argv):
        if False == str(sys.argv[2]).isdigit() or 0>=int(sys.argv[2]):
            print(error)
            sys.exit(-1)
        count = int(sys.argv[2])
    #开始测试
    while 'y' == need_continue:
        print("\n小朋友，您需要完成%d以内的加减法%d道，让我们开始吧：" %(max, count))
        suc_cnt = 0
        for cur in range(0,count,1):
            cur_opt = random.randint(1,10000)
            cur_sum = random.randint(2,max)
            opt_str = ""
            ret_str = ""
            if cur_opt<=add2_prob:
                opt_str,ret_str = get_2add(cur_sum)
            elif cur_opt>add2_prob and cur_opt<=sub2_prob:
                opt_str,ret_str = get_2sub(cur_sum)
            elif cur_opt>sub2_prob and cur_opt<=add3_prob:
                opt_str,ret_str = get_3add(cur_sum)
            elif cur_opt>add3_prob and cur_opt<=sub3_prob:
                opt_str,ret_str = get_3sub(cur_sum)
            elif cur_opt>sub3_prob and cur_opt<=addsub_prob:
                opt_str,ret_str = get_add_sub(cur_sum)
            else:
                opt_str,ret_str = get_sub_add(cur_sum)
            add = 1
            while True:
                int_str = str( input(("第%d题: %s" %(cur+1, opt_str))) ).strip()
                if int_str == ret_str:
                    suc_cnt = suc_cnt+add
                    print("答对了！")
                    break
                else:
                    add = 0
                    print("答错了，再做一次！")
        if count == suc_cnt:
            print("全做对了呢，真棒！" )
        else:
            print("错了%d道题目，再接再厉哦！" %(count-suc_cnt))
        need_continue = str(input("输入 y或者Y 继续答题；按 Enter 键退出答题...:")).strip()
        need_continue = need_continue.lower()
    sys.exit(0)
            