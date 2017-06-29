from PIL import Image


#FUNCTIONS

def negative(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    
    newRed = 255 - red
    if newRed > 255:
        newRed = 255
        
    newGreen = 255 - green 
    if newGreen > 255:
        newGreen = 255
        
    newBlue = 255 - blue
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)


def overExpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    
    newRed = red*2
    if newRed > 255:
        newRed = 255
        
    newGreen = green*2
    if newGreen > 255:
        newGreen = 255
        
    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)

    newPixelList.append(p)

#RUNNING CODE        

myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
halfway = length//2

counter = 0


for pixel in pixelList:

#pixel manipulation
    if (counter < halfway): #this is the top half of the photo
        overExpose(pixel)
        
    else: #this is the bottom half of the photo
        negative(pixel)
    counter = counter + 1
    
##    red = pixel[0]
##    green = pixel[1]
##    blue = pixel[2]
##
###New Red Green Blue 
##    
##    newRed = 255 - red
##    if newRed > 255:
##        newRed = 255
##        
##    newGreen = 255 - green 
##    if newGreen > 255:
##        newGreen = 255
##        
##    newBlue = 255 - blue
##    if newBlue > 255:
##        newBlue = 255
##
##    p = (newRed,newGreen,newBlue)
##    










#add pixel to new pixel



#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
