from ij.gui import Plot, Arrow
from jarray import array
from ij.io import OpenDialog
import csv
from org.apache.commons.lang import ArrayUtils;
import java.awt.Color;

scale=5

od = OpenDialog("Choose a file","")
folder = od.getDirectory()
fName = od.getFileName()
path = folder + fName
x1 = []
y1 = []
x2 = []
y2 = []
dx = []
dy = []

#Draw Circles radii 30
cx =[]
cy =[]

for x in range(-7,8,1):
	for y in range(-7,8,1):
		if ((x**2)+(y**2))<=(7.5**2):
			cx.append(x)
			cy.append(y)
			
fReader = csv.reader(open(path), delimiter=",")
for row in fReader:
	print ','.join(row)
	if row[4]!="":
		last = len(x1)-1;
		if row[0]=="":
			x1.append(x1[last])
			holderX2 = x1[last]+float(row[4])/scale
			x2.append(holderX2)
			y1.append(y1[last])
			holderY2 = y1[last]+float(row[5])/scale
			y2.append(holderY2)
		else: 
			x1.append(float(row[1]))
			holderX2 = float(row[1])+float(row[4])/scale
			x2.append(holderX2)
			y1.append(float(row[2]))
			holderY2 =float(row[2])+float(row[5])/scale
			y2.append(holderY2)
		dx.append((holderX2-x1[last+1])) 
		dy.append((holderY2-y1[last+1]))

mx1 = []
mx2 = []
my1 = []
my2 = []
for i in range(0,len(x1)):
	mx1.append(x1[i]-dx[i]/2)
	my1.append(y1[i]-dy[i]/2)
	mx2.append(x2[i]-dx[i]/2)
	my2.append(y2[i]-dy[i]/2)

#plt = Plot(fName, "degrees","degrees")
#plt.setLimits(-10,10, -10, 10)
##plt.setAxes(False,False,True, True,False, False, 1, 10);
#plt.setFrameSize(500,500);
#plt.draw()
#plt.addPoints(cx,cy,Plot.CIRCLE);
#plt.drawVectors(x1,y1,x2,y2)
#plt.show()

plt2 = Plot(fName, "degrees","degrees")
plt2.setLimits(-10,10, -10, 10)
plt2.setAxes(False,False,True, True,False, False, 1, 10);
plt2.setFrameSize(500,500);
plt2.draw()
plt2.addPoints(cx,cy,Plot.CIRCLE);
plt2.drawVectors(mx1,my1,mx2,my2)
plt2.setColor(java.awt.Color.RED)
plt2.setLineWidth(2);
plt2.addPoints(x1,y1,Plot.CIRCLE);
plt2.show()