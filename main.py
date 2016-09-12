from PIL import Image
import statistics
myImage = [0] * 9

for i in range (1,10):
	myImage[i - 1]=Image.open("Project1Images/%d.png" %i)

#prints the height of an image from the array and the width
print (myImage[0].height)
print (myImage[0].width)
newImage = Image.new("RGB", (myImage[0].width, myImage[0].height))


#Goes through each x and each y and when combined it goes through every pixel
#nested loop 
for x in range(0, myImage[0].width):
	for y in range(0, myImage[0].height):
		#Sets up red and green blue list and filling them up of the values of all the pixels
		#Empty out the list
		redPixelList = []
		greenPixelList = []
		bluePixelList = []	
		#Goes through every image and grabs the red green and blue pixel
		#and filling out the list with all the RGB values
		for thisImage in myImage:
			
			myRed, myGreen, myBlue = thisImage.getpixel((x,y))
			
			redPixelList.append(myRed)
			greenPixelList.append(myGreen)
			bluePixelList.append(myBlue)
		#Once you get the values you take the median and then
		#you put median into the new image at that pixel location.
		myTuple = (statistics.median(redPixelList), 
		statistics.median(greenPixelList),
		statistics.median(bluePixelList))
		newImage.putpixel((x, y), myTuple)

newImage.show()
		
		
#height = image[1,9].height

