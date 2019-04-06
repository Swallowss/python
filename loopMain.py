
import time
from pynput import keyboard
from pykeyboard import PyKeyboard
from pynput.mouse import Button, Controller
from myButtonObj import *
mouse = Controller()
k = PyKeyboard()
# # 常量定义
# blackMan = '1'  # 黑人 键盘1
# meteorite = '2'  # 陨石 键盘2
# yuanlibo = '3'  # 原力波 键盘3
# blackHole = '4'  # 黑洞 键盘4
# dianxing = Button.left  # 电刑 鼠标左键
# yindao = Button.right  # 引导 鼠标右键


# 宏循环的主体 具体的宏要放在这里去实现
class loopMain(object):
    # 键盘按下  k.press_key(keyWord)
    # 键盘抬起  k.release_key(keyWord)
    # 鼠标按下  mouse.press(Button.left)
    # 鼠标抬起  mouse.release(Button.left)

    def __init__(self, myButtonObj):
        self.myButtonObj=myButtonObj


    # keyWord 键盘点击 beginSec 按键开始的延迟时间 endSec 按键结束的延迟时间
    def keyEnter(self, keyWord, sec):
        k.press_key(keyWord)
        time.sleep(sec)
        k.release_key(keyWord)

    # 满勾玉时的循环
    def fullLoop(self, n):
        num = 0
        while n > num:
            self.loop_32()
            num += 1

    # 0勾玉时的循环
    def zeroLoop(self, n):
        num = 0
        while n > num:
            if num == 0:
                tt = time.time()
                self.blackManLoop()
                time.sleep(1.5)
                self.meteorite_one()
                mouse.press(self.myButtonObj.dianxing)
                time.sleep(1.19)
                mouse.release(self.myButtonObj.dianxing)
                self.meteorite_one()
                mouse.press(self.myButtonObj.dianxing)
                time.sleep(2.294)
                mouse.release(self.myButtonObj.dianxing)
                self.meteorite_blackMan()
                print("0层勾玉第一次循环历时: ", time.time()-tt)
            else:
                self.loop_32()
            num += 1
    # 满勾玉 陨石起手 
    def meteorite_fullLoop(self, n):
        num = 0
        while n > num:
            if num == 0:
                self.meteorite_blackMan()
            self.loop_32()
            num += 1
    #野外原力波一发陨石
    def meteorite_outSetOneLoop(self,n):
        num = 0
        while n > num:
            self.meteorite_outSetOne()
            num += 1
    #双人 陨石起手 32.03s循环 一发陨石
    def doubleMode_meteorite_fullLoop(self, n):
        num = 0
        while n > num:
            if num == 0:
                self.meteorite_blackMan()
            self.loop_32_one()
            num += 1
    
    # 32s基础循环 两发陨石
    def loop_32(self):
        tt = time.time()
        self.blackManLoop()
        time.sleep(1.5)
        self.meteorite_one()
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(2.094)
        mouse.release(self.myButtonObj.dianxing)
        self.meteorite_blackMan()
        print("32s带勾玉循环历时: ", time.time()-tt)
    
    # 32s基础循环 一发陨石
    def loop_32_one(self):
        tt = time.time()
        self.blackManLoop()
        time.sleep(3.5)
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(4.47)
        mouse.release(self.myButtonObj.dianxing)
        self.meteorite_blackMan()
        print("32s带勾玉循环历时: ", time.time()-tt)

    # 单发陨石-带黑洞  黑洞-原力波-电刑-陨石-电刑-引导 持续时间4.255s
    def meteorite_one(self):
        tt = time.time()
        k.press_key(' ')  # 强制站立
        k.press_key(self.myButtonObj.blackHole)  # 按下黑洞
        k.release_key(self.myButtonObj.blackHole)
        time.sleep(0.5)
        k.press_key(self.myButtonObj.yuanlibo)
        k.release_key(self.myButtonObj.yuanlibo)
        time.sleep(0.5)
        # 电刑5发
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(1.75)
        mouse.release(self.myButtonObj.dianxing)
        time.sleep(0.05)
        k.press_key(self.myButtonObj.meteorite)
        time.sleep(0.05)
        k.release_key(self.myButtonObj.meteorite)
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(1)
        mouse.release(self.myButtonObj.dianxing)
        mouse.press(self.myButtonObj.yindao)
        time.sleep(0.4)
        mouse.release(self.myButtonObj.yindao)
        k.release_key(' ')  # 强制站立
        print("单发陨石历时: ", time.time()-tt)

    # 黑人20s循环 持续时间20.06s
    def blackManLoop(self):
        tt = time.time()
        k.press_key(self.myButtonObj.blackMan)
        k.release_key(self.myButtonObj.blackMan)
        n = 20
        while n > 0:
            k.press_key('1')
            k.release_key('1')
            time.sleep(1)
            n -= 1
        print("黑人循环历时: ", time.time()-tt)

    # 黑人增伤的陨石 持续4.1267
    def meteorite_blackMan(self):
        tt = time.time()
        k.press_key(' ')  # 强制站立
        k.press_key(self.myButtonObj.blackHole)  # 按下黑洞
        k.release_key(self.myButtonObj.blackHole)
        time.sleep(0.5)
        k.press_key(self.myButtonObj.yuanlibo)
        k.release_key(self.myButtonObj.yuanlibo)
        time.sleep(0.5)
        # 电刑5发
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(1.75)
        mouse.release(self.myButtonObj.dianxing)
        time.sleep(0.05)
        k.press_key(self.myButtonObj.meteorite)
        time.sleep(0.05)
        k.release_key(self.myButtonObj.meteorite)
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(1.15)
        mouse.release(self.myButtonObj.dianxing)
        mouse.press(self.myButtonObj.yindao)
        time.sleep(0.12)
        k.press_key(self.myButtonObj.blackMan)
        k.release_key(self.myButtonObj.blackMan)
        mouse.release(self.myButtonObj.yindao)
        k.release_key(' ')  # 强制站立
        print("双黑陨石历时: ", time.time()-tt)

    #带野外原力波黑人陨石一发
    def meteorite_outSetOne(self):
        self.blackManLoop()
        time.sleep(0.5)
        k.press_key(' ')  # 强制站立
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(10.5)
        mouse.release(self.myButtonObj.dianxing)
        time.sleep(0.05)
        k.press_key(self.myButtonObj.meteorite)
        time.sleep(0.05)
        k.release_key(self.myButtonObj.meteorite)
        mouse.press(self.myButtonObj.dianxing)
        time.sleep(1.15)
        mouse.release(self.myButtonObj.dianxing)
        mouse.press(self.myButtonObj.yindao)
        time.sleep(0.12)
        k.press_key(self.myButtonObj.blackMan)
        k.release_key(self.myButtonObj.blackMan)
        mouse.release(self.myButtonObj.yindao)
        k.release_key(' ')  # 强制站立