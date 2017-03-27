V.png : plotter.py output.dat
	python plotter.py

output.dat : a.out
	time ./a.out > output.dat

a.out : placa.c
	gcc -fopenmp placa.c
