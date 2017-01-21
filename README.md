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

## Ensure everything went ok

- Open `Task Scheduler`(How to? You know, type "task scheduler" in the search bar of windows start menu)
- Click "Task Scheduler Library", then double-click "bingLockScreen"

Check the settings of the task(I marked the part with a red rectangle):

Normally, You don't need to change the parts of settings in "General" and "Triggers".  

![task_scheduler_general.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_general.png)
![task_scheduler_trigger.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_trigger.png)

Ensure you use set the right path of `python` and `bingLockScreen.py`.

![task_scheduler_actions.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_actions.png)

You had better check the option "Run task as soon as possible after a scheduled start is missed" from "Settings"

![task_scheduler_setttings.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_setttings.png)

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

## 确保一切顺利
- 打开“任务计划程序”(怎么打开？你知道的，在Windows开始菜单搜索框中键入“任务计划”)
- 单击 "任务计划程序库"，然后双击“bingLockScreen”

检查该任务计划的设置（我用红色框高亮的部分）:

通常，你都不需要修改位于“通用”和“触发器”标签下方的设置。

![task_scheduler_general.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_general.png)
![task_scheduler_trigger.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_trigger.png)

确保你给`python`和`bingLockScreen.py`指定正确的路径。

![task_scheduler_actions.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_actions.png)

你最好就勾选位于“设置”的复选项"如果过了计划开始时间，立即启动任务"。

![task_scheduler_setttings.png](https://github.com/WeiqiChenCN/bingLockScreen/raw/master/task_scheduler_setttings.png)
