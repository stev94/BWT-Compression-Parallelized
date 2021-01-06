.PHONY: test-cli
test-cli:									## Run python tests
	source venv/bin/activate && \
	pytest tests/test_pbwt.py::TestPBWT::test_run_tests tests/test_cli.py

.PHONY: make-venv
make-venv:									## Create python venv
	virtualenv -p python venv

.PHONY: clean-cli
clean-cli:									## Clean python build stuff
	@rm -rf $(CURDIR)/venv && \
	rm -f $(CURDIR)/pbwt

.PHONY: cli-dependencies
cli-dependencies: make-venv					## Install cli dependencies
	source venv/bin/activate && \
	cd cli && \
	pip install -e . && \
	rm -rf pbwt_cli.egg-info
