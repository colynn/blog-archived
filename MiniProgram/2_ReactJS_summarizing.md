## 序言

## 正确地使用State

### 不要直接修改state
例如， 此代码不会重新渲染组件：

```
// Wrong
this.state.comment = 'Hello';
```

而是应用使用setState():

```
// Correct
this.setState({comment: 'Hello'})
```

__注__: 构造函数是唯一可以给 this.state 赋值的地方.

### State 的更新可能是异步的

出于性能考虑，React 可能会把多个 setState() 调用合并成一个调用。

因为 this.props 和 this.state 可能会异步更新，所以你不要依赖他们的值来更新下一个状态。

例如，此代码可能会无法更新计数器：

```
// Wrong
this.setState({
  counter: this.state.counter + this.props.increment,
});
```

要解决这个问题，可以让 setState() 接收一个函数而不是一个对象。这个函数用上一个 state 作为第一个参数，将此次更新被应用时的 props 做为第二个参数：

```
// Correct
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

上面使用了箭头函数，不过使用普通的函数也同样可以：


```
// Correct
this.setState(function(state, props) {
  return {
    counter: state.counter + props.increment
  };
});
```

### State 的更新会被合并 /？
 


## 事件处理
React 元素的事件处理和 DOM 元素的很相似，但是有一点语法上的不同:
* React 事件的命名采用小驼峰式（camelCase），而不是纯小写。
* 使用 JSX 语法时你需要传入一个函数作为事件处理函数，而不是一个字符串。


__注__: 你必须谨慎对待 JSX 回调函数中的 this，在 JavaScript 中，class 的方法默认不会绑定 this。如果你忘记绑定 this.handleClick 并把它传入了 onClick，当你调用这个函数的时候 this 的值为 undefined。

这并不是 React 特有的行为；这其实与 JavaScript 函数工作原理有关。通常情况下，如果你没有在方法后面添加 ()，例如 onClick={this.handleClick}，你应该为这个方法绑定 this。



## 问题
1. 在npm下载包(创建react-app时）时出现如下错误：

    ```
    npm ERR! Maximum call stack size exceeded 
    npm ERR! A complete log of this run can be found in:
    npm ERR! path/log
    ```
    
    解决：
    1. 查询具体的path的log, 一般是npm的版本问题或是npm cache的权限问题。

        * 更新npm版本的方式

        ```
        npm install npm -g --registry https://registry.npm.taobao.org 
        ```

        * 确认cache目录权限及修改所有者的方式或可以直接清理node的缓存。

        ```
        ## 确认目录的所有
        $ ls -dl /path/dir/.npm/_cacache/* 

        ## 修改cache目录的所有者
        $ sudo chown $(id -F) /path/dir/.npm/_cacache/* 

        ## [Deprecated]清理node缓存
        $ npm cache clean -f
        ``` 
    

[返回首页](/index.html)