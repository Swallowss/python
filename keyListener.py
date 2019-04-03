
import threading
from pynput import keyboard
from loopMain import *
from stopThread import *
t = None
class keyListener(object):
    
    def on_press(self,key):
        pass
    def on_release(self,key):
        lm=loopMain();
        st=stopThread();
        global t
        if key==keyboard.Key.f2:
            if t is not None:
                try:
                   st.stop_thread(t)
                except:
                    print("线程已结束")
                    t = None
                else:
                   t = None
            else:
                 t = threading.Thread(target=lm.fullLoop, args=(30,))
                 t.start();
        elif key==keyboard.Key.f4:
            if t is not None:
                try:
                   st.stop_thread(t)
                except:
                    print("线程已结束")
                    t = None
                else:
                   t = None
            else:
                 t = threading.Thread(target=lm.zeroLoop, args=(30,))
                 t.start();
        elif key==keyboard.Key.f12:
            return False
    
    def onListener(self):
        print('开启监听....');
        with keyboard.Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()