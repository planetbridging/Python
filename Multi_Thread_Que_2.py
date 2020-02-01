import queue
import time
from threading import Thread

def worker(yay):
    print(yay)
    #time.sleep(5)
    #while True:
     #   item = q.get()
      #  print ("waiting")
       # time.sleep(5)
        #print ("well" + yay)
        #q.task_done()
    return

    
q = queue.Queue()
for i in range(5):
    t = Thread(target=worker, args=('yayy' + str(i),))
    t.daemon = True
    t.start()

for item in range(5):
    #q.put(item)
    q.join()


print("alldone")
