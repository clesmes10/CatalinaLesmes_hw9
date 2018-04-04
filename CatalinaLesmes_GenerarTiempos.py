import time
 
#funcion recursiva de fibonacci

N = 35
def fibonacci(N):
	if(N<2):
		return N
	else:
		return fibonacci(N-1) + fibonacci(N-2)

#funcion que devuelve el tiempo que se demora la funcion fibonacci en calcular el n esimo numero

def get_time(N):
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return t1
#imprime el resultado
for j in range(N+1):
	print j, get_time(j)
