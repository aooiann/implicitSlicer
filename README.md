# implicitSlicer
![titleImg](img/titleImg.jpg)
implicit surface slicing for 3D printing
## Usage
You can start quickly in *line 55* in the file *main.py*
```
# MAIN ENTRANCE
allLay=makeAllLay(40,40,1,exprOperater(miniSrf, affineFun, (0.1, 0.2, 0.2),(0.5*math.pi, 0.5*math.pi, 0.33*math.pi)), 0.1, 1, 60, 1)
gcodeOut.writeGcodeBody(allLay,100.0,0.1,0.2)
```
The variables in parentheses represent:
*(Canvas SizeX, Canvas SizeY, Grid Size, Implicit Equation Expression, Value of Expression, Mode, Layers Count, Layer Height).*

### Display Platform
I use *Rhinoceros* platform to display the graphics generated.And you can disable the rhinoceros functions by annotating *line 50* in the file *main.py*.

### Drawing Mode
You can change the way the expression be drawn by changing the value of mode(0 or 1). ***"0"*** means draw with zigzag lines, ***"1"*** means draw with smooth lines.Look at the following two examples:
![minisrf_mode0](img/minisrf_mode0.png)
*Mode"0"*
![minisrf_mode1](img/minisrf_mode1.png)
*Mode"1"*

### Expression & Affine Transformation
The *Implicit Equation Expression* participates as ***exprOperater(Expression, AffineFun, (Scale X, Scale Y, Scale Z), (Rotate Z, Rotate Y, Rotate X))***,you can create personalized patterns by changing the expression and the rotation and scaling values.Also,look at the following examples:
![minisrf_scale](img/minisrf_scale.png)
*Same expression different scaling value*
![minisrf_rotate](img/minisrf_rotate.png)
*Same expression different rotation value*
![minisrf_free](img/minisrf_free.png)
*Same expression different scaling & rotation value*
![schwarzP](img/schwarzP.png)
*Different expression*

### G-code Output
Based on the previously generated graphics, you can use the ***writeGcodeBody(allLays, origOffset, fr, raiseheight)*** method in *gcodeOut.py* to export the G-code for 3D printing.*origOffset* will be half the width of your printer, *fr* represents how far the first layer will be raised, and *raiseheight* represents how far the printhead will be raised at the end of one path to ensure not hit the printed material when it starts printing the next path.
![gcodeOutput](img/gcodeOutput.png)
*Preview the print path*
![3DprintingModel](img/3DprintingModel.jpg)
*One of my printouts*

### Now, start generating your personalized graphics and print them out!  
![personalizedPattern](img/personalizedPattern.jpg)
