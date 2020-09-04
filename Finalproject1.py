import cv2
import pandas as pd

#reading an image
image=cv2.imread("colortrial.jpg")


#declaring global variable
clicked=False
r=g=b=xpos=ypos=0

#reading file using pandas
index=["color","color_name","hex","R","G","B"]
csv=pd.read_csv("colors.csv",names=index,header=None)

#function to calculate minimum distance from all colors
def getcolorname(R,G,B):

    minimum=10000
    for i in range(len(csv)):
        d=abs(R-int(csv.loc[i,"R"]))+abs(G-int(csv.loc[i,"G"])) + abs(B-int(csv.loc[i,"B"]))
        if (d<=minimum):
            minimum=d
            cname=csv.loc[i,"color_name"]
    return cname

#function to get x,y cordinates
def draw_func(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked=True
        xpos=x
        ypos=y
        b,g,r=image[y,x]
        b=int(b)
        g=int(g)
        r=int(r)

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_func)

while(1):
    cv2.imshow("image",image)

    if(clicked):

        cv2.rectangle(image,(20,20),(750,60),(b,g,r),-1)

        text=getcolorname(r,g,b)+" "  "R:" + str(r) + " " + "G:" + str(g) +" " + "B:" + str(b)

        cv2.putText(image,text,(50,50),4,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(image,text,(50,50),4,0.8,(0,0,0),2,cv2.LINE_AA)

        clicked=False

    if cv2.waitKey(20) & 0xFF==27:
        break

cv2.destroyAllWindows()



