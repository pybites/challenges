from PIL import Image
from os import path

import distutils.dir_util
import sys
import cv2


class Thumbler(object):
    """Thumbler class

    Scans the provided image and saves the locations of the detected faces coordinates.
    Draws squares around the detected faces.
    Extracts the detected faces into thumbnails into a folder by the same name as the image.
    """
    def __init__(self, source_image):
        self.source_image = source_image
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.image = cv2.imread(self.source_image)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.faces = self.detect_faces()
        self.found = len(self.faces)

    def detect_faces(self):
        """Using the HAAR Cascade file, it detects faces that are facing forward"""
        detected = self.face_cascade.detectMultiScale(
            self.gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30)
        )

        return detected

    def show_faces(self):
        """Draws a box around the faces that where detected"""
        # Draw a rectangle around the faces
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Faces found', self.image)
        cv2.waitKey(0)

    def extract_faces(self):
        """Extracts the faces that were found in the images"""
        if self.found:
            if '/' in self.source_image:
                face_dir = path.join('thumbs', self.source_image.split('/')[-1].split('.')[0])
            else:
                face_dir = path.join('thumbs', self.source_image.split('.')[0])
            distutils.dir_util.mkpath(face_dir)
            img = Image.open(self.source_image)
            for n, face in enumerate(self.faces):
                x, y, w, h = face
                thumb = img.crop((x, y, x+w, y+h))
                thumb.save(path.join(face_dir, f'face_{n}.jpg'))

            print(f'Found {self.found} faces!')
        else:
            print('No faces were detected!')

    def __repr__(self):
        """Simple representation of the object"""
        return f'<{__class__.__name__} image:{self.source_image} faces:{self.found}>'


def main():
    """Main entry point into the script"""
    # Get user supplied values
    if len(sys.argv) == 1:
        print('You must specify an image to process:\n')
        print('    python thumbler.py image.jpg\n')
    else:
        source_image = sys.argv[1]

        pic = Thumbler(source_image)
        pic.show_faces()
        pic.extract_faces()

if __name__ == '__main__':
    main()
