## Structured types, mutability, and higher-order functions

### 关键字

- scalar types
- mutable
- tuples
- ordered sequences
- literals
- comma
- parentheses
- concatenated
- indexed
- sliced
- conjunction
- literals of type list?
- mutable
- immutable
- statement
- expression
- object equality
- value equality
- id
- side effect
- aliasing
- cloning
- clause
- first-class objects
- highter-order programming
- hashing
- list comprehension

### 单词

- conjunction
- mechanism
- individual
- bracket
- singleton
- subtle
- cloning
- marvelous
- examples of literals
- prudent


### scalar type

int float 这种不能访问内部结构的类型，就是scalar type。像str可以通过`"mutable"[0:2]`(slicing) 

### 相等 有两种

- value equation
- object equation

操作符，使用的都是value equation。 要比较两个变量表示的是不是同一个object，可以使用函数`id()`

#### atom


### 高阶函数

可以把函数当成参数的函数就是高阶函数（参数里包含函数的函数就是高阶函数）。
图灵等价，函数的存在就是为了抽象，高阶函数就是更高层次的抽象。

### 函数是一类对象

为什么要怎么分？

- 谁是二类(second-class object)?

### 可变和不可变

在Python中一切都是对象，变量是对象的引用，一个对象可以被多个变量引用。

    raw_list = [1, 2, 3]
    new_list = [raw_list, 5, 6, 7]

修改`raw_list`会改变new_list的值，因为raw_list只是对象`[1, 2, 3]`的aliasing。

#### 在迭代时需要注意

不要动态改变迭代的序列。

    _list = [2, 1, 4, 6]
    for x in _list:
        if x in [1, 2, 3]:
            _list.remove(x)
    print _list

    Out[1]: [1, 4, 6]

Python里面使用计数器来判断循环的结束。当动态修改正在循环的列表时，计数器不会同时变化，会导致序列中的某些元素被跳过。

上面代码序列元素`1`直接被跳过。 `2`被删除时序列变为`[1, 4, 6]`，此时计数器为`1` 即`[1, 4, 6][1]`, 元素`1`被跳过。

这种情况可以通过`seq[:]`复制一个新的list来避免，如果list中包含其他可变类型元素，就使用copy模块的`deepcopy`。

#### 函数默认参数 可变还是不可变

在Python 官方FAQ里写到默认参数是可变也有好处，在重复计算时可以当缓存，同一个函数共享一个object（这个好牵强，是不是设计有问题）

##### 函数参数设置

lambda函数的参数要求与普通函数的要求一样吗？

- 关键字参数后面不能是位置参数。`def normal(a, b=3, z):return`

#### side effect

- 不可变对象的内置方法都是没有副作用的。

- `+` 没有副作用，他会返回一个新的值


#### 字典

字典里查找一个值所用的时间并不会随着字典的变大而变大。什么复杂度啊？


### 再谈赋值

    i = 0
    a = [2, 3, 4]
    i, a[i] = 1, 9
    print a

    Out[1]: [2, 9, 4]

Python的求值顺序是从左到右，赋值时是先对等号右边的求值。

所以`i`在`a[i]`之前改变了值。

### list comprehension

subtle是紧凑的意思吗？

这个会降低代码可读性吗？


### statement expression clause keyword operator 是什么关系？

print 是statement

