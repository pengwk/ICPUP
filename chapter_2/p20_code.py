#!/usr/bin/env
#_*_ coding: utf-8 _*_


times = 10
before = 0
while times:
    now = int(raw_input("Please input a integer: "))
    if before < now and now % 2 != 0:
        before, now = now, before
    times -= 1
if before % 2 == 0:
    print "No odd!"
else:
    print before
