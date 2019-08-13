## 数据类型

```
var length = 7;                             // 数字
var lastName = "Gates";                      // 字符串
var cars = ["Porsche", "Volvo", "BMW"];         // 数组
var x = {firstName:"Bill", lastName:"Gates"};    // 对象 
var x = true;     // 布尔值
var y = false;    //布尔值
```

### 数组添加元素
1. push() 结尾添加

| 参数 | 描述 | 
| ------ | ------  |
| newelement1	| 必需。要添加到数组的第一个元素。|
| newelement2	| 可选。要添加到数组的第二个元素。|
| newelementX	| 可选。可添加多个元素。|

2. unshift() 头部添加

| 参数 | 描述 | 
| ------ | ------  |
| newelement1	| 必需。要添加到数组的第一个元素。|
| newelement2	| 可选。要添加到数组的第二个元素。|
| newelementX	| 可选。可添加多个元素。|

3. splice() 方法向/从数组指定位置添加/删除项目，然后返回被删除的项目。

| 参数 | 描述 | 
| ------ | ------  |
| index	| 必需。整数，规定添加/删除项目的位置，使用负数可从数组结尾处规定位置。|
| howmany	| 必需。要删除的项目数量。如果设置为 0，则不会删除项目。|
| item1, ..., itemX	| 可选。向数组添加的新项目。|


### 数组删除元素
1. splice 方法

如：```array.splice(index, nums);```

__注__: 数组长度相应改变,但是原来的数组索引也相应改变，splice参数中第一个index,是删除的起始索引(从index算起); 第二个nums,是删除元素的个数.

此时遍历数组元素可以用普通遍历数组的方式,比如for,因为删除的元素在数组中并不保留。


2. delete 方法

如： ```delete array[index] ```

__注__：这种方式数组长度不变,此时 array[index]对应的index会变为undefined,好处是原来数组的索引也保持不变,此时要遍历数组元素可以才用.这种遍历方式跳过其中undefined的元素，所以非常实用。

获取数组下表的函数

```

/*
* 获取某个元素下标
*
*       arrays  : 传入的数组
*
*       obj     : 需要获取下标的元素
* */
function contains(arrays, obj) {
    var i = arrays.length;
    while (i--) {
        if (arrays[i] === obj) {
            return i;
        }
    }
    return false;
```

### 对象添加元素

```
var jsonObj={

      'param1':22,

      'param2' :33

};

 

jsonObj.newParam ='pre';

// 新的属性添加以后，json对象变成：

var jsonObj={

      'param1':22,

      'param2' :33,

      'newParam':'pre'

};
```

### 对象删除元素

```
delete jsonObj.age;
//结果：Object { id: 1, name: "danlis" }
```

### 比较运算符

假定 x = 5;

| 运算符 | 描述 | 比较 | 返回 |
| ------ | ------ | ------ |------ |
| == | 等于     | x == 8      | false |
| === | 值相等并且类型相等  | x === 8 | true |
| != | 不相等     | x != 8      | true |
| !== | 值不相等或类型不相等  | x !== 5 | false |

### 条件（三元）运算符

语法

```
variablename = (condition) ? value1:value2
```


实例

```
var voteable = (age < 18) ? "太年轻":"足够成熟";
```



[返回首页](/index.html)