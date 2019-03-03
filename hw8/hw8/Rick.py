from Board import *
class Rick(object):
    def __init__(self,boardname,x0,y0,length,dx,dy,boards):
        self.boards=boards
        self.boardname=boardname
        for board in boards:
            if board.name==self.boardname:
                self.board=board
                self.board0=board
        self.tLx=x0
        self.tLy=y0
        self.tL=self.tLx, self.tLy
        self.dx=dx
        self.dy=dy
        self.length=length
    def move(self):
        self.tLx+=int(self.dx/self.board.gravity)
        self.tLy+=int(self.dy/self.board.gravity)
    def __str__(self):
        return 'Rick of %s is in %s board at (%d, %d) with speed (%.1f,%.1f)'%(self.boardname,self.board.name,self.tLx, self.tLy, self.dx,self.dy)
    def outofbound(self):
        if self.tLx<=0 or self.tLx+self.length>=1000 or self.tLy<=0 or self.tLy+self.length>=1000:
            return True
    def changeboard(self):
        if self.tLx<=0:
            for board in self.boards:
                if self.board.leftboard==board.name:
                    self.board=board
                    self.tLx=self.board.portalx
                    self.tLy=self.board.portaly
                    return 'Rick of %s moved from %s board to %s board'%(self.boardname,self.board.name,self.board.leftboard), self.tLx, self.tLy 
        elif self.tLx+self.length>=1000:
            for board in self.boards:
                if self.board.rightboard==board.name:
                    self.board=board
                    self.tLx=self.board.portalx
                    self.tLy=self.board.portaly                    
                    return 'Rick of %s moved from %s board to %s board'%(self.boardname,self.board.name,self.board.rightboard), self.tLx, self.tLy
        elif self.tLy<=0:
            for board in self.boards:
                if self.board.upboard==board.name:
                    self.board=board
                    self.tLx=self.board.portalx
                    self.tLy=self.board.portaly                    
                    return'Rick of %s moved from %s board to %s board'%(self.boardname,self.board.name,self.board.upboard), self.tLx, self.tLy
        elif self.tLy+self.length>=1000:
            for board in self.boards:
                if self.board.downboard==board.name:
                    self.board=board
                    self.tLx=self.board.portalx
                    self.tLy=self.board.portaly                    
                    return 'Rick of %s moved from %s board to %s board'%(self.boardname,self.board.name,self.board.downboard), self.tLx, self.tLy
        else:
            return False
    def crash(self):
        for i in self.board.obstacles:
            if self.tLx<=i[0]<=(self.tLx+self.length) and self.tLy<=i[1]<=(self.tLy+self.length):
                return i
        return False
    def reverse(self):
        self.dx*=-1
        self.dy*=-1
        self.dx*=0.5
    def goback(self, other):
        self.board=self.board0
        other.board=other.board0
        self.tLx=self.board0.portalx
        self.tLy=self.board0.portaly
        self.dx*=0.5
        self.dy*=0.5
        other.tLx=other.board0.portalx
        other.tLy=other.board0.portaly
        other.dx*=0.5
        other.dy*=0.5
    def meet(self, other):
        if self!=other and self.board.name==other.board.name:
            if self.tLx<=other.tLx<=self.tLx+self.length:
                if self.tLy<=other.tLy<=self.tLy+self.length:
                    return True
                if self.tLy<=other.tLy+other.length<=self.tLy+self.length:
                    return True
                if other.tLy<=self.tLy<=other.tLy+other.length:
                    return True
                if other.tLy<=self.tLy+self.length<=other.tLy+other.length:
                    return True
            if other.tLx<=self.tLx<=other.tLx+other.length:
                if self.tLy<=other.tLy<=self.tLy+self.length:
                    return True
                if self.tLy<=other.tLy+other.length<=self.tLy+self.length:
                    return True
                if other.tLy<=self.tLy<=other.tLy+other.length:
                    return True
                if other.tLy<=self.tLy+self.length<=other.tLy+other.length:
                    return True
            else:
                return False
        else:
            return False 
    def stop(self):
        magnitude=(self.dx**2+self.dy**2)**0.5
        if magnitude<=2*self.length:
            return True