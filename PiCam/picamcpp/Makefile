export LIB_DIR=./lib
export LIBRARIES= -L$(LIB_DIR) -L/usr/lib/
export INCLUDE_DIR=./headers
export INCLUDES= -I/usr/include/opencv -I/usr/include/opencv -I$(INCLUDE_DIR)
export LINKS=-lopencv_calib3d -lopencv_contrib -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_gpu -lopencv_highgui -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_objdetect -lopencv_ocl -lopencv_photo -lopencv_stitching -lopencv_superres -lopencv_ts -lopencv_video -lopencv_videostab
export SRC_DIR=./src
export OBJ_DIR=./obj
export BINARY=picam

# Flags. Debug or Otimized
#export FLAGS= -ggdb -O0 -Wall -D _DEBUG
#g++ $(FLAGS) $(INCLUDES) $(LIBRARIES) -o $(BINARY) Circle.cpp Line.cpp ObjectClassifier.cpp Objects.cpp Rectangle.cpp main.cpp $(LINKS)
export FLAGS= -O3 -Wall -g

SOURCES=$(shell ls $(SRC_DIR))


all: picam
	@echo "PiCam.a created..."
	@echo "DONE."

picam:
	@echo "Build process started...";
	$(foreach source, $(SOURCES), g++ $(FLAGS) -c $(SRC_DIR)/$(source) $(INCLUDES) -o $(OBJ_DIR)/$(subst .cpp,,$(source)).o;)

	@echo "";
	ar csr $(LIB_DIR)/libpicam.a \
	$(foreach source, $(SOURCES), $(OBJ_DIR)/$(subst .cpp,,$(source)).o)

	@echo "";


$@.cpp: picam $@.cpp
	make picam
	g++ $(FLAGS) $@.cpp $(INCLUDES) $(LIBRARIES) -lpicam $(LINKS) -o picam

clean:
	rm -f $(BINARY)
	rm -rf $(BINARY).dSYM
	rm $(OBJ_DIR)/*
	rm $(LIB_DIR)/*