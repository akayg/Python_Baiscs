import threading

counter = 0

def increment():
    global counter
    for _ in range(10_000_000):
        counter += 1

# Create threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final counter:", counter)
