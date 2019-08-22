## 序言

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