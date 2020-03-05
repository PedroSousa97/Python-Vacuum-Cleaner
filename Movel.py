from graphics import *


class Movel:
    #Função para criar móvel retangular
    def __init__(self,x1,x2,y1,y2):
        self.movelrect = Rectangle(Point(x1,y1),Point(x2,y2))               #Criação de móveis retangulares através das variáveis passadas para o construtor
        self.movelrect.setFill(color_rgb(60,60,60))
        self.movelrect.setOutline(color_rgb(0,0,0))
        self.movelrect.setWidth(2)
        self.movelcirc=Circle(Point((x1+x2)/2,(y1+y2)/2),abs((x1-x2)/2))
        self.movelcirc.setFill(color_rgb(60,60,60))
        self.movelcirc.setOutline(color_rgb(0,0,0))
        self.movelcirc.setWidth(2)
        self.x1=x1       #Valor mínimo de X do móvel
        self.x2=x2       #Valor máximo de X do móvel
        self.y1=y1       #Valor mínimo de Y do móvel
        self.y2=y2       #Valor máximo de Y do móvel
    def criaSofa(self,win):
        self.movelrect.draw(win)    #Desenha movel retangular no ecrã
    def criaMesa(self,win):
        self.movelcirc.draw(win)    #Desenha movel redondo no ecrã
   