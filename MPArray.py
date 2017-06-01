#success


import multiprocessing as mp
from multiprocessing.sharedctypes import Array
import time

def decrement(baris):
    for x in range(0,5):
        for i, v in enumerate(baris):
            baris[i] = v - 1
        print(baris[:])
        time.sleep(1)
    print(baris[:])

def assign(baris):
    for x in range(0,2):
        baris[1] = 5
        time.sleep(1)
        print('asda')
    print(baris[:])


if __name__ == '__main__':
    baris = Array('i',[10,10,10])#, lock=mp.Lock())
    decrease = mp.Process(target = decrement, args=(baris,))
    decrease.daemon = True
    decrease.start()
    change = mp.Process(target = assign, args=(baris,))
    change.daemon = True
    change.start()

    decrease.join()
    change.join()

    dir(baris)
    print(baris[:])# + 'Final')
