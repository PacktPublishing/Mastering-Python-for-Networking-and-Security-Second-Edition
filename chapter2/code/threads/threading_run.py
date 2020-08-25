import threading

class MyThread(threading.Thread):

    def __init__ (self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        print(self.message)

def test():
    for num in range(0, 10):
        thread = MyThread("I am the "+str(num)+" thread")
        thread.name = num
        thread.start()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test",number=5))
