This is a collection of different Computer Vision tools for image segmentation used from various tutorials.
CANNY
This is for detecting edges using the Canny Edge Detector. “The Canny Edge detector was developed by John F. Canny in 1986. Also known to many as the optimal detector, Canny algorithm aims to satisfy three main criteria:
* Low error rate: Meaning a good detection of only existent edges.
* Good localization: The distance between edge pixels detected and real edge pixels have to be minimized.
* Minimal response: Only one detector response per edge.”    
(https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html)
As it can be seen once this program runs, the hard/dark edges within an image are turned to white and the rest of the image is turned to black. Making it much easier to distinguish objects from one another.
Grab-Cut
The grab-cut method is used to isolate an entire object out of the foreground of an image. It is very useful if something smaller needs to be extracted out of a large image to be analyzed.
(https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_grabcut/py_grabcut.html)
Hough-Transform
The Hough line transform is used for detecting lines within an image using a mathematical form. These lines can be used to detect shapes which outline objects.
(https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html)
Image Gradient
The image gradient file uses the Laplacian image filter to segment texture in an image. It does this by finding the derivative using the Sobel derivitives.
(https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_gradients/py_gradients.html) 
K-means
K-means is very popular as it follows the nearest neighbor algorithm, which identifies clusters of color within the image that is analyzed.
(https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html)
Watershed
This algorithm reduces the image to grayscale and identifies the peaks and valleys in the image by color intensity.  It also identifies the object in the foreground rather than the background which is necessary to focus.
(https://docs.opencv.org/3.3.1/d3/db4/tutorial_py_watershed.html) 
Segmentation
This folder has two different methods of segmentation that can be used with video or camera feeds. One by HSV, which stands for Hue, Saturation, and Value. This method provides the widest range of color since it is 3 dimensional in value. Another is by LAB, which is still 2D like the normal RGB color array, but it incorporates more values by giving more possibilities, like purple, yellow, and baby blue. The final file is the same as the HSV file; however, it updates the frames more often.
(https://github.com/guidefreitas/color_segmentation.git)