import math


def affineFun(scaleZ,scaleY,scaleX,rZ,rY,rX,x,y,z):
    rMX=[math.cos(rZ)*math.cos(rY), math.sin(rZ)*math.cos(rX)+math.cos(rZ)*math.sin(rY)*math.sin(rX), math.sin(rZ)*math.sin(rX)-math.cos(rZ)*math.sin(rY)*math.cos(rX)]
    rMY=[-math.sin(rZ)*math.cos(rY), math.cos(rZ)*math.cos(rX)-math.sin(rY)*math.sin(rZ)*math.sin(rX), math.cos(rZ)*math.sin(rX)+math.sin(rY)*math.sin(rZ)*math.cos(rX)]
    rMZ=[math.sin(rY), -math.cos(rY)*math.sin(rX), math.cos(rY)*math.cos(rX)]
    tx=(scaleX*rMX[0]*x+scaleX*rMX[1]*y+scaleX*rMX[2]*z)
    ty=(scaleY*rMY[0]*x+scaleY*rMY[1]*y+scaleY*rMY[2]*z)
    tz=(scaleZ*rMZ[0]*x+scaleZ*rMZ[1]*y+scaleZ*rMZ[2]*z)
    
    return tx,ty,tz



def exprOperater(expression, affineFun, scale, rotate):
    scaleZ,scaleY,scaleX = scale
    rZ,rY,rX = rotate
    return lambda x, y, z: expression(*affineFun(scaleZ,scaleY,scaleX, rZ,rY,rX, x, y, z))


def miniSrf(x,y,z):
    return math.cos(x)*math.sin(y)+math.cos(y)*math.sin(z)+math.cos(z)*math.sin(x)

def ellipse(x,y,z):
    return x**2+y**2+z**2

def hyperbola(x,y,z):
    return x**2-y**2+z**2

def Neovius_mS(x,y,z):
    return 3*(math.cos(x)+math.cos(y)+math.cos(z))+4*math.cos(x)*math.cos(y)*math.cos(z)
        
def SchwarzP(x,y,z):
    return math.cos(x)+math.cos(z)+math.cos(y)
