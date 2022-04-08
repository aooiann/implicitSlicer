'''
@author:shaojiayan
@lastEditTime:2022-04-08 13:49
@version:1.0
------------------------------

'''


import traceOP
import fitOP
import rhinoDraw
import gcodeOut
import math
from exprHouse import *


def makeLay(rangeX, rangeY, z, gridSize, expression, V, mode):
    listLine=[]
    pntTrace=[]
    # GENERATE SHORT LINES
    for x in range(-rangeX,rangeX,gridSize):
        for y in range(-rangeY,rangeY,gridSize):
            exp1=expression(x+0.5*gridSize, y+0.5*gridSize, z)
            exp2=expression(x+0.5*gridSize, y-0.5*gridSize, z)
            exp3=expression(x-0.5*gridSize, y+0.5*gridSize, z)
            if (exp1-V)*(exp2-V)<0:
                listLine.append([[x,y,z],[x+gridSize,y,z]])
            if (exp1-V)*(exp3-V)<0:
                listLine.append([[x,y,z],[x,y+gridSize,z]])

    # FIND TRACE BY MODE
    if listLine:
        pntTrace=traceOP.trace(listLine)
        if mode==0:
            return pntTrace
        elif mode==1:
            pathFit=fitOP.fitting(pntTrace,expression,V)
            return pathFit
        else:
            print("Can't draw by this mode")
            return None

def makeAllLay(rangeX, rangeY, gridSize, expression, V, mode, layCount, lh):
    allLayers=[]
    for i in range(layCount):
        path=makeLay(rangeX, rangeY, i*lh, gridSize, expression, V, mode)
        if path:
            allLayers.append(path)
            rhinoDraw.drawPolyLine(path)
    
    return allLayers

# MAIN ENTRANCE
allLay=makeAllLay(40,40,1,exprOperater(miniSrf, affineFun, (0.1, 0.2, 0.2),(0.5*math.pi, 0.5*math.pi, 0.33*math.pi)), 0.1, 1, 60, 1)
# gcodeOut.writeGcodeBody(allLay,100.0,0.1,0.2)

