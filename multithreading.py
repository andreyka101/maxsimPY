import threading
import time 
def fun_1():
    time.sleep(4)
    print("end")

thread_1 = threading.Thread(target=fun_1)
thread_1.start()

# fun_1()

for i in range(10):
    print(i)

print("-----")
thread_1.join()

for i in "qwertyuiop":
    print(i)