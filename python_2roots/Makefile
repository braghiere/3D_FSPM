
_${PYTHON_MODN}.so: 
	cp -rf ../dest/gnu/optimised/*.o obj/
	cp ../mod/*.mod .    
	f90wrap -m min3p ../src/* -k kind_map -v --default-to-inout 
	f2py-f90wrap --fcompiler=intelem -c -m _min3p -L. -lsrc f90wrap_*.f90 obj/*.o -lstdc++ 


test: _${PYTHON_MODN}.so
	python test.py

clean: 
	rm -rf f90wrap_*.f90
	rm -rf *.mod 
	rm -rf *.so
	rm -rf obj/*.o
