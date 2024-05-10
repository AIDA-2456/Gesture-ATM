import cv2
from config import cfg
import mediapipe as mp
from drawpage import DrawPage
from detectclick import DetectClick
import datetime
from facerec import FaceRec


def main():
    # For webcam input.
    cap = cv2.VideoCapture(0)

    # Set the window size as per the configuration
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cfg["screen_x"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg["screen_y"])

    # Initialise the class draw page with info of all the pages we're going to show
    dwPg = DrawPage(cfg["pages"])

    # Get coordinates of buttons and other shapes we're going to draw on screen
    coords = dwPg.getCoordintates()

    # coords is a list of tuples where last element is center of a circle on screen
    detClick = DetectClick([s[-1] for s in coords])

    # Iniitalise the face recognition class and the face detection classifier
    facerec = FaceRec()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialise hand detection model
    mp_hands = mp.solutions.hands.Hands(
        min_detection_confidence = cfg["min_detection_confidence"],
        min_tracking_confidence = cfg["min_tracking_confidence"],
        max_num_hands = cfg["max_num_hands"]
    )

    with mp_hands as hands:

        while cap.isOpened():
            success, image = cap.read()
            if not success:
              print("Ignoring empty camera frame.")
              # If loading a video, use 'break' instead of 'continue'.
              break
            # Flip the image to make it mirror like and intuitive.
            # We use one image to draw and other to detect hands.
            overlay = cv2.flip(image, 1).copy()
            output = cv2.flip(image, 1).copy()
            # Try to match face only when Match button is clicked.
            if (("face_matched" in cfg and not cfg["face_matched"]) or "face_matched" not in cfg) and cfg["currentpage"] == "Match":
                gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.05, 5)
                cfg["face_matched"] = facerec.MatchTheFace(image) if len(faces) >= 1 else False
                cfg["currentpage"] = "Transactions" if cfg["face_matched"] == True else "FaceRec"


            # Draw the buttons as per the current page to be shown to customer.
            dwPg.drawThePage(cfg["currentpage"], overlay)

            # Converting the image and making it non-writable for better performance.
            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            output.flags.writeable = False

            # Processing the image to be able to detect hands in it if any.
            results = hands.process(output)

            # Reversing the color conversion and making image writable.
            output.flags.writeable = True
            output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

            if results and results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]

                imgH, imgW, imgC = output.shape

                # Get position of the fingertip in form of pixels.
                xpos, ypos = int(hand.landmark[8].x * imgW), int(hand.landmark[8].y * imgH)

                # Draw a circle around the fingertip to make it more visible while being tracked.
                cv2.circle(overlay, (xpos, ypos), 20, (255, 0, 255), cv2.FILLED)

                # Detect if the fingertip has clicked any button or not.
                clickedBtnIndex = detClick.detectClick((xpos, ypos))

                if clickedBtnIndex != None and clickedBtnIndex>-1 and clickedBtnIndex <8:
                    # endtime is timestamp till which the fingertip needs to be on a button for it to qualify as a click.

                    # Calculate the endtime if not already calculated.
                    if "endtime" not in cfg:
                        cfg["endtime"] = datetime.datetime.now() + datetime.timedelta(seconds=cfg["btnClickDelay"])
                        cfg["endtime"] = cfg["endtime"].strftime("%H:%M:%S.%f")[:-5]

                    # After some seconds, check if the fingertip is still on button. If yes, then navigate.
                    elif cfg["endtime"] <= datetime.datetime.now().strftime("%H:%M:%S.%f")[:-5]:
                        cPage = cfg["currentpage"]
                        cfg["currentpage"] = cfg["pages"][cPage]["navigation"][clickedBtnIndex]
                        del cfg["endtime"]

                elif clickedBtnIndex == None and "endtime" in cfg:
                    if "face_matched" in cfg:
                        del cfg["face_matched"]
                    del cfg["endtime"]

            # After all the drawing and hand tracking, put both images on top of each other.
            alpha = cfg["alpha"]
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

            # Show the image in window.
            cv2.imshow("Bio-Metric transaction control ATM", output)

            # Stop running the code when Escape key is pressed or if any Exit option is chosen.
            if cv2.waitKey(5) & 0xFF == 27 or cfg["currentpage"] == "Exit":
                break

    cap.release()


if __name__ == "__main__":
    main()
