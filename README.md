# stcmcuAutoDownload
## 实现的功能
 - 这是一个通过python3 + selenium4 在完成自动登录 https://www.stmcu.com.cn/ 的账号并随机或顺序下载30次以完成每日得到300积分的程序。
  
## 运行步骤
 - 驱动程序 [msedgedriver.exe](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 需要下载符合 edge 浏览器的版本，自己的 edge 浏览器的版本查看方式为打开浏览器设置中的 [关于 Microsoft Edge](edge://settings/help) 查看。
 - 使用其他浏览器也可以通过下载对应的驱动程序替换 msedgedriver.exe ，并且更改`driver = webdriver.Edge()`中的Edge为需要的浏览器以实现
 - selenium4 需要运行在 python3.7 版本以上的环境中，selenium4 的包可以通过打开命令提示符(CMD)、或者Powershell输入 `pip3 install selenium` 完成下载
 - 满足以上条件后，在 `my_username = <username>` 和 `my_password = <password>` 中填入自己的用户名和密码，进入文件夹中运行 edge.py 即可

## 可能存在的问题
 - website.txt 中的部分网址可能存在下载链接失效的问题，会在后续测试的过程中更新。
 - 如果出现点击 立即下载 后弹出无标题的标签页但是很久没有能够得到下载链接的情况，这可能是因为网速的问题，可以适当的延长延时的时间。相反，如果网速足够快的情况下可以取消延时。
