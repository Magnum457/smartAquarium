from threading import Thread
import sys
import random

NUM_VALUES = 1000
values = []
sequential_total = 0
threaded_total = 0
threads = []
NUM_THREADS = 4

class Th(Thread):
    subtotal = 0
    
    def __init__(self, num):
        sys.stdout.write("Criando a Thread numero " + str(num) + "\n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        
    def run(self):        
        range_start = int(self.num * NUM_VALUES / NUM_THREADS)
        range_end = int(((self.num + 1) * NUM_VALUES / NUM_THREADS) - 1)

        for i in range(range_start, range_end):
            self.subtotal += values[i]
            
        sys.stdout.write("Subtotal para thread " + str(self.num) +
                                            ": " + str(self.subtotal)
                                                 + "(de " + str(range_start)
                                                 + " para " + str(range_end) + ") \n");
        sys.stdout.flush()
            
    def get_subtotal(self):
        return self.subtotal
        
for i in range(NUM_VALUES):
    values.append(random.randint(0, 100))
    
for i in range(NUM_VALUES):
    sequential_total += values[i]
    
print("Sequential total: " + str(sequential_total))

for thread_number in range(NUM_THREADS):
    threads.insert(thread_number, Th(thread_number))
    threads[thread_number].start()
    
for thread_number in range(NUM_THREADS):
    threads[thread_number].join()
    threaded_total += threads[thread_number].get_subtotal()
    
print("Threaded total: " + str(threaded_total))
