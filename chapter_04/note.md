# Function, Scoping, and Abstraction

## 关键字 keys

- Turing Complete
- lacks general utility
- linguistic features
----

- parentheses
- formal parameters
- actual parameters (arguments)
- function call (function invocation)
- bound
- lambda abstraction
- positional arguments
- keyword arguments
    + default parameters value
-----

- scoping
    + name space
    + scope
- local variable
- symbol table
- stack frame
- static or lexical scoping
- poped
- pushed
----

- Specification
    + Docstring
    + Assumptions
    + Guarantees
- triple quotation
----

- Recursion
    + base case
    + recursive case (inductive case)
- Fibonacci numbers
-----

- Palindromes
    + helper function
    + divide-and-conquer
    + short-circuit-evaluation
        * conjunct
        * disjuncts
-----

- file
    - file handle
    - escape character
    - reading
    - appending

## 单词 words

- referred to
- equivalent 
- variant
- at first glance
- clash
- get burned
- cumbersone
- nevertheless
- trepidation
- initialize
- by way of analogy


## 函数的参数 默认参数 可变问题 mutual

当函数被调用时，形式参数被绑定到实际参数上。 

默认参数是在定义时求值，还是调用时？

#### 陷阱 下一章会解决这个问题 基础面试题

```python
def append_a(l=[]):
    l.append("a")    
    return l
```

## return

`return` 可以不跟表达式使用， 返回`None`


## lambda abstraction

参数，操作不是具体的Object
可以操作不具体的Object

## 作用域 scoping

静态作用域，仅看程序就可以知道， 还有动态作用域吗？

#### 注意

在一个作用域里没有定义的变量，解释器会在其上一个作用域中寻找定义。

如果在一个作用域里变量的定义出现在使用之后，就会产生一个错误。

同一个作用域里只要出现变量的定义，解释器就不会去其他作用域里寻找定义。

Python是怎么运行的啊？

1. 编译成字节码
2. 虚拟机运行

## Specification ??约定 规范 标准

specification 是函数使用者与函数编写者之间的约定，在什么条件下，产出什么结果。
 
包含：

- Assumptions 函数调用时必须满足的条件，参数的限制
- Guarantees 函数必须实现的目标


## Function

- 解耦（Decomposition） 把任务分解成模块，方便复用
- 抽象 隐藏细节。 寻找对抽象建立者和潜在使用者都相关的概念。抽象的本质是保留与情景相关的信息， 滤掉无关的。

>The essence of abstraction is preserving
information that is relevant in a given context, and forgetting information that is irrelevant in that context. The key to using abstraction effectively in programming is finding a notion of relevance that is appropriate for both the builder of an abstraction and the potential clients of the abstraction. That is the true art of programming.
Abstraction is all about forgetting.

>Abstraction is a many-to-one process.

## 分治

- divide-and-conquer principle（子问题更易解决，子问题答案的组合就是原问题的答案）
- divide-and-conquer algorithms（动态规划？？）

## 全局变量 Global Variables


不使用全局变量会使程序更易阅读、测试、调试。

函数仅仅通过参数与返回值与外部环境交换信息。


## short-circuit evaluation 短路求值？？

减少不必要的计算。


#### two Boolean-valued expression

- conjunct ` x > 1 and r < 0`
- disjuncts ` x > 1 or r< 0 `