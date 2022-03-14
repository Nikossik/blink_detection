# Blink Detection using dlib and OpenCV

![EYE](photo1.jpeg)

## **Key Points**
1. Steps involved:
    1. Localize the face in the image
    2. Extract out the eyes landmarks
    3. Calculate EAR (Eye Aspect Ratio)
    4. Determine if the person is blinking.

2. **EAR** (Eye Aspect Ratio) formula:

![EAR FORMULA](photo2.png)

    The eye aspect ratio will remain approximately constant when the eyes are open

3. The eye aspect ratio will remain approximately constant when the eyes are open
and then will rapidly approach zero during a blink, then increase again as the eye opens.

4. 68 coordinates are detected for the given face by the dlib's face detector.

5. We use coordinates only for eyes.

6. On each frame, the detector finds the eyes by coordinates and counts the EAR, after which we compare the EAR of each eye with the thrash hold and understand whether it is open or closed.
