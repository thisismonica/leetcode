import threading
import time
def myfun(i):
	print i, " going to sleep for 5 sec..."
	time.sleep(5)
	print i, "thread exit"

for i in range(5):
	t = threading.Thread( target=myfun, args=(i,) )
	t.start()
	time.sleep(1)
