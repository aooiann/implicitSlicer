# implicitSlicer
![titleImg](img/titleImg.jpg)
implicit surface slicing for 3D printing
## Usage
You can start quickly in *line 55* in the file *main.py*
```
# MAIN ENTRANCE
allLay=makeAllLay(40,40,1,exprOperater(miniSrf, affineFun, (0.1, 0.2, 0.2),(0.5*math.pi, 0.5*math.pi, 0.33*math.pi)), 0.1, 1, 60, 1)
```
The variables in parentheses represent:
*(Canvas SizeX, Canvas SizeY, Grid Size, Implicit Equation Expression, Value of Expression, Mode, layers Count, layer Height).*
#### Expression & Affine Transformation
The *Implicit Equation Expression* participates as ***exprOperater(Expression, AffineFun, (Scale X, Scale Y, Scale Z), (Rotate Z, Rotate Y, Rotate X))***,you can create personalized patterns by changing the expression and the rotation and scaling values.
