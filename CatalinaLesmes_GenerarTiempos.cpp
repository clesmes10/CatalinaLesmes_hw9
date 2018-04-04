#include <iostream>
#include <ctime>
using namespace std;
//funcion recursiva para obtener los valores de fibonacci pto 1

int fibonacci(int N){
	if(N < 2){
		return N;}
	else{
		return fibonacci(N-1) + fibonacci(N-2);}
	}
//funcion para retornar el numero de segundos que se demora la funcion de fibonacci en obtener el n-esimo numero
float get_time(int N){
	clock_t t;
	t = clock();
	fibonacci(N);
	t = clock() - t;
	float time = ((float)t)/CLOCKS_PER_SEC;
	return time;
	 }
//funcion que corre todo el codigo

int main() {
	int N;
        int i;
	N = 35;
	fibonacci(N);
	get_time(N);
	for(i=0; i<N +1; i++){
		cout << i  << " " << get_time(i) << endl;}
	return 0;
}

