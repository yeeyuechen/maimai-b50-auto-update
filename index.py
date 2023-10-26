# b50无人值守更新
import pyautogui
import time
import os

#Welcome
os.system('cls')
print('舞萌DX B50/B40 无人值守更新 版本 1.0')
print('如果鼠标无法点击游戏记录请修改index.py文件')
print(' ')

#输入循环运行间隔时间及核心信息
core = input('输入查分器更新核心的绝对路径（路径后可以添加参数）：')
print("输入b50更新间隔时长（单位：min）")
tmot = input('输入：')
tmot = float(tmot)
fintmot = tmot * 60

#循环执行
while True:
    time.sleep(fintmot)
    os.system('start cmd.exe cmd /k' + core)
    pyautogui.moveTo(225, 700, duration=1)
    pyautogui.click(225,700)
    pyautogui.moveTo(225, 625, duration=1)
    pyautogui.click(225,625)
    time.sleep(5)
    pyautogui.hotkey('alt','f4')
    pyautogui.hotkey('alt','tab')
    time.sleep(30)
    pyautogui.hotkey('alt','f4')