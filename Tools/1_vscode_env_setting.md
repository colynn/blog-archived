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
    __设置路径__：Code -> Preferences -> Settings

[返回首页](/index.html)
