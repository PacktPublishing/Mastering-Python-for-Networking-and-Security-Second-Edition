import threading

class MyThread(threading.Thread):

    def __init__ (self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        print(self.message)

threads = []
for num in range(0, 5):
	thread = MyThread("I am the "+str(num)+" thread")
	thread.name = num
	thread.start()