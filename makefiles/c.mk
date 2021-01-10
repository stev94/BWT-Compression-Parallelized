# app name
TARGET = cpbwt

# directories
SRC_DIR ?= $(CURDIR)/src/sources
HDR_DIR ?= $(CURDIR)/src/headers
BLD_DIR ?= $(CURDIR)/build
OBJ_DIR ?= $(BLD_DIR)/obj
DEP_DIR ?= $(BLD_DIR)/dep

# files
SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)
DEPS := $(OBJS:$(OBJ_DIR)/%.o=$(DEP_DIR)/%.d)
INCL := -I$(CURDIR)/src/include -I$(HDR_DIR)

# C stuff
CC = gcc
CFLAGS = -Wall -Wextra -pedantic -g -O0 $(INCL)
LFLAGS = -lpthread -lm


.PHONY: test-c
test-c: 									## Perform some tests
	@bash ./tests/test_c.sh

.PHONY: clean-c								## Clean c build stuff
clean-c:
	@rm -rf $(BLD_DIR)
	@rm -f $(CURDIR)/$(TARGET)

.PHONY: build-c
build-c: build-dirs $(CURDIR)/$(TARGET)		## Build c executable (it does not check input args, used for testing)
	@echo "Built c executable"

.PHONY: build-dirs
build-dirs:									## Create build directories
	@echo "Building executable pbwtzip. Build files will be stored in the ./build folder."
	@mkdir -p $(BLD_DIR)
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(DEP_DIR)

$(CURDIR)/$(TARGET): $(OBJS)				## Link
	$(CC) -o $@ $(OBJS) $(LFLAGS)
	@echo "Linking completed"

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c 				## Compile sources
	$(CC) -c $(CFLAGS) $< -o $@
	$(CC) $(INCL) -MM -MT '$(OBJ_DIR)/$*.o' $(SRC_DIR)/$*.c > $(DEP_DIR)/$*.d
	@echo "Compiled $<"

-include $(DEPS)
