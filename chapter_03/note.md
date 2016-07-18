## 关键字

- Exhaustive Enumeration
- decrementing function
- terminate
- guess and check
- Approximate solutions
- Bisection Search
- lexicographical order
- significant digit 
- exponent
- float point
- round value
- accumulation
- polynomial
- coefficient
- degree
- root
- successive approximation
- Newton-Raphson method
- round


## 单词

- iteration
- appropritate
- initialization
- indicate
- blush
- instantaneously
- incredibly
- Less commonly
- evalate
- verbose
- equivalent
- epsilon
- Roughly speaking
- fine tune
- exploit
- mercifully
- sneak


## 求根的几种方法

- 穷举法 exhaustive enumeration
- 二分法 bisection search
- 牛顿法 Newton-Raphson method


## 浮点数的储存 10个`0.1`相加不等于`1`

1. 二进制无法在有限的位数内表示部分十进制小数，0.1就是其中之一。
2. 我们看到的`0.1`, 并不是储存在计算机中的真实数据。
3. print 或者 `__str__` 进行了舍入，便于我们阅读（那真的数据怎么看啊？）
4. 在编写数值计算程序时要注意
5. 在比较数值时尽量使用差值的范围，而不是直接使用运算符 e.g., `abs(x-y) < 0.00001`

浮点数的储存在计算机中是以二进制的方式进行的。二进制无法在有限位数的精确的表示部分十进制小数。

## 几个变量之间的关系

- 循环

## 循环和迭代是一个意思吗？

loop iteration