import os
import sys
from PIL import Image

def resize(folder, fileName, factor):
    filePath = os.path.join(folder, fileName)
    #filePath = 'D:\\newjpegimages'
    im = Image.open(filePath)
    w, h  = im.size
    newIm = im.resize((int(w*factor), int(h*factor)))
    # i am saving a copy, overrider original, or save to other folder
    newIm.save(filePath+"new.png")

def bulkResize(imageFolder, factor):
    imgExts = ["png", "bmp", "jpg"]       #Type if images source directory can have
    for path, dirs, files in os.walk(imageFolder):
        for fileName in files:
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName, factor)

if __name__ == "__main__":
    imageFolder='D:\\sampleimage' #path to image folder
    resizeFactor=float(30)/100.0 #resizing by a specific factor
    bulkResize(imageFolder, resizeFactor)
