
import threading
from pynput import keyboard
from loopMain import *
from stopThread import *
t = None

#奥元素0-4s开 满勾玉循环-黑人起手
fullLoopBtn=keyboard.Key.f1
# 火2s-电1.5s 0勾玉不满-黑人起手
zeroLoopBtn=keyboard.Key.f2
# 火3.5-电3开 满勾玉循环-陨石起手起手
meteorite_fullLoopBtn=keyboard.Key.f3

class keyListener(object):
    def on_press(self,key):
        pass
    def on_release(self,key):
        lm=loopMain();
        st=stopThread();
        global t
        if key==fullLoopBtn:
            if t is not None:
                try:
                   st.stop_thread(t)
                except:
                    print("宏已关闭")
                    print("线程已结束")
                    t = None
                else:
                    print("宏已关闭")
                    t = None
            else:
                 t = threading.Thread(target=lm.fullLoop, args=(30,))
                 t.start();
        elif key==zeroLoopBtn:
            if t is not None:
                try:
                   st.stop_thread(t)
                except:
                    print("宏已关闭")
                    print("线程已结束")
                    t = None
                else:
                    print("宏已关闭")
                    t = None
            else:
                 t = threading.Thread(target=lm.zeroLoop, args=(30,))
                 t.start();
        elif key==meteorite_fullLoopBtn:
            if t is not None:
                try:
                   st.stop_thread(t)
                except:
                    print("宏已关闭")
                    print("线程已结束")
                    t = None
                else:
                    print("宏已关闭")
                    t = None
            else:
                 t = threading.Thread(target=lm.meteorite_fullLoop, args=(30,))
                 t.start();
        elif key==keyboard.Key.f12:
            return False
    
    def onListener(self):
        print('开启监听....');
        with keyboard.Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()