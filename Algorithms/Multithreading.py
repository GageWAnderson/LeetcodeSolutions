import time
import threading

start = time.perf_counter()

def do(sleepTime):
    print(f"Sleeping for {sleepTime} seconds")
    time.sleep(sleepTime) #Seconds, script waits for a second
    print("Done sleeping")

# t1 = threading.Thread(target=do) #Target is the function you want to run
# t2 = threading.Thread(target=do) #Use start method on each thread to get it to run.

# t1.start()
# t2.start()

# t1.join()
# t2.join() #Makes sure threads complete up to this point

threads = []
for _ in range(10):
    t = threading.Thread(target=do, args=[1.5])
    t.start() #Starts all the threads in the loop
    threads.append(t)

for thread in threads:
    thread.join()

#Starts all the threads in one loop, then joins them all  at the end
print("finished")