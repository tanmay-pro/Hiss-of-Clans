def getTexture(fileName):
    width = 0
    height = 0
    texture = []
    with open (fileName, 'rb') as f:
        for everyLine in f:
            width = max(width, len(everyLine))
            texture.append(everyLine)
            height+=1
    return texture, height, width
        
class spawningPoint:
    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y
