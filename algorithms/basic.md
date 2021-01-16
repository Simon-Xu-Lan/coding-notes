# subString vs subSequence

- subString: 连续字符, O(n^2)
  - 字符串的子串必须是连续的，如"abcd"的子串有"ab","bcd"等，但是"ac"不是"abcd"的子串。因此，对于长度为 n 的字符串，共有 1+2+...+n 个非空子串，即(n+1)\*n/2 个，是 O(n^2)级别的。
- subSequence: 非连续字符， O(2^n)
  - 字符串的子序列不需要是连续的，因此对于长度为 n 的字符串的子序列，每个字符都有选或不选两种可能。 因此其子序列的数量是指数级别 O(2^n)的

# Global variable

- 全局变量在工程中会出现很大的问题，如果在面试中使用了全局变量，会让人看起来没有什么代码经验

# Python \*

```python
a = [[0] * 2] * 2
a[0][0] = 1
print(a)
# output: [[1, 0], [1, 0]]
# a[0]和a[1]其实是同一个数组的两个分身，它们所对应的数组是相同，因此修改a[0]中的元素，同样会修改a[1]。但是a[0][0]和a[0][1]不是数组（对象），只是数字（基础数据类型，如字符，布尔值等），因此不会同时改变。
```

# Good Quality Code:

- Bug Free
- Good Coding Style:
  - 变量名命名规范有意义
  - 合理使用空格
  - 善于使用空行
- 容易让人读懂的逻辑。
  - **要把复杂的事情用简单的方式**
  - 别把简单的事情写复杂了
- 没有冗余代码
- 有边界检测和异常处理

# Coding Quality

- Coding Style 相关:

  - 二元运算符两边加空格，单元运算符不加空格

    - 二元运算符:
      - - - /
    - 单元运算符:
      - i++ i-- !

  - 花括号和 for, if 之间要加空格(Java)，圆括号和 if 之间要加空格
  - 用空行分隔开不同的逻辑块
  - 逗号, 分号 后面加空格

- Readability 相关

  - 函数名和变量名用 1-2 个单词作为名称
  - 确保一个函数内部不超过 3 层缩进（indention），
    - 如果需要超过了 3 层就用子函数
    - 缩进越多，出错概率越高
  - 多用子函数来减少入口函数的代码量
  - **多用 continue 少用 if**
    ```py
      # Try avoid the following style
      for .....
        if condition:
          do something
          do something
          do something
      # Instead use the following style
      # This style would reduce one layer indentation
      for .....
        if not condition:
          continue
        do something
        do something
        do something
    ```
  - 少用 else

    ```py
    if condition:
      do something
    else:
      do somethings


    if condition
      return
    return
    ```

  - no if else 嵌套， 尽量不要嵌套，用平行 if

    ```py
    # avoid using if else inside another if else
    if A:
      if B:
        do sth 1
      else:
        do sth 2
    else:
      if B:
        do sth 3
      else:
        do sth 4
    # Try to use parallel if
    if A & B:
      do sth 1
    elif A & not B:
      do sth 2
    elif not A & B:
      do sth 3
    elif not A & not B:
      do sth 4

    ```

- Bug Free 相关
  • 不管有没有可能出问题，都要对入口函数的参数进行异常检测
  • 访问一个下标的时候，一定要确保这个下标不会越界
  • 访问一个对象的属性或者方法时，一定要确保这个对象不是空
  • 不用全局变量

- 通过函数化，避免全局变量等手段

- 付无穷大

  ```py
    -float('inf')
  ```

- Enumeration: 枚举法

  - 打擂台算法

- O(N) 时间复杂度的算法：

  - 双指针算法
  - 打擂台算法
  - 单调队列算法
  - 单调栈算法

- 双指针算法

  - 相向双指针 （判断回文串）多
    - Reverse 型
      - 翻转字符串
      - 判断回文串
    - Two Sum
      - 两数只和
      - 三数之和
    - Partition
      - 快速 sort
      - 颜色 sort
  - 背向双指针 （最长回文串）少

  - 同向双指针 多

- Valid Palindrome

  - 判断一个字符串忽略大小写和非法字符之后是否是一个回文串

  ```py
    class Solution:
      """
      @params: A string
      @return: Whether the string is a valid lsakdjf

  ```

- 快速排序在大部分时候的时间复杂度都是 O(nlogn)，但是当数组为逆序排序时（假设每次以第一个元素为 pivot），时间复杂度将会退化到 O(n^2)
