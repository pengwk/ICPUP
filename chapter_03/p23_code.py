#!/usr/bin/env
# _*_ coding:utf-8 _*_

espilon = 0.001

_input = int(raw_input("Please input a integer: "))

root_times = _input
pwr_times = 6

root = 0

while root_times:
    if abs(root**1 - _input) <= espilon:
        print "root:{} pwr:{}".format(root, 1)
        break
    elif abs(root**2 - _input) <= espilon:
        print "root:{} pwr:{}".format(root, 2)
        break
    elif abs(root**3 - _input) <= espilon:
        print "root:{} pwr:{}".format(root, 3)
        break
    elif abs(root**4 - _input) <= espilon:
        print "root:{} pwr:{}".format(root, 4)
        break
    elif abs(root**5 - _input) <= espilon:
        print "root:{} pwr:{}".format(root, 5)
        break

    root += 1
    root_times -= 1

    if root_times == 0:
        print "No such pair!"
