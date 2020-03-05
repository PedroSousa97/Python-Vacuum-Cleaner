from graphics import *
from Movel import *
from Robot import *


def Colision(aspirador,obstaculo):
    if obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20 and  obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y1 - 10: #Deteta colisão quando o aspirador está por baixo do móvel
        return True
    if obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 +20 and obstaculo.y2 + 10 < aspirador.ypos < obstaculo.y2 + 20:   #Deteta colisão quando o aspirador está acima do móvel
        return True
    else:
        return False
def Colision_lado(aspirador,obstaculo):
    if obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 + 20 and obstaculo.x1-20 < aspirador.xpos < obstaculo.x1 - 10:        #Deteta colisão quando o aspirador está à esquerda do móvel
        return True
    if obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 +20 and obstaculo.x2 + 10 < aspirador.xpos < obstaculo.x2 + 20:       #Deteta colisão quando o aspirador está à direita do móvel
        return True
    else:
        return False


def desvia_cima(aspirador,obstaculo,janelaheight,janelawidth):
    if aspirador.xpos<janelawidth/2:                                                        #Caso de desvio quando o aspirador se encontra por baixo do obstaculo
        if Colision(aspirador,obstaculo): 
            voltar = aspirador.xpos
            while obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20:
                aspirador.walle.move(0.1,0)             #Quando este se encontra na metade esquerda do ecrã (aspirador.xpos<janelawidth/2) desvia-se pela direita, nunca saindo assim do ecrã     
                aspirador.battery.move(0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 + 20:
                aspirador.walle.move(0,0.1)
                aspirador.battery.move(0,0.1)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            if aspirador.ypos < janelaheight-20:
                while aspirador.xpos > voltar:
                    aspirador.walle.move(-0.1,0)
                    aspirador.battery.move(-0.1,0)
                    aspirador.xpos=aspirador.walle.getCenter().getX()
                    aspirador.ypos=aspirador.walle.getCenter().getY()
    if aspirador.xpos>janelawidth/2:
        if Colision(aspirador,obstaculo): 
            voltar = aspirador.xpos
            while obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20:
                aspirador.walle.move(-0.1,0)
                aspirador.battery.move(-0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 + 20:
                aspirador.walle.move(0,0.1)             #Quando este se encontra na metade direita do ecrã (aspirador.xpos>janelawidth/2) desvia-se pela esquerda, nunca saindo assim do ecrã
                aspirador.battery.move(0,0.1)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            if aspirador.ypos < janelaheight-20:
                while aspirador.xpos < voltar:
                    aspirador.walle.move(0.1,0)
                    aspirador.battery.move(0.1,0)
                    aspirador.xpos=aspirador.walle.getCenter().getX()
                    aspirador.ypos=aspirador.walle.getCenter().getY()
    if janelawidth/2-20<aspirador.xpos<janelawidth/2+20:
        if Colision(aspirador,obstaculo): 
            voltar = aspirador.xpos
            while obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20:
                aspirador.walle.move(0.1,0)
                aspirador.battery.move(0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 + 20:
                aspirador.walle.move(0,0.1)                                                             #Quando está a meio do ecrã opta pelo desvio à direita
                aspirador.battery.move(0,0.1)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while aspirador.xpos > voltar:
                aspirador.walle.move(-0.1,0)
                aspirador.battery.move(-0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()

def desvia_abaixo(aspirador,obstaculo,janelaheight,janelawidth):
    if aspirador.xpos<janelawidth/2:
        if Colision(aspirador,obstaculo):                                                 #Caso de desvio quando o aspirador se encontra por cima do obstaculo
            voltar = aspirador.xpos
            while obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20:
                aspirador.walle.move(0.1,0)                 #Quando este se encontra na metade esquerda do ecrã (aspirador.xpos<janelawidth/2) desvia-se pela direita, nunca saindo assim do ecrã
                aspirador.battery.move(0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while obstaculo.y1 - 20 < aspirador.ypos:
                aspirador.walle.move(0,-0.1)
                aspirador.battery.move(0,-0.1)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            if aspirador.ypos > 20:
                while aspirador.xpos > voltar:
                    aspirador.walle.move(-0.1,0)
                    aspirador.battery.move(-0.1,0)
                    aspirador.xpos=aspirador.walle.getCenter().getX()
                    aspirador.ypos=aspirador.walle.getCenter().getY()
    if aspirador.xpos>janelawidth/2:
        if Colision(aspirador,obstaculo): 
            voltar = aspirador.xpos
            while obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20:
                aspirador.walle.move(-0.1,0)
                aspirador.battery.move(-0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 + 20:
                aspirador.walle.move(0,-0.1)                 #Quando este se encontra na metade direita do ecrã (aspirador.xpos>janelawidth/2) desvia-se pela esquerda, nunca saindo assim do ecrã
                aspirador.battery.move(0,-0.1)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            if aspirador.ypos > 20:
                while aspirador.xpos < voltar:
                    aspirador.walle.move(0.1,0)
                    aspirador.battery.move(0.1,0)
                    aspirador.xpos=aspirador.walle.getCenter().getX()
                    aspirador.ypos=aspirador.walle.getCenter().getY()
    if janelawidth/2-20<aspirador.xpos<janelawidth/2+20:
        if Colision(aspirador,obstaculo): 
            voltar = aspirador.xpos
            while obstaculo.x1 - 20 < aspirador.xpos < obstaculo.x2 + 20:
                aspirador.walle.move(0.1,0)
                aspirador.battery.move(0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while obstaculo.y1 - 20 < aspirador.ypos < obstaculo.y2 + 20:
                aspirador.walle.move(0,-0.1)                                                             #Quando está a meio do ecrã opta pelo desvio à direita
                aspirador.battery.move(0,-0.1)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()
            while aspirador.xpos > voltar:
                aspirador.walle.move(-0.1,0)
                aspirador.battery.move(-0.1,0)
                aspirador.xpos=aspirador.walle.getCenter().getX()
                aspirador.ypos=aspirador.walle.getCenter().getY()


def pontoParede(clickX,clickY):         #Deteta se o ponto de sujidade está demasiado perto da parede. Se for o caso atribui um valor de X,Y ideal para a realização da limpeza
    if clickY<60:
        clickY=60
        return clickX,clickY
    if clickY>640:
        clickY=640
        return clickX,clickY
    if clickX<60:
        clickX=60
        return clickX,clickY
    if clickX>1040:
        clickX=1040
        return clickX,clickY
    else:
        return clickX,clickY