# Blink Detection using dlib and OpenCV

![EYE](https://miro.medium.com/max/1400/1*S6XpUsffxRrSBTH6KGkJhg.jpeg)

## **Key Points**
1. Steps involved:
    1. Download [weights](https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2)
    2. Localize the face in the image
    3. Extract out the eyes landmarks
    4. Calculate EAR (Eye Aspect Ratio)
    5. Determine if the person is blinking

2. **EAR** (Eye Aspect Ratio) formula:

![EAR FORMULA](https://github.com/Practical-CV/EYE-BLINK-DETECTION-WITH-OPENCV-AND-DLIB/blob/master/media/blink_detection_equation.png?raw=true)

    The eye aspect ratio will remain approximately constant when the eyes are open

3. The eye aspect ratio will remain approximately constant when the eyes are open
and then will rapidly approach zero during a blink, then increase again as the eye opens.

4. 68 coordinates are detected for the given face by the dlib's face detector.

5. We use 12 coordinates only for eyes.

6. On each frame, the detector finds the eyes by coordinates and counts the EAR, after which we compare the EAR of each eye with the threshhold and understand whether it is open or closed.

## **Requirements**:
1. pyTelegramBotAPI==4.4.0
2. numpy==1.17.2
3. opencv-python==4.5.3.56
4. scipy==1.4.1
5. cmake==3.22.2
6. dlib==19.23.0
 
## **Tips**:
This method uses just the eye aspect ratio as the metric to determine if a person has blinked or not. However, due to noise in the video stream, subpar facial landmark detections, or fast changes in viewing angle, this approach could produce false-positive detections, reporting that a blink has taken place when in reality the person had not blinked.

### To make the algorithm work well, follow these tips:  
        1. Only for MacOS and Linux
        2. Try to record videos with good lighting!
        3. Try to keep the distance between the eyes and the camera (not too close and not too far)
