import threading 
from ThreadWorker import ThreadWorker

def main():
    # This initializes ''thread'' as an instance of our Thread Worker
   thread = ThreadWorker()
   # This is the code needed to run our created thread
   thread.start()

if __name__ == "__main__":  
	main()