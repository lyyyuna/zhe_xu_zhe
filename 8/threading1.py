import threading
import time

lock = threading.Lock()

def action(i):
    time.sleep(i)
    print threading.current_thread().name
    time.sleep(i)


for i in range(4):
    t1 = threading.Thread(target=action, args=(i,))
    t1.name = 'dshfi ' + str(i)
    t1.start()