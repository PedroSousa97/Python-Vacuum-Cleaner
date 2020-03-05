from graphics import *

class Button:

    def createButton(self, x1, y1, x2, y2):              #Função para criar o botão de exit
        button = Rectangle(Point(x1,y1),Point(x2,y2))
        button.setFill('white')
        button.setOutline('black')
        return button

    def createText(self, x1, y1, x2, y2,string):          #Função para escrita de texto no notão
        x=x2-x1
        y=y1-y2
        text= Text(Point(x/2,(y2+y/2)),string)
        text.setFace("courier")
        text.setStyle("bold")
        text.setTextColor('black')
        return text

    def Clicked(self,x1,y1,x2,y2):                         #Função para deteção de seleção, a cada coleção corresponde uma string
        if x1<x2 and y1>y2:
            button = 'clicked'
            return button
        else:
            button = 'continue'
            return button