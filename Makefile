HAND_EVAL_DIR = lib/SKPokerEval-develop
CPPFILE = $(HAND_EVAL_DIR)/handRanker.cpp
LIBFILES = $(HAND_EVAL_DIR)/src/*.h
INCLUDES = -I /usr/include/python3.6/
EXEDIR = ./bin
EXENAME = hand_ranker
TARGET = $(EXEDIR)/$(EXENAME)
CPPFLAGS = -Wall -std=c++11

COMPILE = g++ $(INCLUDES) -o $(TARGET) $(CPPFILE) $(LIBFILES) $(CPPFLAGS)

all: $(TARGET) compile

compile: $(CPPFILE)
	mkdir -p $(EXEDIR)
	$(COMPILE)
	

clean:
	rm $(TARGET)
	rm $(HAND_EVALUATOR_DIR)/*~
