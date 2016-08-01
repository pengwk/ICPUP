# classes and object-oriented programming

## 再次看

### words

- inheritance
- override
- class variable
- convenient
- hierarchy
- mechanism
- instance
- appropriate
- data attribute
- object-oriented programming
- interface
- abstraction barrier
- leg up
- meltdown
- beasts
- mortgages
- at first glance
- abstract class
- generator
- weak static semantic check
- moot
- exploits 

### sentence

> Abstract data types allow us to incorporate this kind of organization into the design of programs. 

> When we think about the world, we rely on abstractions.

> 

### 面向对象的两个核心概念

- encapsulation 
- information hiding


encapsulation: 封装 方法与数据的结合体

information hiding:  信息隐藏 modularity的关键  使用者不关心内部实现，实现的人可以任意更改实现，而不必担心外部调用失败。

数据只应该通过类提供的接口来操作，方便更改实现。

#### weak static semantic checking 大致是什么？

检测某些修改是否会导致错误。 动态修改变量类型，引起某些调用失败。

### representation-independence

> The representation invariant defines which values of the data attributes
> correspond to valid representations of class instances.
> 
> Data abstraction achieves representation-independence.
> 

数据属性的值有效的表示了、代表了类型的实例。

类中的哪个值，是这个类抽象的数据。这个数据定义了这个类，这个类就是为了这个数据而存在的。


### 接口 interface

ADT的方法规范定义了ADT与其余程序的接口，接口提供了一个抽象屏障(abstract barrier)，把外部程序与数据结构、算法、提供类抽象的代码隔离开。

编程是在不断改变中管理复杂度。  有两种机制可以用来达到这个目标：

- 抽象 decomposition
- 解耦 abstraction

解耦创建了程序的骨架，抽象隐藏了细节。为什么？

> Programming is about managing complexity in a way that facilitates change. There are two powerful mechanisms available for accomplishing this: decomposition and abstraction. Decomposition creates structure in a program, and abstraction suppresses detail. The key is to suppress the appropriate. Classes and Object-Oriented Programming
details. This is where data abstraction hits the mark. One can create domainspecific types that provide a convenient abstraction. Ideally, these types capture concepts that will be relevant over the lifetime of a program.
If one starts the
programming process by devising types that will be relevant months and even decades later, one has a great leg up in maintaining that software.

### Generator

`yield` 

不能直接访问数据结构，导致效率低下。 引入额外的方法调用（这个怎么衡量，时间？？）

方法返回一个复制的内部数据给外部，浪费资源。允许外部直接访问，违反隐藏信息的原则。

一次访问，返回一个。 调用一次`.getStudents()`究竟会得到什么东西？ 返回生成器？

```python
def getStudents(self):
    """Return the students in the grade book one at a time"""
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s
```

```python
for s in book.getStudents():
    print s
```


### 文档

docstring里面的文档是给调用者看的，修改代码本身的文档应该写在哪里呢？

注释里面？？

### 代码重用

代码重用不仅能减少开发时间，而且还能增加软件的可靠度。

### 替换原则 The Substitution Principle

保证父类的方法可以在子类上完美调用，子类方法在父类上不作要求。 

## 回想

面向对象编程

- 封装 enclapuse
- 抽象 abstract

封装是为了解耦，模块化设计；抽象是为了隐藏信息。

继承 inherience

subclass superclass 

type 创建一个类就多了一个类型

ADT Abstract Data Type 

数据和方法的结合体

----
操作符重载 overload

特殊方法 Python protocol

`__lt__` less than `<` 

当操作符左右两边的 相应特殊方法不一致时，以左边的为准 使用左边定义的方法判定

实现一个特殊方法后，其他调用这个特殊方法的函数也可以使用，比如：实现`__lt__`后就可以使用`sort
`方法

print 调用的是`__str__`特殊方法， 如果没有实现就会显示object的id

这种用协议的方法真的很兴奋，语言本身带有常用的关键字，实现特殊方法即可使用，是多态（polymorphic）吗？

----
贷款的多样性 利率

- 先少后多，年轻投资，老了回报更高
- 固定利率
- point 是什么？
----



### 疑问

- `super`可以在任何地方调用吗？
- 新式类 与 老式类有什么区别？
- MRO的顺序是什么？ `Method Resolution Order`
- 静态方法 `staticmethod`
- 类方法 `classmethod`
- ADT C语言里面也有讲，什么区别？
- 面向过程又是什么鬼？
-  