
##  Go语法
### 变量声明
1. 指定变量类型，如果没有初始化，则变量默认为零值;
    ```
    package main
    import "fmt"
    func main() {

        // 声明一个变量并初始化
        var a = "RUNOOB"
        fmt.Println(a)

        // 没有初始化就为零值
        var b int
        fmt.Println(b)

        // bool 零值为 false
        var c bool
        fmt.Println(c)
    }
    ```
2. 根据值自行判定变量类型
    ```
    var v_name = value
    ```
3. 省略 var, 注意 := 左侧如果没有声明新的变量，就产生编译错误
    ```
    var intVal int 

    intVal :=1 // 这时候会产生编译错误

    intVal,intVal1 := 1,2 // 此时不会产生编译错误，因为有声明新的变量，因为 := 是一个声明语句
    ```
### 多变量声明
```
package main

var x, y int
var (  // 这种因式分解关键字的写法一般用于声明全局变量
    a int
    b bool
)

var c, d int = 1, 2
var e, f = 123, "hello"

// 短声明方式
// 这种不带声明格式的只能在函数体中出现
// g, h := 123, "hello"

func main(){
    g, h := 123, "hello"
    println(x, y, a, b, c, d, e, f, g, h)
}
```
_注_: 
1. 类型在变量名 之后。
2. 当连续两个或多个函数的已命名形参类型相同时，除最后一个类型以外，其它都可以省略。
3. var 语句可以出现在包或函数级别。
4. 变量声明可以包含初始值，每个变量对应一个; 初始化值已存在，则可以省略类型；变量会从初始值中获得类型。
5. 常量可以是字符、字符串、布尔值或数值, 常量不能用 := 语法声明。

### 零值
没有明确初始值的变量声明会被赋予它们的 零值。

零值是：
* 数值类型为 0，
* 布尔类型为 false，
* 字符串为 ""（空字符串）。

### Go 的基本类型有
```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // uint8 的别名

rune // int32 的别名
    // 表示一个 Unicode 码点

float32 float64

complex64 complex128
```

本例展示了几种类型的变量。 同导入语句一样，变量声明也可以“分组”成一个语法块。

```
package main

import (
	"fmt"
	"math/cmplx"
)

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}
```

_注_: int, uint 和 uintptr 在 32 位系统上通常为 32 位宽，在 64 位系统上则为 64 位宽。 当你需要一个整数值时应使用 int 类型，除非你有特殊的理由使用固定大小或无符号的整数类型。

### For循环
Go 只有一种循环结构：for 循环。

* 基本的 for 循环由三部分组成，它们用分号隔开：

初始化语句：在第一次迭代前执行
条件表达式：在每次迭代前求值
后置语句：在每次迭代的结尾执行
初始化语句通常为一句短变量声明，该变量声明仅在 for 语句的作用域中可见。

一旦条件表达式的布尔值为 false，循环迭代就会终止。

注意：和 C、Java、JavaScript 之类的语言不同，Go 的 for 语句后面的三个构成部分外没有小括号， 大括号 { } 则是必须的。

```
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}

```

* 初始化语句和后置语句是可选的。

```   
package main

import "fmt"

func main() {
	sum := 1
	for ; sum < 1000; {
		sum += sum
	}
	fmt.Println(sum)
}
```
* 此时你可以去掉分号，因为 C 的 while 在 Go 中叫做 for。

```
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}
```

### defer
defer 语句会将函数推迟到外层函数返回之后执行。

* 推迟调用的函数其参数会立即求值，但直到外层函数返回前该函数都不会被调用。
```
package main

import "fmt"

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}

```
* 推迟的函数调用会被压入一个栈中。当外层函数返回时，被推迟的函数会按照后进先出的顺序调用。
```
package main

import "fmt"

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}

```

### 指针
Go 拥有指针。指针保存了值的内存地址。

类型 *T 是指向 T 类型值的指针。其零值为 nil。

```
var p *int
```

& 操作符会生成一个指向其操作数的指针。
```
i := 42
p = &i
```

* 操作符表示指针指向的底层值。
```
fmt.Println(*p) // 通过指针 p 读取 i
*p = 21         // 通过指针 p 设置 i
```
这也就是通常所说的“间接引用”或“重定向”。

与 C 不同，Go 没有指针运算。

### 结构体指针
结构体字段可以通过结构体指针来访问。

如果我们有一个指向结构体的指针 p，那么可以通过 (*p).X 来访问其字段 X。不过这么写太啰嗦了，所以语言也允许我们使用隐式间接引用，直接写 p.X 就可以。
```
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	(*p).Y = 19
	p.X = 1e9
	fmt.Println(v)
}
```

### 结构体文法？
结构体文法通过直接列出字段的值来新分配一个结构体。

使用 Name: 语法可以仅列出部分字段。（字段名的顺序无关。）

特殊的前缀 & 返回一个指向结构体的指针。
```
package main

import "fmt"

type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}  // 创建一个 Vertex 类型的结构体

    // ?? 这种就是结构体文法吗？
	v2 = Vertex{X: 1}  // Y:0 被隐式地赋予
	v3 = Vertex{}      // X:0 Y:0
	p  = &Vertex{1, 2} // 创建一个 *Vertex 类型的结构体（指针）
)

func main() {
	fmt.Println(v1, p.X, v2, v3)
}
```

### 数组
类型 [n]T 表示拥有 n 个 T 类型的值的数组。

表达式

```
var a [10]int
```
会将变量 a 声明为拥有 10 个整数的数组。

数组的长度是其类型的一部分，因此数组不能改变大小。这看起来是个限制，不过没关系，Go 提供了更加便利的方式来使用数组。

```
package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

    // ?? 不理解为何种用法
	primes := [6]int{2, 3, 5, 7, 11, 13}  
	fmt.Println(primes)
}
```

### 切片
每个数组的大小都是固定的。而切片则为数组元素提供动态大小的、灵活的视角。在实践中，切片比数组更常用。

类型 []T 表示一个元素类型为 T 的切片。

切片通过两个下标来界定，即一个上界和一个下界，二者以冒号分隔：

```
a[low : high]
```
它会选择一个半开区间，包括第一个元素，但排除最后一个元素。

以下表达式创建了一个切片，它包含 a 中下标从 1 到 3 的元素：

```
a[1:4]
```


* 切片的默认行为 

对于数组
```
var a [10]int
```
来说，以下切片是等价的：
```
a[0:10]
a[:10]
a[0:]
a[:]
```

_注_: 
* 切片就像数组的引用
* 切片并不存储任何数据，它只是描述了底层数组中的一段。
* 更改切片的元素会修改其底层数组中对应的元素。
* 与它共享底层数组的切片都会观测到这些修改。
* 切片s的长度和容量可通过表达式 len(s) 和 cap(s) 来获取。
* 切片的零值是 nil.

### 切片文法、数组文法 应用场景??