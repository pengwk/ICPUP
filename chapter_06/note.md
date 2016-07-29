# Testing and Debugging

## 定义

测试：试着确定程序是否如期望般运行的过程。

调试：试着修正一个你已知他不会如期望般运行的程序的过程

测试和调试应该在程序编写前就开始思考。好的程序员依照方便测试和调试的思路来写程序。关键点是将程序分离成能实现、测试、调试的独立于其他部分的部分。

能够被单独实现、单独测试、单独调试（模块化程序）

一个函数只做一件事，是不是就是这个目的？

## 基本错误 （这个话题好大）

- syntax errors
- static semantic errors

举个例子：


## Testing

测试的关键是寻找合适的测试数据。能够显现程序所有可能的错误，同时不会运行太长时间。寻找这些数据的方法是：将所有的输入分类，从每一个子集选一个输入，构成测试数据。这基本上是一个不可能实现的目标，是我们的理想与追求。

>A *partition* of a set divides that set into a collection of subsets such that each element of original set belongs to exactly one of the subsets.

一个集合的元素是另一个的所有子集（互不包含）

一个集合的partition是其所有的元素互不重叠的子集。

寻找输入的分类并不容易。

> Typically, people rely on heuristics based on exploring different paths through some combination of the code and the specifications.

- 文档 -> black-box testing  
- 探索代码不同组合形成的路径 -> glass-box testing

#### 探索不同的执行路径

通过：

- 文档（规范） -> black-box testing
- 代码 -> glass-box testing

##### specification 文档、规范 


测试与实现分离,当实现改变时测试数据集不用重新寻找。

###### boundary conditions

- aliasing 别名 同一object多个name引用

##### Glass-Box Testing （rarely sufficient）

glass-box test suite path-complete

可以使用商业工具主观检测（objectively measure）glass-box test的完成度。

不能保证显示所有BUG即使path-complete

##### Conducting Tests

- unit testing
- integration testing

Software Quality Assurance（SQA）

- test drivers 模拟程序使用unit的部分。被测试的部分 调用被测试代码的部分
- stubs 模拟程序被unit使用的部分。程序中除去被测试的部分 被测试代码调用其他程序的部分

stubs: check argument, environment, return value consistent with the specification

可以测试那些还未被开发的程序，甚至是尚不存在的硬件

在其依赖的其他程序、硬件尚不存在的情况下，进行程序的测试

###### regression testing ??

回归测试。修改->测试->修改

## keyword

- test suite 
- partition
- characterize
- intended behavior

- common sense
- tedious
- charming urban legend

- manifestation
- 

## Debugging

程序中的bug，是自己犯的错误。

Runtime bugs:

- overt -> covert
- persistent -> intermittent

overt bug: 有明显的特征症状，显示。
covert bug： 不明显，没有什么信息表明他有问题。 最危险

persistent bug： 输入相同时，bug就会出现
intermittent bug： 接近相同条件下，输入相同，bug也不一定出现。 Chapter 12会比较多好奇中。


### 好思路，怎么做？？

最好的bug是既overt又persistent的，好的程序员会将程序按容易发生这种错误的方式写。
defensive programming 防御式编程

既然covert和intermittent的bug很难找，那就改变写程序的方式思路。这样做的坏处是什么？


if the conditions provoking the bug are not clear, life is much harder. 

###  Learning to Debug 学会调试

调试是为非预期行为的出现搜寻一个解释的过程。在搜寻的过程中要系统进行。

1. 从已知数据中寻找信息。测试结果和程序本身。 测试通过和不通过的数据都显示了问题的存在，试着弄明白为什么有的测试会通过而有的会失败。因为BUG的存在，所以看到代码时要记住自己没有完全理解他。（哭）

2. 提出一个满足所有数据的假设，形式是：如果我改了这里，问题就会消失。

3. 设计并运行一个有可能证明假设并且可重复的实验，在实验之前想好对可能出现的结果的解释（很重要）。

4. 记录已经尝试过的实验。
> insanity is doing the same thing, over and over again, but expecting different results.

#### 设计实验


调试就是寻找，每次尝试都是缩小搜索范围。

- 设计一个可以确定特定区域代码是否对integration testing负责实验。`a problem uncovered during integration testing.` 
- 减少用来引发bug的测试数据 `the amount of test data needed to provoke a manifestion of a bug.`

系统的减少搜索空间。 systematically reduce the search space.

- binary search


We have now narrowed the bug to one line.

An aliasing bug has bitten us.

###### 当事情变得更为艰难

> When the going gets tough, the tough get going. Joseph P.Kennedy


hints:

- wrong order
- misspell
- side effect
- reinitialize
- value equality & object equality(id)
- object -> type
- alias
- Stop asking yourself why the program isn't doing what you want it do. Intead, ask yourself why it is doing what it is.（与其问自己程序为什么不做自己让他做的事，不如问自己他为什么要做这些事）
- Keep in mind that the bug is probably not where you think it is.
- Try to explain the problem to somebody else.
- Don't believe everything you read.
- Stop debugging and start to writing documentation.
- Walk away, and try again tomorrow.


bug 很有可能在你注意不到的地方，注意到了还会犯错？？

找不对的原因不如找发生的解释。

写文档，讲给别人听 ——> 梳理思路

##### bug 找到后

找到后立即修复，非常开心。 慢一点，我们的目标不是修复一个bug，而是建造一个没有bug的程序。

询问自己这个bug是否能解释所有的现象，或者说这个bug只不过是冰山一角。(it is just the tip of the iceberg)

在修改之前，试着理解ramification of the proposed "fix"。这个修改会影响其他吗？会变得复杂吗？可以为其他部分的代码tidy up吗？

如果有许多无法解释的错误，那么用更好的方式来组织程序或者能简单正确实现的算法。



----

- black box
- glass box
- 边际测试 

黑盒测试：只看输入输出

白盒测试：遍历内部路径

边界测试：测试那些按类型或者是按其他类型分类的‘中间’值（e.g. 1，-1 ，0）


提高代码质量究竟包含什么意思？

- TDD
- unit test
- 

#### 测试覆盖100%是什么鬼？


#### 在Python中如何进行？


## Debug

## 分类

- covert
- 

什么BUG最容易被发现？

什么BUG危害最大？


## 解决方法

- binary search
- problem space
- 

before running code,

1. 提出一个满足所有数据的假设
2. 验证它
3. 再次测试

#### 想法、思路

- 找到异常行为的解释。

- 修复一个BUG并不是最重要的，建立一个没有错误的软件才是
- 在运行调试代码之前，想清楚所有可能结果的解释。不能仅依靠运行结果来解释代码。
- the general principles are applicable to getting any complex system to work. 通用准则对任何复杂的系统都是适用的。


## 文档

假设
结果
参数说明

#### 具体的语法是怎么样的啊？

## 感悟

编程是心智的体现，在各种限制条件下做出符合需求的软件或者功能。我以前倾向于直接写代码，这样太浪费时间了，做了错事，事倍功半。 应当符合各种基本要求，比如先规划后写，坚持写文档，命名规范，好烦。不可以再像以前那样写程序了。简直就是自毁前程！


We hate to bring this up, but Dr.Pangloss was wrong.

>"all is for the best" in the "best of all possible worlds"

>Best of all possible worlds

[Best of all possible worlds](https://en.wikipedia.org/wiki/Best_of_all_possible_worlds)

[Dr.Pangloss](http://www.merriam-webster.com/dictionary/Panglossian)