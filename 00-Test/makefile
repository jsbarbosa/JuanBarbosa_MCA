output.pdf : data.dat python.py
	python python.py data.dat
data.dat : a.out
	./a.out > data.dat
a.out : generator.c
	gcc generator.c -lm
