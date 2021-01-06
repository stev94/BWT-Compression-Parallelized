.PHONY: test-cli
test-cli:									## Run python tests
	python -c "import sys; print(sys.path)" && \
	source $(CURDIR)/venv/bin/activate && \
	pytest $(CURDIR)/tests/test_pbwt.py::TestPBWT::test_run_tests $(CURDIR)/tests/test_cli.py

.PHONY: make-venv
make-venv:									## Create python venv
	virtualenv -p python venv

.PHONY: clean-cli
clean-cli:									## Clean python build stuff
	@rm -rf $(CURDIR)/venv && \
	rm -f $(CURDIR)/pbwt && \
	rm -f pbwt_autocomplete.sh

.PHONY: cli-dependencies
cli-dependencies: make-venv					## Install cli dependencies
	source venv/bin/activate && \
	cd cli && \
	pip install -e . && \
	rm -rf pbwt_cli.egg-info

.PHONY: build-autocomplete
build-autocomplete: 						## Builds autocomplete
	$(shell source venv/bin/activate && _PBWT_COMPLETE=source ./pbwt > pbwt_autocomplete.sh)
