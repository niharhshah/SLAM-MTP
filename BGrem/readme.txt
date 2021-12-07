# Removing background from object images
Using structured edge detection on the image we create a thresholded image on which we find the contours. The area of bounding boxes of each contour is calculated and the contour corresponding to max area is picked.The image is cropped according to this bounding box. Then the same process is repeated with the cropped image. This time the area of the contours are calculated and max area contour is taken. Mask is created with this contour as boundary and we get the final output.

Requirements :
1)The model.yml file used for structured edge detection used in the code can be found at https://github.com/opencv/opencv_extra/blob/master/testdata/cv/ximgproc/model.yml.gz

2)Use the “opencv-contrib-python” library instead of “opencv-python”
