## 关键字

- versus
- weak static semantic checking
- high reliability constraints
- statement
- Objects
- Type
- Expressions
- Scalar
- operators
- value
- variable
- assignment
- reserved word(or keyword)
- comments
- straight-line program
- Indentation
- nested
- constant time
- conputational complexity
- overload
- type checking
- type conversions(type casts)
- iteration(also called looping)
- hand-simulating
- Flow Chart
- Initializing
- Concatenation

## 单词

- forewarned 
- vehicle
- dribs and drabs
- ulterior purpose
- undergone
- incorporating
- clearly superior
- remainder
- either...or..
- prompt
- supicious
- tally the votes in an election
- intrinsic
- odd
- subtle
- quaint
- depicted
- mechanism



## Python操作符（operator）有哪些？怎么自定义？  

- 算术运算符 `-`、 `+`、 `*`、 `/`、 `//`、 `**` `%` 
- 比较 `>` `<` `>=` `<=` `!=` `<>` `==`
- 位运算 `>>` `<<` `&` `^` `|` `~`

自定义：
不能创建新的operator，但是可以overload


## overload 怎么自己定义？或者添加新的规则？


## 关键字算对象吗？ Object


## 类型分为Scalar和non-scalar？ type scalar不可分？什么意思？

scalar 是不可分的，可以看做是atoms of language.

Python's types of scalar objects:

- int
- float
- bool
- None

Non-scalar:

- strings, have internal structure.??


#### atom 又是什么鬼？

不可分割，原子

Atoms are the most basic elements of expressions

- Identifier(name)
- Literals
- Dict
- List
- Set
- Tuple
- 


## 英文Literal代表什么意思？

就是字面的意思，字符串和数字。

也有没有想象力的意思。

## 除法操作符 / 和 // 有什么区别？

根据operator module 中的命名来看

- `/`是float point division，有浮点数就是真除 e.g., 3/2.0 --> 1.5 
- `//`是floor division(also called integer division)， 结果一定是整数（直接取整数部分），但是返回值的类型取决于是否有浮点数的出现


## 快速交换变量的值？ 酷狗的基本面试题

使用多重赋值（multiple assignment）

```python
x, y, = y, x
```
先对右边的表达式进行求值，再赋值。


## 计算复杂度 Conputational complexity

存在一个时间常量，程序的运行步骤不随着输入的改变而超过这个数值。

运行时间不会怎长随着输入的变化。

O(X) ...

## sequence type 

共享的操作：

- Length e.g., len("abc")
- indexing e.g, "abc"[0]
- Slicing e.g., "abc"[0:2]

#### 那些是sequence types？

- str
- list
- tuple
- unicode
- bytearray
- buffer
- xrange
