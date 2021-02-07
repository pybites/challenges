from PIL import Image
import argparse
import os

if __name__ == "__main__":
    description = "Transforms each images in a folder into a thumbnail image. The images must be in png or jpg format."
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--directory', '-d', type=str, required=True)
    args = parser.parse_args()        
    
    for file in os.listdir(args.directory):
        path = os.path.join(args.directory, file)
        if file.endswith((".jpg",".png", ".jpeg")):
            image = Image.open(path)
            image.thumbnail((100, 100))
            image.save(path)