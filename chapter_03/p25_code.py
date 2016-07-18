#!/usr/bin/env 
# _*_ coding:utf-8 _*_

s = '1.23,2.4,3.123'

_sum = 0

for str_num in s.split(","):
    _sum += float(str_num)

print _sum 