## Exceptions And Assertions

### words

- Virtually
- exceptions
- polymorphic
- In principle
- impose
- defensive programming

### sentence

> We will deal with the exceptional exceptions ——those that do not deal with errors——later in this chapter.

### problem 

- `i.e.`是什么意思？


### 多态 polymorphic

参数是多种不同类型

参数的类型可以是不同的。 因为类型是`first-class`

### first-class & second-class ？ 


### 错误的处理

内部还是外部？

一个函数需要打开一个文件来完成任务，文件打开失败的`IOError`应该在这个函数里处理还是在调用这个函数的地方处理？

有异常出现，必须要处理。 看到异常一般只有异常信息，出错代码位置。具体的错误信息缺乏错误产生的语境，所以调用者得到的信息是不够的。

调用者要么使用返回值计算另一个值，要么处理异常打印出“有用”的消息。

具体的异常在内部处理，同时向外部提供包含语境的更多异常信息，方便处理。


### assert 

- 防御型编程的有用工具。 确认参数的具体类型。

- 调试工具。确认中间值是否正常，函数返回值是否正常。

## 回想

错误，返回值

没有处理的错误会让程序停止运行，提醒程序员考虑充分，而不是让程序继续运行下去。

依靠返回值暗示程序出了问题，粗心没检查返回值是不是None就惨了。

控制流 control flow mechanism

- 一个异常 `except ValueError:pass`
- 多个异常 `except (ValueError, IndexError): pass`
- 所有异常 `except: pass`


assertions 断定

确定程序的运行状态，防止出现错误。可以用来检查参数。在程序即将执行不可恢复的动作时，放上去。

`assert Boolean expression, argument`

多态 poly

多个类型工作，更加通用的代码，范围更广。type是first-class对象。

抛出一个异常`raise ValueError("msg to display")`

----
异常应该放到哪里处理？

函数内，函数外，模块内，模块外

保留更多的信息，

----

我的docstring该怎么写呢？

假设的参数约定
返回结果的保证

参数类型，参数含义，方便生成文档 要用什么语法？ 

----