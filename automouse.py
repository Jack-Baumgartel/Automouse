import pyautogui as pya
import numpy as np

pya.FAILSAFE = True

#find screen dimensions
x,y = pya.size()

while pya.FAILSAFE == True:	
	#determine a random point on the screen
	xnew = np.random.randint(0,x)
	ynew = np.random.randint(0,y)

	#smoothly move the cursor to that point
	pya.moveTo(xnew,ynew,duration=3,tween=pya.easeInOutQuad)

	#pause
	pya.PAUSE = 5
