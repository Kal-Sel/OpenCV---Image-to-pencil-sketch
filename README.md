# OpenCV-Image to pencil sketch
## Convert A Photo To Pencil Sketch Using Python In 12 Lines Of Code

In order to obtain a pencil sketch (that is, a black-and-white drawing) of the camera frame, we will make use of two image blending techniques, known as __*dodging*__ and __*burning*__. These terms refer to techniques employed during the printing process in traditional photography; photographers would manipulate the exposure time of a certain area of a darkroom print in order to lighten or darken it. _Dodging lightens an image, whereas burning darkens it_.
OpenCV does not offer a native function to implement these techniques, but with a little insight and a few tricks, we will arrive at our own efficient implementation that can be used to produce a beautiful pencil sketch effect.

If you search on the Internet, you might stumble upon the following common procedure to achieve a pencil sketch from an RGB color image:

1. Convert the color image to grayscale.

2. Invert the grayscale image to get a negative.

3. Apply a Gaussian blur to the negative from step 2.

4. Blend the grayscale image from step 1 with the blurred negative from step 3 using a color dodge.



After using this procedure, we get an output like this:


![alt text](https://github.com/Kal-Sel/OpenCV---Image-to-pencil-sketch/blob/master/Opencv.png "Coloured to pencil sketch")
