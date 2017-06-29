from PIL import Image


myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []


#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    avg = (red + green + blue)//3
    
    newRed = avg
    if newRed > 255:
        newRed = 255
        
    newGreen = avg 
    if newGreen > 255:
        newGreen = 255
        
    newBlue = avg
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)
    




#add pixel to new pixel

    newPixelList.append(p)


#open the image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixelList)
newImage.show()
