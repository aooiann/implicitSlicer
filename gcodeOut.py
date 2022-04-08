def dist(p1,p2):
    xt=p2[0]-p1[0]
    yt=p2[1]-p1[1]
    zt=p2[2]-p1[2]
    d=(xt**2+yt**2+zt**2)**0.5
    return(d)

def calExtru(p1,p2):
    pointDist=dist(p1,p2)*0.035
    el=round(pointDist,4)
    return el


def writeGcodeBody(allLays, origOffset, fr, raiseheight):
    doc=open('testGcode.txt','w+')
    for lay in allLays:      
        if lay:
            for i in range(len(lay)): 
                s0="G0 F1200 X"+str(round(lay[i][0][0]+origOffset,2))+" Y"+str(round(lay[i][0][1]+origOffset,2))+" Z"+str(round(lay[i][0][2]+fr,2))
                doc.write(s0+'\n')
                for k in range(1,len(lay[i])):
                    sk="G1 F800 X"+str(round(lay[i][k][0]+origOffset,2))+" Y"+str(round(lay[i][k][1]+origOffset,2))+" Z"+str(round(lay[i][k][2]+fr,2))+" E"+str(calExtru(lay[i][k],lay[i][k-1]))
                    doc.write(sk+'\n')  
                sLast="G0 F1200 X"+str(round(lay[i][len(lay[i])-1][0]+origOffset,2))+" Y"+str(round(lay[i][len(lay[i])-1][1]+origOffset,2))+" Z"+str(round(lay[i][len(lay[i])-1][2]+raiseheight+fr,2))
                doc.write(sLast+'\n')
    doc.close()
