import face_recognition
import os
from config import cfg


class FaceRec():

    def __init__(self, facespath = "C:/Users/Dell/Downloads/Gesture-Based-Touchless-ATM-main/Gesture-Based-Touchless-ATM-main/Faces"):
        self.faces = []
        # Store encodings of all the pictures from our database in memory.
        for file in os.listdir(facespath):
            if file.endswith(".jpeg") or file.endswith(".jpg"):
                img = face_recognition.load_image_file(os.path.join(facespath, file))
                self.faces.append(face_recognition.face_encodings(img)[0])


    def MatchTheFace(self, img):
        # Get encodings of the image/frame from the camera.
        encodings = face_recognition.face_encodings(img)

        # If encoding of any face is present then get it, else say no face matched.
        if len(encodings) > 0:
            encodings = encodings[0]
        else:
            return False

        comparisons = face_recognition.compare_faces(self.faces, encodings, tolerance=cfg["tolerance"])

        # Return true only if at least one of the face matches in database matches wit clicked picture.
        return True if any(comparisons) else False
