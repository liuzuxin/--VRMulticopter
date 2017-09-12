/* Create a displacement vector to access the adjacent pixels. An
 adjacent pixel q is computed with:
 q = p + displacement
*/
// vector<Point> ObjectClassifier::create_adjacency(const int size)
// {
//     vector<Point> adjacency;

//     if (size == 4)
//     {
//         adjacency.push_back(Point(0, 0));
//         adjacency.push_back(Point(1, 0));
//         adjacency.push_back(Point(0, -1));
//         adjacency.push_back(Point(-1, 0));
//         adjacency.push_back(Point(0, 1));
//     }
//     else if (size == 8)
//     {
//         adjacency.push_back(Point(0, 0));
//         adjacency.push_back(Point(1, 0));
//         adjacency.push_back(Point(1, -1));
//         adjacency.push_back(Point(0, -1));
//         adjacency.push_back(Point(-1, -1));
//         adjacency.push_back(Point(-1, 0));
//         adjacency.push_back(Point(-1, 1));
//         adjacency.push_back(Point(0, 1));
//         adjacency.push_back(Point(1, 1));
//     }
//     else
//         cout << "Wrong adjacency size. Must be either 4 or 8" << endl;

//     return adjacency;
// }

// /*
//  Checks if a given point (probably adjacent), is inside the image.
// */
// bool ObjectClassifier::valid_point(const Mat img, const Point p)
// {
//     Rect r = Rect(0, 0, img.cols, img.rows);
//     return p.inside(r);
// }

// /* Returns if r1 intersects with r2. */
// bool ObjectClassifier::rect_intersection(Rect r1, Rect r2)
// {
//     return (r1 & r2) == r1;
// }

// int ObjectClassifier::point_to_index(const Point p1, const Size s)
// {
//     return (p1.y * s.width) + p1.x;
// }
// Point ObjectClassifier::index_to_point(const int index, const Size s)
// {
//     int x, y;
//     x = (index % (s.width * s.height)) % s.width;
//     y = (index % (s.width * s.height)) / s.width;
//     return Point(x, y);
// }

// /* Eucliean distance between two points */
// float ObjectClassifier::euclidean_distance(const Point p1, const Point p2)
// {
//     return sqrt(pow((p1.x - p2.x), 2) + pow((p1.y - p2.y), 2));
// }

// /* Computes the image histogram (used for debugging) */
// void ObjectClassifier::histogram(const Mat gray)
// {
//     float frequency[256];
//     int i, j, val;

//     for (i = 0; i < 256; i++)
//         frequency[i] = 0;

//     for (i = 0; i < gray.rows; i++)
//     {
//         for (j = 0; j < gray.cols; j++)
//         {
//             val = (int) gray.at<uchar>(i, j);
//             frequency[val]++;
//         }
//     }

//     for (i = 0; i < 256; i++)
//         cout << i << ": " << frequency[i] << "| ";
// }

// /* Normalizes the image and opens a gui to display it (used for debugging) */
// void ObjectClassifier::display(const Mat img)
// {
//     Mat tmp;
//     double min, max;
//     minMaxLoc(img, &min, &max);
//     if (min != max)
//     {
//         normalize(img, tmp, 0, 255, NORM_MINMAX, CV_8U);
//         imshow("display", tmp);
//     }
//     else
//         imshow("display", img);
//     waitKey();
// }

// /* Prints the min and max value of an Mat image (used for debugging) */
// void ObjectClassifier::print_min_max(const Mat img)
// {
//     double min, max;
//     minMaxLoc(img, &min, &max);
// }