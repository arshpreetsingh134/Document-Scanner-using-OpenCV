# Document-Scanner-using-OpenCV
I have used **OpenCV2** framework for Computer Vision features such as- Edge Detection, Contour Plotting, Perspective Transform, etc. to build this application.

The application was completed in 4 easy steps :-
1. **Step 1:** Edge Detection using _Gaussian Blur_ and _Canny Algorithm._
2. **Step 2:** Using edges to find contours (outline) of the piece of paper being scanned.
3. **Step 3:** Applying _Perspective Transform_ (aka, "Bird's-Eye View") to obtain a top-down view of the document.
4. **Step 4:** Converting to Grayscale and applying _Threshold_ to give the document a "paper-like" feel.
</br>
- The first script file, [perspectiveTransform.py](https://github.com/arshpreetsingh134/Document-Scanner-using-OpenCV/blob/master/perspectiveTransform.py) performs a 4-point perspective transform on the image.

- The second script file, [scan_doc.py](https://github.com/arshpreetsingh134/Document-Scanner-using-OpenCV/blob/master/scan_doc.py) contains the core functionality.

- Moreover, I have used the utility module *imutils*, which contains convenience functions for resizing, rotating, and cropping images.

</br>

## Here are some bills I tested my application on :-
### Test Image (1) :
<img src = "https://github.com/arshpreetsingh134/Document-Scanner-using-OpenCV/blob/master/images/test_image.jpg" height=650>
</br>

### Scanned Image :
![Output 1](https://github.com/arshpreetsingh134/Document-Scanner-using-OpenCV/blob/master/images/output_01.jpg)

</br>
</br>
</br>

### Test Image (2) :
<img src = "https://github.com/arshpreetsingh134/Document-Scanner-using-OpenCV/blob/master/images/test_image02.jpg" height=650>
</br>

### Scanned Image :
![Output 1](https://github.com/arshpreetsingh134/Document-Scanner-using-OpenCV/blob/master/images/output_02.jpg)
