from graphics import *


class Menu:

    def createMenu(self,win,midscreenx,midscreeny):   #Função para criação dos botões e colocação dos mesmo em posições ideiais
    

        button1 = Image(Point(midscreenx,midscreeny+270), 'button1.png')
        button1.draw(win)
        button2 = Image(Point(midscreenx,midscreeny+90), 'button2.png')
        button2.draw(win)
        button3 = Image(Point(midscreenx,midscreeny-90), 'button3.png')
        button3.draw(win)
        button4 = Image(Point(midscreenx,midscreeny-270), 'buttonEXIT.png')
        button4.draw(win)

    def buttonClicked(self,x,y):        #Função para deteção do botão selecionado, a cada seleção corresponde um return do tipo string
        if y>27.5 and y<132.5:
            button = 'button4'
            return button
        if y>207.5 and y<312.5:
            button = 'button3'
            return button
        if y>387.5 and y<492.5:
            button = 'button2'
            return button
        if y>567.5 and y<672.5:
            button = 'button1'
            return button
