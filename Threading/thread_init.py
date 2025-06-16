import time
import threading

def printnumber():
    print("Thread started")
    for i in range(1, 6):
        print(i)
        time.sleep(1)
    print("Thread Ended")

# Create thread
t = threading.Thread(target=printnumber)

# Start and wait
t.start()
t.join()
