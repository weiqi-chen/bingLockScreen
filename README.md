Result show in the picture

效果如图

![example](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/example.png)

# Bing Lock Screen

My python script to get Bing Today homepage and set it as your lock screen ( for windows 7 )

You can set it as a task from `Task Scheduler`, And Update your lock screen of your Windows 7 daily and automatically .

The script will setup the register and files.

The script has not been test for a long time, And it is writted in python3. So you need to install [python3](https://www.python.org/downloads/) before using it.


# 必应美图锁屏

将必应每天美图设置为你的锁屏（Windows7系统适用）的python脚本。

你可以通过`任务计划`来将其设置为一个任务，然后每一台都自动地更新你的锁屏背景。

这个脚本会设置注册表和文件。

这个脚本尚未经过长时间的测试，而且它是用python3书写的，所以你需要安装[python3](https://www.python.org/downloads/)来使用。


# Installation

1. Download the `bingLockScreen.py` by clicking `Clone or download` -> `Download ZIP`.
2. Unzip and copy `bingLockScreen.py` to `C:\bingLockScreen.py`.
3. Setup a task scheduler.

## Hot to setup the Task Scheduler?

1. Run `cmd` with highest privileges.
2. Run the command below from `cmd`:

 > Before running the command, you must ensure you already have python3 installed on your computer, and make sure the path of python.exe is correct. You may modify it if needed.
 
```
schtasks /create /np /rl HIGHEST  /sc DAILY /tn bingLockScreen /tr "C:\Python34\python.exe C:\bingLockScreen.py" /st 07:00
```
 
Now, You setted up a task scheduler to Download the bing home page and set it as your lock screen.
And It will be run daily at 07:00.
 
 
# 安装
 
1. 通过点击`Clone or download` -> `Download ZIP`来下载`bingLockScreen.py`；
2. 解压缩并复制文件`bingLockScreen.py`到这里`C:\bingLockScreen.py`；
3. 创建一个任务计划
 
## 如何创建任务计划？
 
1. 以管理员权限运行运行命令行提示符(CMD)；
2. 在`CMD`中执行下面的命令:
 
> 使用下方的命令之前，你必须谨慎确认你已经安装了python3，并确认python.exe的路径是否正确。必要时你需要修正下面路径。
 
```
schtasks /create /np /rl HIGHEST  /sc DAILY /tn bingLockScreen /tr "C:\Python34\python.exe C:\bingLockScreen.py" /st 07:00
```

现在，你已经设置了一个任务计划来下载必应美图并设置为你的锁屏。
每天的7点该脚本会自动运行
