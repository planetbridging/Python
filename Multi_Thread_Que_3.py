from concurrent.futures.thread import ThreadPoolExecutor
import time

def call_script(ordinal, arg):
    print('Thread', ordinal, 'argument:', arg)
    time.sleep(2)
    print('Thread', ordinal, 'Finished')

args = ['argumentsA', 'argumentsB', 'argumentsC']

with ThreadPoolExecutor(max_workers=2) as executor:
    ordinal = 1
    for arg in args:
        executor.submit(call_script, ordinal, arg)
        ordinal += 1
print('All tasks has been finished')
