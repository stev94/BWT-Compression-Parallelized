.DEFAULT_GOAL := help
SHELL := /bin/bash
THIS_FILE := $(firstword $(MAKEFILE_LIST))
THIS_FOLDER := $(shell basename $(CURDIR))

master_version := $$(git show master:cli/version.py | grep __version__ | awk -F= '{print $$2}' | awk -F\' '{print $$2}')
this_branch := $(shell git rev-parse --abbrev-ref HEAD)

# version
this_version := $(shell cat cli/version.py | grep __version__ | awk 'BEGIN {FS = " = "}; {print substr($$2, 2, length($$2)-2)}')
VERSION ?= ${version}

include makefiles/*

all: build clean help version start-dev-env clean-dev-env

.PHONY: help
help:										## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$'  $(MAKEFILE_LIST) | sort | awk -F: '{printf "%s: %s\n", $$2, $$3}' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: clean-c clean-cli					## Clean builds folder
	@echo "Everything cleaned."

.PHONY: version
version:    					## Print some version info
	@echo -e "\033[0;32m$(TARGET):\033[0m current: \033[0;34m$(this_version)\033[0m master: \033[0;36m$(master_version)\033[0m"

.PHONY: build
build: build-c build-cli					## Build executable
	@echo "Built executable"

.PHONY: start-dev-env
start-dev-env: build-c cli-dependencies		## Install python dependencies
	@echo "Dev environment built."

.PHONY: clean-dev-env
clean-dev-env: clean-c						## Clean dev environemnt
	@rm -rf $(CURDIR)/venv

.PHONY: build-cli
build-cli: cli-dependencies	build-c			## Build PBWT cli
	source venv/bin/activate && \
	cd cli && \
	pyinstaller --clean --onefile pbwt.py && \
	echo "Installation successfully ended. Cleaning up" && \
	mv dist/pbwt $(CURDIR) && \
	rm -rf build && \
	rm -rf dist && \
	rm -f pbwt.spec && \
	chmod 755 $(CURDIR)/pbwt && \
	echo "Everything setup. You can use the app by typing ./pbwt"
