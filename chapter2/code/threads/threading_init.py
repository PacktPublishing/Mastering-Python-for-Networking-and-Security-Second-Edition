import threading

def myTask():
    print("Hello World: {}".format(threading.current_thread()))

# We create our first thread and pass in our myTask function
myFirstThread = threading.Thread(target=myTask)
# We start out thread
myFirstThread.start()