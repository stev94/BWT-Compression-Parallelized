.DEFAULT_GOAL := help
SHELL := /bin/bash

# version
version := $(shell cat version)
VERSION ?= ${version}

# app name
TARGET = pbwtzip

# directories
SRC_DIR ?= $(CURDIR)/src/sources
HDR_DIR ?= $(CURDIR)/src/headers
BLD_DIR ?= $(CURDIR)/build
OBJ_DIR ?= $(BLD_DIR)/obj
DEP_DIR ?= $(BLD_DIR)/dep

# main files 
MAIN = $(CURDIR)/src/main.c
MAIN_O = $(OBJ_DIR)/main.o
MAIN_D = $(DEP_DIR)/main.d

# files
SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(MAIN_O) $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
DEPS := $(OBJS:$(OBJ_DIR)/%.o=$(DEP_DIR)/%.d)
INCL := -I$(CURDIR)/src/include -I$(HDR_DIR)

# C stuff
CC = gcc
CFLAGS = -Wall -Wextra -pedantic -g -O0 $(INCL)
LFLAGS = -lm -lpthread

all: build clean help

.PHONY: help
help:										## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean					
clean:										## Clean build folder
	rm -rf $(BLD_DIR) || echo "No build directory found"
	rm $(TARGET) || echo " No executable found"

.PHONY: test
test: build									## Perform some tests
	./test.sh

.PHONY: build
build: build-dirs $(TARGET) 				## Build executable
	@echo "Built executable"

.PHONY: build-dirs
build-dirs:									## Create build directories
	@echo "Building executable pbwtzip. Build files will be stored in the ./build folder."
	@mkdir -p $(BLD_DIR)
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(DEP_DIR)

$(TARGET): $(OBJS)							## Link	
	$(CC) $(LFLAGS) -o $@ $(OBJS)
	@echo "Linking completed"

-include $(DEPS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c 				## Compile sources
	$(CC) -c $(CFLAGS) $< -o $@
	$(CC) $(INCL) -MM -MT '$(OBJ_DIR)/$*.o' $(SRC_DIR)/$*.c > $(DEP_DIR)/$*.d
	@echo "Compiled $<"

$(MAIN_O): $(MAIN)							## Compile main
	$(CC) -c $(CFLAGS) $< -o $@
	$(CC) $(INCL) -MM -MT '$(MAIN_O)' $(MAIN) > $(MAIN_D)
	@echo "Compiled $<"
