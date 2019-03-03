class board(object):
    def __init__(self,name,gravity,portalx,portaly,rightboard,upboard,leftboard,downboard,obstacles):
        obstacless=[]
        obstaclex=obstacles[::2]
        obstacley=obstacles[1::2]
        for i in range(len(obstaclex)):
            obstacless.append((obstaclex[i],obstacley[i]))
        self.name=name
        self.gravity=gravity
        self.portalx=portalx
        self.portaly=portaly
        self.rightboard=rightboard
        self.upboard=upboard
        self.leftboard=leftboard
        self.downboard=downboard
        self.obstacles=obstacless
    def __str__(self):
        return 'Board %s: Portal location: (%d,%d), Gravity: %d'%(self.name,self.portalx,self.portaly,self.gravity)\
               +'\n\tObstacles at:%s'%(self.obstacles)\
               +'\n\tPortals to: right: %s, up: %s, left: %s, down: %s'%(self.rightboard,self.upboard,self.leftboard,self.downboard)