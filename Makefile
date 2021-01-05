.DEFAULT_GOAL := help
SHELL := /bin/bash
THIS_FILE := $(firstword $(MAKEFILE_LIST))

# version
version := $(shell cat cli/version.py | grep __version__ | awk 'BEGIN {FS = " = "}; {print substr($$2, 2, length($$2)-2)}')
VERSION ?= ${version}

# app name
TARGET = pbwt

# directories
SRC_DIR ?= $(CURDIR)/src/sources
HDR_DIR ?= $(CURDIR)/src/headers
BLD_DIR ?= $(CURDIR)/build
OBJ_DIR ?= $(BLD_DIR)/obj
DEP_DIR ?= $(BLD_DIR)/dep
BIN_DIR ?= $(CURDIR)/bin

# files
SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
DEPS := $(OBJS:$(OBJ_DIR)/%.o=$(DEP_DIR)/%.d)
INCL := -I$(CURDIR)/src/include -I$(HDR_DIR)

# C stuff
CC = gcc
CFLAGS = -Wall -Wextra -pedantic -g -O0 $(INCL)
LFLAGS = -lm -lpthread

all: build clean help version

.PHONY: help
help:										## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(THIS_FILE) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: clean-c clean-cli						## Clean builds folder
	@echo "Everything cleaned."

.PHONY: version
version:									## Print some version info
	@echo $(VERSION)

.PHONY: build
build: build-c build-cli			## Build executable
	@echo "Built executable"

.PHONY: build-dirs
build-dirs:									## Create build directories
	@echo "Building executable pbwtzip. Build files will be stored in the ./build folder."
	@mkdir -p $(BLD_DIR)
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(DEP_DIR)
	@mkdir -p $(BIN_DIR)

# Build python cli
.PHONY: test-cli
test-cli:									## Run python tests
	source venv/bin/activate && \
	pytest tests/test_pbwt.py::TestPBWT::test_run_tests tests/test_cli.py

.PHONY: test-cy-cli
test-cy-cli:								## Run cython tests
	source venv/bin/activate && \
	pytest tests/test_pbwt.py::TestPBWT::test_run_test_cython

.PHONY: clean-cli
clean-cli:									## Clean python build stuff
	@rm -rf $(CURDIR)/venv
	@rm -rf $(BLD_DIR)/cpypbwt
	@rm -f $(CURDIR)/pbwt_proxy.cpython-38-x86_64-linux-gnu.so

.PHONY: build-cli
build-cli: build-c venv						## Install python dependencies
	source venv/bin/activate && \
	cd cli && \
	pip install -e . && \
	rm -rf pbwt_cli.egg-info

.PHONY: build-cy-cli
build-cy-cli: venv							## Install cython dependencies
	mkdir -p build/cpypbwt && \
	source venv/bin/activate && \
	pip install cython && \
	cd cli/cpbwt/ && \
	python setup_cython.py install && \
	cd $(CURDIR)/cli/cpbwt && \
	cp "build/lib.linux-x86_64-3.8/pbwt_proxy.cpython-38-x86_64-linux-gnu.so" $(CURDIR) && \
	mv dist build ../../build/cpypbwt

.PHONY: venv
venv:										## Create python venv
	virtualenv -p python venv

# Build c project
.PHONY: test-c
test-c: 									## Perform some tests
	@bash ./tests/test_c.sh

.PHONY: clean-c								## Clean c build stuff
clean-c:
	@rm -rf $(BLD_DIR)
	@rm -rf $(BIN_DIR)
	@rm -f $(CURDIR)/$(TARGET)

.PHONY: build-c
build-c: build-dirs $(BIN_DIR)/$(TARGET)	## Build c executable (it does not check input args, used for testing)
	@echo "Built c executable"

$(BIN_DIR)/$(TARGET): $(OBJS)				## Link
	$(CC) $(LFLAGS) -o $@ $(OBJS)
	@echo "Linking completed"

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c 				## Compile sources
	$(CC) -c $(CFLAGS) $< -o $@
	$(CC) $(INCL) -MM -MT '$(OBJ_DIR)/$*.o' $(SRC_DIR)/$*.c > $(DEP_DIR)/$*.d
	@echo "Compiled $<"

-include $(DEPS)
