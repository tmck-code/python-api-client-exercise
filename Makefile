pip/clean:
	./setup.py clean && \
		rm -rf build dist interview_python_api.egg-info

pip/build: pip/clean
	./setup.py bdist

pip/install: pip/build
	./setup.py install

.PHONY: pip/clean pip/build pip/install
