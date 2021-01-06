
.PHONY: build-cy-cli
build-cy-cli: 								## Install cython dependencies
	mkdir -p build/cpypbwt && \
	virtualenv -p python venv && \
	source venv/bin/activate && \
	pip install cython && \
	cd cli/cpbwt/ && \
	python setup_cython.py install && \
	cd $(CURDIR)/cli/cpbwt && \
	cp "build/lib.linux-x86_64-3.8/pbwt_proxy.cpython-38-x86_64-linux-gnu.so" $(CURDIR) && \
	mv dist build ../../build/cpypbwt

.PHONY: clean-cy-cli
clean-cy-cli:								# Clean cython dev environemnt
	@rm -rf $(CURDIR)/venv
	@rm -rf $(BLD_DIR)/cpypbwt
	@rm -f $(CURDIR)/pbwt_proxy.cpython-38-x86_64-linux-gnu.so

.PHONY: test-cy-cli
test-cy-cli:								## Run cython tests
	source venv/bin/activate && \
	pytest tests/test_pbwt.py::TestPBWT::test_run_test_cython

