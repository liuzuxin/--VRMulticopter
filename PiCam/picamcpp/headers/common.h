// //
// //  ObjectClassifier.h
// //  ocv-drawingclassifier
// //
// //  Created by Nikolas Moya on 2/28/15.
// //  Copyright (c) 2015 Nikolas Moya. All rights reserved.
// //


// #include <iostream>
// #include <queue>
// #include <list>
// #include <opencv2/imgproc/imgproc.hpp>
// #include <opencv2/highgui/highgui.hpp>
// #include "Objects.h"

// //#import <UIKit/UIKit.h>


// /* This is the most important class. It is the wrapper of opencv library.
//  The main interface is classify_objects(). Other methods are dependencies from
//  the classify_objects() method or auxiliary methods to ease the classification.
//  I will briefly describe each method in the ObjectClassifier.cpp file.
// */

// class MyContour{
// public:
//     cv::Rect  bbox;
//     std::vector<cv::Point> elements;
// public:
//     MyContour(){};
//     ~MyContour(){this->elements.clear();}
// };


// class ObjectClassifier {
// private:
//     cv::Mat src;
    
// public:
//     ObjectClassifier(cv::Mat src);
//     ~ObjectClassifier();
    
//     Objects classify_objects();
    
//     std::vector<cv::Point> create_adjacency(const int size);
//     cv::Mat euclidean_distance_transform(const cv::Mat binary, const int adjacency_size);
//     std::vector<MyContour> connected_components(const cv::Mat binary, const int adjacency_size);
    
//     cv::Mat create_white_image(const cv::Size s);
//     cv::Mat close_drawing_gaps(const cv::Mat src_binary);
//     cv::Mat thin_contours(const cv::Mat src_gray);
    
//     void draw_points(cv::Mat img, const std::vector<cv::Point> vec);
//     void detect_circles(const cv::Mat src, int *number_of_circles, cv::Point *center, int *radius);
//     void detect_lines(const cv::Mat src, MyContour contour, float classification_measure, int *number_of_lines, cv::Point *start, cv::Point *end);
//     float euclidean_distance(const cv::Point p1, const cv::Point p2);
//     bool valid_point(const cv::Mat img, const cv::Point p);
//     bool rect_intersection(const cv::Rect r1, const cv::Rect r2);
//     float bbox_distance_measure(const cv::Mat edt);
//     int point_to_index(const cv::Point p1, const cv::Size s);
//     cv::Point index_to_point(const int index, const cv::Size s);
//     void histogram(const cv::Mat gray);
//     void print_min_max(const cv::Mat img);
//     void display(const cv::Mat img);
    
// };


// #endif /* defined(__ocv_drawingclassifier__ObjectClassifier__) */






