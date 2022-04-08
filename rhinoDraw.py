import rhinoscriptsyntax as rs

def drawPolyLine(polyLines):
    for pl in polyLines:
        if len(pl)>2:
            rs.AddPolyline(pl)
            