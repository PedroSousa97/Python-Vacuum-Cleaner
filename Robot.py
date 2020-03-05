from graphics import *
from Functions import *

class Robot:

    def __init__(self, win, x, y):
        """win is the GraphWin to display the shot, angle, velocity, and
        height are initial projectile parameters.
        """
        self.walle = Circle(Point(x,y), 20)             #Representação do aspirador utilizando uma circunferência
        self.walle.setFill(color_rgb(172,172,172))
        self.walle.setOutline(color_rgb(0,0,0))
        self.walle.draw(win)
        self.battery = Rectangle(Point(x,y),Point(x+5,y+5))  #Representação da Luz de bateria utilizando um quadradro em cima do robo, com o mesmo ponto de ancoragem
        self.battery.setOutline(color_rgb(0,0,0))            #x+5 e y+5 representão a dimensão de 5px para cada lado do quadrado
        self.battery.setFill(color_rgb(0,223,82))
        self.battery.draw(win)
        self.xpos = self.walle.getCenter().getX()            #Posição X do centro do aspirador
        self.ypos = self.walle.getCenter().getY()            #Posição Y do centro do aspirador
        
    def limpaPonto(self,clickX,clickY,pontodesuj):
        while self.ypos<clickY+40:         #Sequência de movimentos para limpar o ponto de sujidade
            self.walle.move(0,0.05)                            
            self.battery.move(0,0.05)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()                                    
        while self.xpos<clickX+40:
            self.walle.move(0.05,0)
            self.battery.move(0.05,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.ypos>clickY-40:
            self.walle.move(0,-0.05)
            self.battery.move(0,-0.05)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.xpos>clickX-40:
            self.walle.move(-0.05,0)
            self.battery.move(-0.05,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.ypos<clickY+40:
            self.walle.move(0,0.05)
            self.battery.move(0,0.05)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.xpos<clickX:
            self.walle.move(0.05,0)
            self.battery.move(0.05,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.ypos>clickY+20:
            self.walle.move(0,-0.05)
            self.battery.move(0,-0.05)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.xpos<clickX+20:
            self.walle.move(0.05,0)
            self.battery.move(0.05,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.ypos>clickY-20:
            self.walle.move(0,-0.05)
            self.battery.move(0,-0.05)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.xpos>clickX-20:
            self.walle.move(-0.05,0)
            self.battery.move(-0.05,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
        while self.ypos<clickY+20:
            self.walle.move(0,0.05)
            self.battery.move(0,0.05)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()                        
        while self.xpos<clickX:
            self.walle.move(0.05,0)
            self.battery.move(0.05,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
            pontodesuj.undraw()

    def buscaPonto(self,clickX,clickY,movel1,movel2,janelaheight,janelawidth):
        if self.xpos<clickX:          #IF's para detetar a posição do ponto de sujidade relativamente ao robot e atribuir movimento
            while self.xpos<clickX:   #Tendo em conta a posição relativa do ponto (ou sobe,ou desce, ou esquerda, ou direita)
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)   #Deteta colisão e faz desvio de móvel acima
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)    
                self.walle.move(0.1,0)      #Incrementa posição do aspirador e bateria e atualiza xpos e ypos 
                self.battery.move(0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.ypos<clickY:
            while self.ypos<clickY:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)    
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.xpos>clickX:
            while self.xpos>clickX:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth) 
                self.walle.move(-0.1,0)
                self.battery.move(-0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.ypos>clickY:
            while self.ypos>clickY:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth) 
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        
    def buscaPonto_Imp2(self,clickX,clickY,movel1,movel2,movel3,movel4,movel5,janelaheight,janelawidth): #Análogo à função anterior mas para 5 móveis na sala
        if self.xpos<clickX:          #IF's para detetar a posição do ponto de sujidade relativamente ao robot e atribuir movimento
            while self.xpos<clickX:   #Tendo em conta a posição relativa do ponto (ou sobe,ou desce, ou esquerda, ou direita)
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_cima(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_cima(self,movel5,janelaheight,janelawidth)   
                self.walle.move(0.1,0)
                self.battery.move(0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.ypos<clickY:
            while self.ypos<clickY:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_cima(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_cima(self,movel5,janelaheight,janelawidth)    
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.xpos>clickX:
            while self.xpos>clickX:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_cima(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_cima(self,movel5,janelaheight,janelawidth) 
                self.walle.move(-0.1,0)
                self.battery.move(-0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.ypos>clickY:
            while self.ypos>clickY:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_cima(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_cima(self,movel5,janelaheight,janelawidth) 
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()

    def buscaPonto_Imp3(self,clickX,clickY,movel1,movel2,movel3,janelaheight,janelawidth):  #Análogo à função anterior mas para 3 móveis na sala
        if self.xpos<clickX:          #IF's para detetar a posição do ponto de sujidade relativamente ao robot e atribuir movimento
            while self.xpos<clickX:   #Tendo em conta a posição relativa do ponto (ou sobe,ou desce, ou esquerda, ou direita)
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)           
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)  
                self.walle.move(0.1,0)
                self.battery.move(0.1,0)            
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.ypos<clickY:
            while self.ypos<clickY:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)    
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.xpos>clickX:
            while self.xpos>clickX:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth) 
                self.walle.move(-0.1,0)
                self.battery.move(-0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        if self.ypos>clickY:
            while self.ypos>clickY:
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth) 
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()

    def retornaBase(self,dockX,dockY,movel1,movel2,janelaheight,janelawidth):

        if self.ypos<dockY:
            while self.ypos<dockY:                      #IF's para detetar a posição da dockstation e voltar para a mesma
                if Colision(self,movel1):               
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)     #Deteta colisão e faz desvio de móvel abaixo
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)    
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)        #Incrementa a posição do aspirador e bateria e atualiza xpos e ypos
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        
        if self.xpos<dockX:          
            while self.xpos<dockX:   
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)    
                self.walle.move(0.1,0)
                self.battery.move(0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()


        if self.ypos>dockY:
            while self.ypos>dockY:
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth) 
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY() 
        
        if self.xpos>dockX:
            while self.xpos>dockX:
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth) 
                self.walle.move(-0.1,0)
                self.battery.move(-0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()

    def retornaBase_Imp2(self,dockX,dockY,movel1,movel2,movel3,movel4,movel5,janelaheight,janelawidth): #Análogo à função anterior mas para 5 móveis na sala

        if self.ypos<dockY:
            while self.ypos<dockY:                      #IF's para detetar a posição da dockstation e voltar para a mesma
                if Colision(self,movel1):               
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_abaixo(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_abaixo(self,movel5,janelaheight,janelawidth)    
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        
        if self.xpos<dockX:          
            while self.xpos<dockX:   
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_abaixo(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_abaixo(self,movel5,janelaheight,janelawidth)    
                self.walle.move(0.1,0)
                self.battery.move(0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()


        if self.ypos>dockY:
            while self.ypos>dockY:
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_abaixo(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_abaixo(self,movel5,janelaheight,janelawidth) 
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY() 
        
        if self.xpos>dockX:
            while self.xpos>dockX:
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                if Colision(self,movel4):
                    desvia_abaixo(self,movel4,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_abaixo(self,movel5,janelaheight,janelawidth) 
                self.walle.move(-0.1,0)
                self.battery.move(-0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
    
    def retornaBase_Imp3(self,dockX,dockY,movel1,movel2,movel3,janelaheight,janelawidth):  #Análogo à função anterior mas para 3 móveis na sala

        if self.ypos<dockY:
            while self.ypos<dockY:                      #IF's para detetar a posição da dockstation e voltar para a mesma
                if Colision(self,movel1):               
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth) 
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)    
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
        
        if self.xpos<dockX:          
            while self.xpos<dockX:   
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)  
                self.walle.move(0.1,0)
                self.battery.move(0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()


        if self.ypos>dockY:
            while self.ypos>dockY:
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY() 
        
        if self.xpos>dockX:
            while self.xpos>dockX:
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                self.walle.move(-0.1,0)
                self.battery.move(-0.1,0)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()


    def limpa_sala(self,dockX,dockY,movel1,movel2,movel3,movel4,movel5,janelaheight,janelawidth):  #Função para limpeza da totalidade da sala com movimento vai e vem no eixo dos Y
        
        while self.xpos<1080:                        #Inicia limpeza (de baixo para cima)
            while self.ypos<680:
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)   #Deteta colisão e faz desvio de móvel abaixo
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    break
                if Colision(self,movel4):
                    break
                if Colision(self,movel5):
                    desvia_cima(self,movel5,janelaheight,janelawidth)
                if janelaheight-30<self.ypos<janelaheight-20:      #Alcançou o ponto máximo da o eixo dos Y
                    if Colision_lado(self,movel1)==False and Colision_lado(self,movel2)==False and Colision_lado(self,movel3)==False and Colision_lado(self,movel4)==False and Colision_lado(self,movel5)==False and self.xpos<janelawidth-20:
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()   #Se não colidir com nenhum móvel, incrementa a posição do aspirador e bateria para a direita
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
            while self.ypos>20:                     #Limpeza de cima para baixo
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)  #Deteta colisão e faz desvio de móvel abaixo
                if Colision(self,movel5):
                    desvia_abaixo(self,movel5,janelaheight,janelawidth)
                if 20<self.ypos<30:   #Alcançou o ponto mínimo da o eixo dos Y
                    if Colision_lado(self,movel1)==False and Colision_lado(self,movel2)==False and Colision_lado(self,movel3)==False and Colision_lado(self,movel4)==False and Colision_lado(self,movel5)==False and self.xpos<janelawidth-20:
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()           #Se não colidir com nenhum móvel, incrementa a posição do aspirador e bateria para a direita
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()  
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
        while self.xpos>140:  #Volta para trás e volta a relaizar a limpeza. Raciocínio é o mesmo, mas quando chega aos limites do eixo do Y, incrementa a posição do aspirador para o lado esquerdo
            while self.ypos<680:
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    break
                if Colision(self,movel4):
                    break
                if Colision(self,movel5):
                    desvia_cima(self,movel5,janelaheight,janelawidth)
                if janelaheight-30<self.ypos<janelaheight-20:
                    if Colision_lado(self,movel1)==False and Colision_lado(self,movel2)==False and Colision_lado(self,movel3)==False and Colision_lado(self,movel4)==False and Colision_lado(self,movel5)==False and self.xpos<janelawidth-20:
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
            while self.ypos>20:
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel5):
                    desvia_abaixo(self,movel5,janelaheight,janelawidth)
                if 20<self.ypos<30:
                    if Colision(self,movel1)==False and Colision(self,movel2)==False and Colision(self,movel3)==False and Colision(self,movel4)==False and Colision(self,movel5)==False:
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
        self.battery.setFill(color_rgb(255,0,0))
        while self.ypos>dockY:
            self.walle.move(0,-0.1)
            self.battery.move(0,-0.1)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
            if Colision(self,movel1):
                desvia_abaixo(self,movel1,janelaheight,janelawidth)
            if Colision(self,movel2):
                desvia_abaixo(self,movel2,janelaheight,janelawidth)
            if Colision(self,movel3):
                desvia_abaixo(self,movel3,janelaheight,janelawidth)
            if Colision(self,movel4):
                desvia_abaixo(self,movel4,janelaheight,janelawidth)
            if Colision(self,movel5):
                desvia_abaixo(self,movel5,janelaheight,janelawidth)
        while self.xpos>dockX:
            self.walle.move(-0.1,0)
            self.battery.move(-0.1,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
            if Colision(self,movel1):
                desvia_abaixo(self,movel1,janelaheight,janelawidth)
            if Colision(self,movel2):
                desvia_abaixo(self,movel2,janelaheight,janelawidth)
            if Colision(self,movel3):
                desvia_abaixo(self,movel3,janelaheight,janelawidth)
            if Colision(self,movel4):
                desvia_abaixo(self,movel4,janelaheight,janelawidth)
            if Colision(self,movel5):
                desvia_abaixo(self,movel5,janelaheight,janelawidth)
        self.battery.setFill(color_rgb(255,128,0))
        time.sleep(2)                                   #Carrega por 2 segundo e muda a cor para laranja, após carregado verde de novo
        self.battery.setFill(color_rgb(0,223,82))


    def limpa_sala_Imp3(self,dockX,dockY,movel1,movel2,movel3,janelaheight,janelawidth): #Análogo à função anterior mas para 3 móveis na sala
        
        while self.xpos<1080:                        #Inicia limpeza
            while self.ypos<680:
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)
                if janelaheight-30<self.ypos<janelaheight-20:
                    if Colision_lado(self,movel1)==False and Colision_lado(self,movel2)==False and Colision_lado(self,movel3)==False and self.xpos<janelawidth-20:
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
            while self.ypos>20:
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                if 20<self.ypos<30:
                    if Colision_lado(self,movel1)==False and Colision_lado(self,movel2)==False and Colision_lado(self,movel3)==False and self.xpos<janelawidth-20:
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
        while self.xpos>140:                        #Volta para trás
            while self.ypos<680:
                self.walle.move(0,0.1)
                self.battery.move(0,0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_cima(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_cima(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_cima(self,movel3,janelaheight,janelawidth)
                if janelaheight-30<self.ypos<janelaheight-20:
                    if Colision_lado(self,movel1)==False and Colision_lado(self,movel2)==False and Colision_lado(self,movel3)==False and self.xpos<janelawidth-20:
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
            while self.ypos>20:
                self.walle.move(0,-0.1)
                self.battery.move(0,-0.1)
                self.xpos = self.walle.getCenter().getX()
                self.ypos = self.walle.getCenter().getY()
                if Colision(self,movel1):
                    desvia_abaixo(self,movel1,janelaheight,janelawidth)
                if Colision(self,movel2):
                    desvia_abaixo(self,movel2,janelaheight,janelawidth)
                if Colision(self,movel3):
                    desvia_abaixo(self,movel3,janelaheight,janelawidth)
                if 20<self.ypos<30:
                    if Colision(self,movel1)==False and Colision(self,movel2)==False and Colision(self,movel3)==False:
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.walle.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
                        self.battery.move(-0.1,0)
                        self.xpos = self.walle.getCenter().getX()
                        self.ypos = self.walle.getCenter().getY()
        self.battery.setFill(color_rgb(255,0,0))
        while self.ypos>dockY:
            self.walle.move(0,-0.1)
            self.battery.move(0,-0.1)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
            if Colision(self,movel1):
                desvia_abaixo(self,movel1,janelaheight,janelawidth)
            if Colision(self,movel2):
                desvia_abaixo(self,movel2,janelaheight,janelawidth)
            if Colision(self,movel3):
                desvia_abaixo(self,movel3,janelaheight,janelawidth)
        while self.xpos>dockX:
            self.walle.move(-0.1,0)
            self.battery.move(-0.1,0)
            self.xpos = self.walle.getCenter().getX()
            self.ypos = self.walle.getCenter().getY()
            if Colision(self,movel1):
                desvia_abaixo(self,movel1,janelaheight,janelawidth)
            if Colision(self,movel2):
                desvia_abaixo(self,movel2,janelaheight,janelawidth)
            if Colision(self,movel3):
                desvia_abaixo(self,movel3,janelaheight,janelawidth)
        self.battery.setFill(color_rgb(255,128,0))
        time.sleep(2)                                   #Carrega por 2 segundo e muda a cor para laranja, após carregado verde de novo
        self.battery.setFill(color_rgb(0,223,82))