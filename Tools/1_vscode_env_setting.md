# VS Code 开发环境设置

## 运行环境
* Mac os 10.13.6
* VS code 1.31.1


## 常用设置
### 1. 隐藏.pyc文件
* 调整Workspace Settings添加如下图，
![Image](images/files_exclude.png)
__设置路径__：Code -> Preferences -> Settings -> Workspace Settings, Search Settings

### 2. 配置markdown-pdf 插件
* 安装说明:

    Chromium download starts automatically when Markdown PDF is installed and Markdown file is first opened with Visutal Studio Code.

    However, it is time-consuming depending on the environment because of its large size (~ 170Mb Mac, ~ 282Mb Linux, ~ 280Mb Win).

    During downloading, the message Installing Chromium is displayed in the status bar.

    If you are behind a proxy, set the http.proxy option to settings.json and restart Visual Studio Code.

    If the download is not successful or you want to avoid downloading every time you upgrade Markdown PDF, please specify the installed Chrome or 'Chromium' with markdown-pdf.executablePath option.
* 设置 markdown-pdf.executablePath
    ```
    "markdown-pdf.executablePath": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ```
* 保存后，重启vscode 即可。
* 如何使用自定义css
    ```
    // 路径和css文件名以你的文件为准
    "markdown-pdf.styles": ["/.markdown/github.css"],
    ```
    自定义样式参考：http://markedstyle.com/styles
    
    __设置路径__：Code -> Preferences -> Settings


### 3. vscode golint 代码规范解读
#### 警告1
* 描述：exported function xxx should have comment or be unexported
* 环境：
```
=> ~$ go version
go version go1.12.1 darwin/amd64
=> ~$ gopls version
version v0.1.3-cmd.gopls, built in $GOPATH mode
```
* 解决：

Comment SentencesSee https://golang.org/doc/effective_go.html#commentary. Comments documenting declarations should be full sentences, even if that seems a little redundant. This approach makes them format well when extracted into godoc documentation. Comments should begin with the name of the thing being described and end in a period:

记录声明的注释应该是完整的句子，即使这看起来有点多余。这种方法使它们在提取到 godoc 文档时格式良好。注释应以所述物品的名称开始，并以句号结束:
```
// Request represents a request to run a command.
type Request struct { ...
// Encode writes the JSON encoding of req to w.
func Encode(w io.Writer, req *Request) { ...
```

#### 示例警告
```
recorder.go:55:5: exported var RecordBind should have comment or be unexported
recorder.go:158:1: exported function Record_ErrorRecord should have comment or be unexported
recorder.go:173:6: don't use underscores in Go names; type Data_MemStats should be DataMemStats
recorder.go:179:2: struct field FreeRam should be FreeRAM
```

golint 会检测的方面：
* 变量名规范
* 变量的声明，像```var str string = "test"```，会有警告，应该```var str = "test"```
* 大小写问题，大写导出包的要有注释
* x += 1 应该 x++

[返回首页](/index.html)
