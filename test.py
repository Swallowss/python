
import time
import threading
from pynput import keyboard
from pykeyboard import PyKeyboard
import inspect
import ctypes
k = PyKeyboard()
if __name__=='__main__':

    
    t = None

    def loop(n):
        while  n > 0:
            print('T-minus', n)
            keyEnter("-",0.5)
            n -= 1
            time.sleep(1)
    # keyWord 键盘点击 sec 延迟时间
    def keyEnter(keyWord,sec):
        k.press_key(keyWord)
        time.sleep(sec)
        k.release_key(keyWord)

    def _async_raise(tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
 
    def stop_thread(thread):
        _async_raise(thread.ident, SystemExit)
    def on_press(key):
        print('on_press',key);
    def on_release(key):
        global t
        if key==keyboard.Key.f1:
            if t is not None:
                stop_thread(t)
                t = None
            else:
                 t = threading.Thread(target=loop, args=(10,))
                 t.start();
        elif key==keyboard.Key.f12:
            return False

    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
