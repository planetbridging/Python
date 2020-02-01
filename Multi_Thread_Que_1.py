import queue
import time

def do_stuff(q):
  while not q.empty():
    print (q.get())
    time.sleep(5)
    q.task_done()

q = queue.Queue(maxsize=0)

for x in range(20):
  q.put(x)

do_stuff(q)

print("DONE")
