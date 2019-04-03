
import time
from pynput import keyboard
from pykeyboard import PyKeyboard
from  pynput.mouse import Button, Controller
mouse = Controller()
k = PyKeyboard()
#常量定义
blackMan='1'  #黑人 键盘1
meteorite='2' #陨石 键盘2
yuanlibo='3'  #原力波 键盘3
blackHole='4' #黑洞 键盘4
dianxing=Button.left #电刑 鼠标左键
yindao=Button.right  #引导 鼠标右键


# 宏循环的主体 具体的宏要放在这里去实现
class loopMain(object):
    # 键盘按下  k.press_key(keyWord)
    # 键盘抬起  k.release_key(keyWord)
    # 鼠标按下  mouse.press(Button.left)
    # 鼠标抬起  mouse.release(Button.left)

    # keyWord 键盘点击 beginSec 按键开始的延迟时间 endSec 按键结束的延迟时间
    def keyEnter(self,keyWord,sec):
        k.press_key(keyWord)
        time.sleep(sec)
        k.release_key(keyWord)

    #满勾玉时的循环
    def fullLoop(self,n):
        while  n > 0:
            self.loop_32()
            n -= 1
    
    #0勾玉时的循环
    def zeroLoop(self,n):
        while  n > 0:
            if n==30:
                tt=time.time()
                self.blackManLoop()
                time.sleep(1.5)
                self.meteorite_one()
                mouse.press(dianxing)
                time.sleep(1.19)
                mouse.release(dianxing)
                self.meteorite_one()
                mouse.press(dianxing)
                time.sleep(2.294)
                mouse.release(dianxing)
                self.meteorite_blackMan()
                print("--",time.time()-tt)
            else:
                self.loop_32()
            n -= 1
    
    def loop_32(self):
        self.blackManLoop()
        time.sleep(1.5)
        self.meteorite_one()
        mouse.press(dianxing)
        time.sleep(2.094)
        mouse.release(dianxing)
        self.meteorite_blackMan()


    # 单发陨石-带黑洞  黑洞-原力波-电刑-陨石-电刑-引导 持续时间4.255s
    def meteorite_one(self):
        k.press_key(' ') #强制站立
        k.press_key(blackHole) #按下黑洞
        k.release_key(blackHole)
        time.sleep(0.5)
        k.press_key(yuanlibo)
        k.release_key(yuanlibo)
        time.sleep(0.5)
        #电刑5发 
        mouse.press(dianxing)
        time.sleep(1.75)
        mouse.release(dianxing)
        time.sleep(0.05)
        k.press_key(meteorite)
        time.sleep(0.05)
        k.release_key(meteorite)
        mouse.press(dianxing)
        time.sleep(1)
        mouse.release(dianxing)
        mouse.press(yindao)
        time.sleep(0.4)
        mouse.release(yindao)
        k.release_key(' ') #强制站立

    #黑人20s循环 持续时间20.06s
    def blackManLoop(self):
        k.press_key(blackMan)
        k.release_key(blackMan)
        n=20
        while n>0:
            k.press_key('1')
            k.release_key('1')
            time.sleep(1)
            n-=1
    
    #黑人增伤的陨石 持续4.1267
    def meteorite_blackMan(self):
        k.press_key(' ') #强制站立
        k.press_key(blackHole) #按下黑洞
        k.release_key(blackHole)
        time.sleep(0.5)
        k.press_key(yuanlibo)
        k.release_key(yuanlibo)
        time.sleep(0.5)
        #电刑5发 
        mouse.press(dianxing)
        time.sleep(1.75)
        mouse.release(dianxing)
        time.sleep(0.05)
        k.press_key(meteorite)
        time.sleep(0.05)
        k.release_key(meteorite)
        mouse.press(dianxing)
        time.sleep(1.15)
        mouse.release(dianxing)
        mouse.press(yindao)
        time.sleep(0.12)
        k.press_key(blackMan)
        k.release_key(blackMan)
        mouse.release(yindao)
        k.release_key(' ') #强制站立
