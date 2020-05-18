import threading

class thread_message(threading.Thread):

    def __init__ (self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        print(self.message)

threads = []
for num in range(0, 10):
    thread = thread_message("I am the "+str(num)+" thread")
    thread.start()
    threads.append(thread)

#  wait for all threads to complete by entering them
for thread in threads:
    thread.join()