[返回首页](/index.html)
### 序言
因为 apparmor 加入了 Linux 内核中，提高了Linux程序的安全性，但同时也限制了应用程序对系统资源的访问权限，

如，在修改 mysql 的数据目录时，需要给 mysqld 添加可以访问的目录资源，具体操作如下：

1. 在 /etc/apparmor.d/usr.sbin.mysqld 增加 mysqld 可访问的新的目录（新的data目录）的权限
```
/path/new-dir/ r,
/path/new-dir/** rwk,
```

2. 重启 apparmor service： 
```
$ sudo service apparmor restart
```

3. 确认mysql 配置当前使用的目录
```
$ sudo grep  -E 'datadir|log_error'  /etc/mysql/mysql.conf.d/mysqld.cnf

# datadir		= /var/lib/mysql
datadir		= /path/new-dir
log_error = /path/log/mysql/error.log
```
4. 重启mysql
```
$ sudo service mysql restart
```

_注_: mysql重启时，注意查看日志，因为我发现apparmor也是通过日志找到因为其才不能正常启动的。
