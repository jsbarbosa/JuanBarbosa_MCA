output.pdf : data.dat
	python python.py data.dat
data.dat : a.out
	./a.out > data.dat
a.out : temp.c
	gcc temp.c