
def geneLerpPnt(p1,p2,expression,V):
    gridSize=max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))
    exp1=expression(p1[0],p1[1],p1[2])-V
    exp2=expression(p2[0],p2[1],p2[2])-V
    gx=gy=0
 
    if exp1*exp2<0:
        t=-exp1/(exp2-exp1)
        gx=(1-t)*p1[0]+t*p2[0]
        gy=(1-t)*p1[1]+t*p2[1]
    else:
        if abs(exp1)<abs(exp2):
            if p1[0]==p2[0]:
                exp11=expression(p1[0]-gridSize,p1[1],p1[2])-V
                exp12=expression(p1[0]+gridSize,p1[1],p1[2])-V
                if exp11*exp1<0:
                    t=-exp11/(exp1-exp11)
                    gx=(1-t)*(p1[0]-gridSize)+t*p1[0]
                    gy=p1[1]
                else:
                    t=-exp12/(exp1-exp12)
                    gx=(1-t)*(p1[0]+gridSize)+t*p1[0]
                    gy=p1[1]
            else:
                exp11=expression(p1[0],p1[1]-gridSize,p1[2])-V
                exp12=expression(p1[0],p1[1]+gridSize,p1[2])-V
                if exp11*exp1<0:
                    t=-exp11/(exp1-exp11)
                    gx=p1[0]
                    gy=(1-t)*(p1[1]-gridSize)+t*p1[1]
                else:
                    t=-exp12/(exp1-exp12)
                    gx=p1[0]
                    gy=(1-t)*(p1[1]+gridSize)+t*p1[1]
        else:
            if p1[0]==p2[0]:
                exp21=expression(p2[0]-gridSize,p2[1],p2[2])-V
                exp22=expression(p2[0]+gridSize,p2[1],p2[2])-V
                if exp21*exp2<0:
                    t=-exp21/(exp2-exp21)
                    gx=(1-t)*(p2[0]-gridSize)+t*p2[0]
                    gy=p2[1]
                else:
                    t=-exp22/(exp2-exp22)
                    gx=(1-t)*(p2[0]+gridSize)+t*p2[0]
                    gy=p2[1]
            else:
                exp21=expression(p2[0],p2[1]-gridSize,p2[2])-V
                exp22=expression(p2[0],p2[1]+gridSize,p2[2])-V
                if exp21*exp2<0:
                    t=-exp21/(exp2-exp21)
                    gx=p2[0]
                    gy=(1-t)*(p2[1]-gridSize)+t*p2[1]
                else:
                    t=-exp22/(exp2-exp22)
                    gx=p2[0]
                    gy=(1-t)*(p2[1]+gridSize)+t*p2[1]

            
    return([gx,gy,p1[2]])

def fitting(pntPath, expression, V):
    pathFit=[]
     
    for polyline in pntPath:
        newpath=[]
        num=len(polyline)
        if num>2:
            for i in range(1,num):
                newpath.append(geneLerpPnt(polyline[i], polyline[i-1], expression, V))
            if polyline[0]==polyline[len(polyline)-1]:
                newpath.append(newpath[0])

        if newpath:
            pathFit.append(newpath)
       
    return pathFit        