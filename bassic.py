from matplotlib import pyplot as plt
from PIL import Image
import math
path = "sampleimg.png" # Your image path
img = Image.open(path)
width, height = img.size
newimg = Image.new("RGB", (width, height), "white")
ximg = Image.new("RGB", (width, height), "white")
yimg = Image.new("RGB", (width, height), "white")
bimg = Image.open(path)
#bimg = Image.new("RGB", (width, height), "white")
for x in range(1, width-1):
# ignore the edge pixels for simplicity (1 to width-1)
    for y in range(1, height-1): # ignore edge pixels for simplicity (1 to height-1)
# initialise Gx to 0 and Gy to 0 for every pixel
        q = 0
        Gx = 0
        Gy = 0
        L  = 0
        # top left pixel
        p = img.getpixel((x-1, y-1))
        r = p[0]
        g = p[1]
        b = p[2]
        # intensity ranges from 0 to 765 (255 * 3)
        intensity = r + g + b
        # accumulate the value into Gx, and Gy
        Gx += -intensity
        Gy += -intensity
        q  +=  intensity
        #print(Gx,Gy,q)
        # remaining left column
        p = img.getpixel((x-1, y))
        r = p[0]
        g = p[1]
        b = p[2]
        Gx += -2 * (r + g + b)
        q  += 2*(r + g +b) 
        L  += -1*(r + g+ b)
        p = img.getpixel((x-1, y+1))
        r = p[0]
        g = p[1]
        q = p[2]
        Gx += -(r + g + b)
        Gy += (r + g + b)
        q  += 2*(r + g +b) 
        # middle pixels
        p = img.getpixel((x, y-1))
        r = p[0]
        g = p[1]
        b = p[2]
        Gy += -2 * (r + g + b)
        q  += 2*(r + g +b)
        L  += -1*(r + g+ b) 

        p = img.getpixel((x, y))
        r = p[0]
        g = p[1]
        b = p[2]
        q += 4*(r + g +b) 
        L += 4*(r + g+ b)
        
        p = img.getpixel((x, y+1))
        r = p[0]
        g = p[1]
        b = p[2]
        Gy += 2 * (r + g + b)
        q  += 2*(r + g +b)
        L  += -1*(r + g+ b) 
        # right column
        p = img.getpixel((x+1, y-1))
        r = p[0]
        g = p[1]
        b = p[2]
        Gx += (r + g + b)
        Gy += -(r + g + b)
        q  += (r + g +b) 
        
        p = img.getpixel((x+1, y))
        r = p[0]
        g = p[1]
        b = p[2]
        Gx += 2 * (r + g + b)
        q += 2*(r + g +b) 
        L  += -1*(r + g+ b)
        
        p = img.getpixel((x+1, y+1))
        r = p[0]
        g = p[1]
        b = p[2]
        Gx += (r + g + b)
        Gy += (r + g + b)
        q  += (r + g +b) 
        q  =(1/16)*q
        q = math.floor(q)
        # calculate the length of the gradient (Pythagorean theorem)
        length = math.sqrt((Gx * Gx) + (Gy * Gy))
        # normalise the length of gradient to the range 0 to 255
        length = length / 4328 * 255
        length = int(length)# draw the length in the edge image
        #newpixel = img.putpixel((length,length,length))
        bimg.putpixel((x,y),(q,q,q))
        ximg.putpixel((x,y),(Gx,Gx,Gx))
        yimg.putpixel((x,y),(Gy,Gy,Gy))
        newimg.putpixel((x,y),(L,L,L))
ximg.show()
yimg.show()
newimg.show()
bimg.show()