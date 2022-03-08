def getTexture(fileName):
    width = 0
    height = 0
    texture = []
    with open (fileName, 'r') as f:
        allLines = f.readlines()
        for everyLine in allLines:
            width = max(width, len(everyLine))
            texture.append(everyLine)
            height+=1
    return allLines, height, width
        
class spawningPoint:
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y

def getSwordPosition(posX, posY):
    posY += 1
    posX += 4
    return posX, posY