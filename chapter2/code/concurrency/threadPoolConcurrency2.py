from concurrent.futures import ThreadPoolExecutor

def message(message):
 print("Processing {}".format(message))

def main():
 print("Starting ThreadPoolExecutor")
 with ThreadPoolExecutor(max_workers=2) as executor:
   future = executor.submit(message, ('message 1'))
   future = executor.submit(message, ('message 2'))
 print("All tasks complete")
  
if __name__ == '__main__':
 main()