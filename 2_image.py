import numpy as np
from PIL import Image

pm = __import__('11_text_to_image')

# 70 levels of gray
grayScale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
grayScale2 = '@%#*+=-:. '

def getAverageL(image):
    """
    Given PIL Image, returns the average value of gray scale value
    """
    # get image as numpy array
    img = np.array(image)
    # get the dimensions
    w, h = img.shape
    # get the average
    return np.average(img.reshape(w*h))

def covertImageToASCII(fileName, cols, scale, moreLevels):
    """
    Given Image and dimensions (rows, cols), returns an m*n list of Images
    """
    # declare globals
    global grayScale1, grayScale2
    # open image and convert to gray scale
    image = Image.open(fileName).convert('L')
    # store the image dimensions
    wImage, hImage = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (wImage, hImage))
    # compute tile width
    wTile = wImage/cols
    # compute tile height based on the aspect ratio and scale of the font
    hTile = wTile/scale
    # compute number of rows to use in the final grid
    rows = int(hImage/hTile)
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (wTile, hTile))
    # check if image size is too small
    if cols > wImage or rows > hImage:
        print("Image too small for specified cols!")
        exit(0)
    # an ASCII image is a list of character strings
    asciiImage = []
    # generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j * hTile)
        y2 = int((j + 1) * hTile)
        # correct the last tile
        if j == rows - 1:
            y2 = hImage
        # append an empty string
        asciiImage.append("")
        for i in range(cols):
            # crop the image to fit the tile
            x1 = int(i * wTile)
            x2 = int((i + 1) * wTile)
            # correct the last tile
            if i == cols - 1:
                x2 = wImage
            # crop the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))
            # get the average luminance
            avg = int(getAverageL(img))
            # look up the ASCII character for grayscale value (avg)
            if moreLevels:
                gsval = grayScale1[int((avg * 69) / 255)]
            else:
                gsval = grayScale2[int((avg * 9) / 255)]
            # append the ASCII character to the string
            asciiImage[j] += gsval
    # return text image
    return asciiImage

# main() function
def main(imgFile, columns, scale, moreLevels, textColor, backgroundColor, pathStore):
    # set output file
    outFile = '/out.txt'
    # convert image to ASCII text
    asciiImage = covertImageToASCII(imgFile, columns, scale, moreLevels)
    # open a new text file
    f = open(pathStore + outFile, 'w')
    # write each string in the list to the new file
    for row in asciiImage:
        f.write(row + '\n')
    # clean up
    f.close()
    pm.main(textColor[1], backgroundColor[1], pathStore)
    print("ASCII art written to %s" % outFile)
