import base64
import threading
import time
from io import BytesIO

import keyboard
import pystray
from PIL import Image
from plyer import notification
from win32api import keybd_event

SWITCH = "`"  # 开关按键
INTERVAL = 0.1  # 连发间隔（秒）
# message = True  # 开关通知显示（废弃

# 开关状态下的托盘图标
image_on = Image.open(BytesIO(base64.b64decode(
    "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")))
image_off = Image.open(BytesIO(base64.b64decode(
    "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")))


# 连发核心过程
def auto_press():
    while True:
        while True:
            if keyboard.read_key() == SWITCH:
                break
            else:
                while keyboard.is_pressed("J"):
                    keybd_event(74, 0, 0, 0)
                    keybd_event(74, 0, 2, 0)
                    time.sleep(INTERVAL)
        # if message:
        #     icon.notify(title="连发已禁用", message="按下 ` 键以启用")
        icon.icon = image_off
        icon.title = "连发禁用"
        time.sleep(1)
        keyboard.wait(SWITCH)
        # if message:
        #     icon.notify(title="连发已启用", message="按下 ` 键以禁用")
        icon.icon = image_on
        icon.title = "连发开启"
        time.sleep(1)  # 防止始终读取到切换键


# 退出程序
def on_quit():
    icon.stop()


# 启动子线程执行连发
notification.notify(title="连发已经启动", message="使用 ` 键切换开关", timeout=1)
notification_thread = threading.Thread(target=auto_press, daemon=True)
notification_thread.start()

# 创建托盘图标
menu = pystray.Menu(pystray.MenuItem("退出", on_quit))
icon = pystray.Icon(name="FingerSavior", title="连发开启", icon=image_on, menu=menu)
icon.run()  # 阻塞主进程
