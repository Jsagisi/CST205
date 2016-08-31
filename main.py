from PIL import Image
myImage = [0] * 9
#myImage = Image.open("Project1Images/1.png")
#myImage.show()
for i in range (1,9):
	myImage[i]=Image.open("Project1Images/%d.png" %i)
	myImage[i].show()
#height = image[1,9].height