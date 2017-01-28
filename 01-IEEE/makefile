plot.pdf : plotter.py data.dat
	python plotter.py

data.dat : a.out
	./a.out > data.dat

a.out : IEEE.c
	gcc IEEE.c -lm
