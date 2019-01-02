from tkinter import *
import tkinter.filedialog
import tkinter.messagebox as tmb
from PIL import ImageTk, Image
from tkinter.colorchooser import *

pm = __import__('2_image')

root = Tk()
root.title("ASCII Image Generator")
#root.geometry("1366x768")

frame = Frame(root)

#Some Global Variables
imgFile = '' #Stores the object to the image file
columns = IntVar() #stores the number of columns of alphabets, our final ASCII image will have
scale = 0.43 #Scaling factor for our image
moreLevels = BooleanVar()
textColor = ((0.0, 0.0, 0.0), '#000000')
backgroundColor = ((255.99609375, 255.99609375, 255.99609375), '#ffffff')
pathStore = ''

def findImage():
    """
    function to find the image path on the computer
    """
    global imgFile
    filename = tkinter.filedialog.askopenfilename()
    if filename == '':
        return
    imgFile = Image.open(filename)
    w, h = int(imgFile.size[0] / 10), int(imgFile.size[1] / 10)
    resized = imgFile.resize((w, h), Image.ANTIALIAS)
    img.dispImg = ImageTk.PhotoImage(resized)
    img.config(width=w, height=h)
    img.create_image((0, 0), image=img.dispImg, anchor="nw")
    print(filename)
    imgFile = filename

def getTextColor(event):
    global textColor
    temp = askcolor()
    if temp[1] != None:
        textColor = temp
    tColorDisp.config(bg=textColor[1])
    print(textColor)

def getBackgroundColor(event):
    global backgroundColor
    temp = askcolor()
    if temp[1] != None:
        backgroundColor = temp
    bColorDisp.config(bg=backgroundColor[1])
    print(backgroundColor)

def findPath():
    global pathStore
    temp = tkinter.filedialog.askdirectory()
    if temp != '':
        pathStore = temp
    path.config(text=pathStore)

def genarate():
    """
    Function will generate our ASCII image, taking in account, the details provided
    """
    if imgFile == '':
        tmb.showwarning(title="No Image!", message="Select an Image!")
        return
    if pathStore == '':
        tmb.showwarning(title="No Path!", message="Select a Destination Folder!")
        return
    print(columns.get())
    print(moreLevels.get())
    pm.main(imgFile, columns.get(), scale, moreLevels.get(), textColor, backgroundColor, pathStore)

Label(root, text='ASCII Image Generator').grid(row=1, column=1, columnspan=2, sticky='e' + 'w')

img = Canvas(root, width=0, height=0)
img.grid(row=2, column=2, rowspan=3, sticky='e' + 'w', padx=20, pady=5)

find = Button(root, text="Find Image", command=findImage)
find.grid(row=2, column=1, sticky='e' + 'w', padx=20, pady=5)

cols = Scale(root, label="Select Columns:", variable=columns, from_=50, to=600, orient=HORIZONTAL)
cols.grid(row=3, column=1, sticky='e' + 'w', padx=20, pady=5)

levels = Checkbutton(root, text="Use More Levels", variable=moreLevels)
levels.grid(row=4, column=1, sticky='e' + 'w', padx=20, pady=5)

tcolor = Label(text='Text Color: ')
tcolor.grid(row=5, column=1, sticky='w', padx=20, pady=5)

tColorDisp = Label(root, bg='black', text='     ')
tColorDisp.grid(row=5, column=2, sticky='w', padx=20, pady=5)
tColorDisp.bind('<Button-1>', getTextColor)

bcolor = Label(text='Background Color: ')
bcolor.grid(row=6, column=1, sticky='w', padx=20, pady=5)

bColorDisp = Label(root, bg='white', text='     ')
bColorDisp.bind('<Button-1>', getBackgroundColor)
bColorDisp.grid(row=6, column=2, sticky='w', padx=20, pady=5)

dest = Button(root, text='Destination folder:',command=findPath)
dest.grid(row=7, column=1, sticky='e' + 'w', padx=20, pady=5)
path = Label(text='')
path.grid(row=7, column=2, sticky='w', padx=20, pady=5)

gen = Button(root, text="Generate ASCII Image", command=genarate)
gen.grid(row=8, column=1, sticky='e' + 'w', padx=20, pady=5, columnspan=2)

root.mainloop()
