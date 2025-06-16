import threading
import time

# Function to print numbers from 1 to 5 with a delay of 1 second
def print_num():
    print("Number Thread starting...")
    for i in range(1, 6):  # Loop through numbers 1 to 5
        print(i)  # Print the current number
        time.sleep(1)  # Pause for 1 second
    print('THREAD NUM IS stopping...')  # Indicate that the thread is stopping

# Function to print letters A to E with a delay of 1 second
def print_alpha():
    print("Thread Alpha is starting...")
    for letter in ['A', 'B', 'C', 'D', 'E']:  # Loop through the list of letters
        print(letter)  # Print the current letter
        time.sleep(1)  # Pause for 1 second
    print('Thread Alpha is stopping')  # Indicate that the thread is stopping

# Create a thread to execute the print_num function
thread1 = threading.Thread(target=print_num)

# Create a thread to execute the print_alpha function
thread2 = threading.Thread(target=print_alpha)

# Start the execution of thread1
thread1.start()

# Start the execution of thread2
thread2.start()

# Wait for thread1 to complete its execution
thread1.join()

# Wait for thread2 to complete its execution
thread2.join()