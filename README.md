### 背景

项目参考：https://github.com/Kin-L/PressTrigger
开源万岁

### 功能

反引号 ` 键总开关

长按 J 键自动替换为连续输入 J

进程没有主界面，托盘图标为蓝色时为开启状态，黄色为关闭状态，右键图标可选择退出

### 部署

环境要求：python3.7+, pip21.0+

#### 依赖安装

`pip install keyboard pystray pillow plyer pywin32`

#### 通过pyinstaller打包

`pip install pyinstaller`

```shell
pyinstaller --name=应用名 --onefile --noconsole --icon=icon.ico --hidden-import plyer.platforms.win.notification main.py
```

或`pyinstaller main.spec`