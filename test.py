import threading

def thread_1():
 # current_thread().name | 线程名称
 print(threading.current_thread().name)

def thread_2():
 print(threading.current_thread().name)

# 定义任务
t1 = threading.Thread(target=thread_1, args=(), name='Thread_1') # name 定义线程名称
t2 = threading.Thread(target=thread_2, args=(), name='Thread_2') 

# 启动任务
print(threading.current_thread().name) # 当前进程名称
t1.start() # 同步 t1.join | 结束 t1.terminate()
t2.start()
