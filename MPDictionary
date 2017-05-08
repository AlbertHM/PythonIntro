import multiprocessing as mp
import time


def waw(queue):
	for i in queue:
		queue[i] -=1
	print('-----'+str(queue)+'----')
	return queue
	
if __name__ == '__main__':
	
	
	q = mp.Manager().dict()
	q['p1'] = 5 #assignment dictionary tidak bisa seperti biasa
	q['p2'] = 3
	q['p3'] = 6
	
	count = mp.Process(target=waw, name='Countdown', args=(q,))
	count.daemon = True
	count.start()
	
	count.join() #wait for the process end
	
	print(q)
