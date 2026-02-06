#1. Synchronous (Single-threaded) ->
#Tasks run 1 after another, each task blocks the next, simple, slow for I/O heavy work

#2. Threading
#Multi threads within 1 process, best for I/O

#3. Multiprocessing
#Multiple processes, each process has its own python interpreter


 #3 Synchronous Code Example (Blocking)
 #Problem: Tasks run one after another
 
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Finished task {name}")
    
start_time = time.time()

task('A')
task('B')
task('C')

end_time = time.time()

print('Total time: ', end_time - start_time)



#AsyncIO version (non-blocking)

import asyncio
import time

async def task(name):
    print(f"Starting task {name}")
    await asyncio.sleep(2)
    print(f"Finished task {name}")
    return f"Result of task {name}"

async def run_asyncio():
    results = await asyncio.gather(task("A"), task("B"), task("C"))
    return list(results)

if __name__ == "__main__":
    start_time = time.perf_counter()
    results = asyncio.run(run_asyncio())
    elapsed_time = time.perf_counter() - start_time

    print("Asyncio results")
    for result in results:
        print(f" {result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran concurrently using asyncio — modern approach for I/O-bound tasks")


#Output:
# Starting task A
# Starting task B
# Starting task C
# Finished task A
# Finished task B
# Finished task C
# Asyncio results
#  Result of task A
#  Result of task B
#  Result of task C

# Total time: 2.00 seconds
# Note: Tasks ran concurrently using asyncio — modern approach for I/O-bound tasks


#What just happened?
#Feature -> Synchronous -> AsyncIO
#Excution -> One-by-one -> Concurrent
#Blocking -> Yes -> No
#Thread count -> 1 -> 1
#Speed -> Slow -> Fast 
#Best for -> Simple tasks -> I/O-bound tasks*


#Asyncio explained:
#great for:
#-> waiting for data from the internet
#-> waiting for a file read
#-> waiting for a timer

#This means:
#-> Task A starts
#-> Task B starts
#-> Task C starts
#-> All three are sleeping at the same time, instead of one waiting for another. 
#-> Total time is arounf 2 seconds, not 6 secs


#Without asyncio (normal code):
#-> Task A: wait 2 sec
#-> Task B: wait 2 sec
#-> Task C: wait 2 sec
#Total = 6 seconds

#With asyncio:
#-> Task A starts waiting 
#-> Task B starts waiting
#-> Task C starts waiting
#All sleep at the same time 
#Total = 2 seconds

#With asyncio, your program can do other things while waiting
#Summary:
#Thing -> Meaning
#async def -> creates an asynchronous function
#await -> "Pause here, let others run"
#asyncio.sleep(2) -> A non-blocking 2 second wait
#asyncio.gather() -> Run many async tasks together
#asyncio.run() -> Start the async event loop
