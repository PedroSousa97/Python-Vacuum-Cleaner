from graphics import *
from Movel import *
from Robot import *
from Menu import *
from button import *
from Functions import *
import time
import re
import random





def main():

    var=1 #Criação de uma variável que se manterá constante de forma a criar o loop infinito que irá conter o menu inicial
          #Permitindo desta forma que após cada implementação, o utlizador volte sempre ao menu inicial
    while var==1:
        win= GraphWin("Menu",700,700)
        win.setBackground('black')
        win.setCoords(0.0,0.0,700.0,700.0)  #Criação do Menu propriamente dito

        midscreenx = win.getWidth()/2     #Meia largura da janela
        midscreeny = win.getHeight()/2    #Meia altura da janela


        options = Menu()    



        options.createMenu(win,midscreenx,midscreeny) #Cria menu com com todos os seus botões botões

        aspirador1 = Image(Point(40,660), 'aspirador1.png')
        aspirador1.draw(win)
        aspirador2 = Image(Point(660,40), 'aspirador2.png')
        aspirador2.draw(win)

        clickPoint = win.getMouse()                   #Deteção do click do mouse para seleção da implementação ou botão exit
        clickPointX = clickPoint.getX()               #Componente X do click
        clickPointY = clickPoint.getY()               #Componente Y do click
        opt=options.buttonClicked(clickPointX,clickPointY)    #Verifica que botão foi carregado
        
        if opt== 'button1':    #Implementação1
            
            win2= GraphWin("Implementação1",1100,700)    #Criação da Janela da 1ª Implementação
            win2.setBackground(color_rgb(119,76,0))
            win2.setCoords(0.0,0.0,1100.0,700.0)
            win.close()                                  #Fecha Janela de Menu para não ter as duas janelas abertas simultaneamente
                                                         #E evitando também que se acomulem janelas de menu após cada implementação
    
            mobilia1=Movel(1000,1100,100,400)            #Cria "sofá" 
            mobilia1.criaSofa(win2)
            mobilia2=Movel(0,160,170,330)                #Cria "mesa redonda" 
            mobilia2.criaMesa(win2)

            dock = Rectangle(Point(0,0),Point(40,40))               #Criação da docking station
            dock.setOutline(color_rgb(0,0,0))
            dock.setFill(color_rgb(0,0,0))
            dock.draw(win2)
            robot= Robot(win2, 20, 20)                    #Cria robot com ponto de ancoragem no meio da docking station
            exitbutton= Button()                                    
            exitbutton.createButton(0,700,100,670).draw(win2)       #Cria rectângulo para o botão de Exit
            exitbutton.createText(0,700,100,670,"EXIT").draw(win2)  #Escreve EXIT no botão

            variavel = 1                 #É definida aqui mais uma variável para o loop infinito de simulação até o utilizador clicar EXIT
            while variavel==1:
                click = win2.getMouse()  #Deteta click e atribui coordenadas
                clickX = click.getX()    #X do click
                clickY = click.getY()    #Y do click
                while clickY>mobilia2.y1-60 and clickY<mobilia2.y2+60 and clickX<mobilia2.x2+60:        #Deteta se o click foi feito em cima de uma móvel ou demasiado perto, se for esse o caso aguarda novo click
                    click = win2.getMouse()  
                    clickX = click.getX()    
                    clickY = click.getY()    
                while clickY>mobilia1.y1-60 and clickY<mobilia1.y2+60 and clickX>mobilia1.x1-60:        #Deteta se o click foi feito em cima de uma móvel ou demasiado perto, se for esse o caso aguarda novo click
                    click = win2.getMouse()  
                    clickX = click.getX()    
                    clickY = click.getY()
                while clickY>680 or clickY<20 or clickX>1080 or clickX<20:        #Deteta se o click foi feito demasiado perto da parede, se for esse o caso aguarda novo click
                    click = win2.getMouse()  
                    clickX = click.getX()    
                    clickY = click.getY()  
                ext=exitbutton.Clicked(clickX,clickY,100,670)    #Deteta se foi clicado o botão EXIT

                if ext == 'continue':                         #Caso não tenha sido clicado, o click transforma-se num Ponto de Sujidade

                    pontodesuj=Point(clickX,clickY)           #Definição do ponto de sujidade e das suas propriedades
                    pontodesuj.setFill('red')
                    pontodesuj.setOutline('red')
                    pontodesuj.draw(win2)

                    clickX,clickY=pontoParede(clickX,clickY)     #Funçaõ de deteção que confirma se o ponto pode ser limpo sem que o aspirador saia do ecrã. Senão altera coordenadas
                    robot.buscaPonto(clickX,clickY,mobilia1,mobilia2,700,1100)      #Busca ponto para limpeza
                    robot.limpaPonto(clickX,clickY,pontodesuj)                      #Limpa ponto
                    robot.retornaBase(20,20,mobilia1,mobilia2,700,1100)             #Retorna à dockstation
                    
                            
                    
                    
                if ext =='clicked':             #Clicou Exit, sai da simulação e volta ao menu inicial
                    win2.close()
                    break
                

        if opt== 'button2': #Implementação2

            win2= GraphWin("Implementação2",1100,700)    #Criação da Janela da 2ª Implementação
            win2.setBackground(color_rgb(119,76,0))
            win2.setCoords(0.0,0.0,1100.0,700.0)
            win.close()                                  #Fecha Janela de Menu para não ter as duas janelas abertas simultaneamente
                                                         #E evitando também que se acomulem janelas de menu após cada implementação

            mobilia1=Movel(1000,1100,100,400)               #Cria "sofá" e guarda as suas coordenadas
            mobilia1.criaSofa(win2)
            mobilia2=Movel(500,600,300,400)                #Cria "mesa redonda" e guarda as suas coordenadas
            mobilia2.criaMesa(win2)
            mobilia3=Movel(300,500,600,700)                 #Cria "sofá" e guarda as suas coordenadas
            mobilia3.criaSofa(win2)
            mobilia4=Movel(700,1000,600,700)                #Cria "sofá" e guarda as suas coordenadas
            mobilia4.criaSofa(win2)
            mobilia5=Movel(0,100,200,300)                   #Cria "sofá" e guarda as suas coordenadas
            mobilia5.criaSofa(win2)     

            dock = Rectangle(Point(0,0),Point(40,40))               #Criação da docking station
            dock.setOutline(color_rgb(0,0,0))
            dock.setFill(color_rgb(0,0,0))
            dock.draw(win2)
            robot= Robot(win2, 20, 20)                    #Cria robot com ponto de ancoragem no meio da docking station
            exitbutton= Button()                                    
            exitbutton.createButton(0,700,100,670).draw(win2)       #Cria rectângulo para o botão de Exit
            exitbutton.createText(0,700,100,670,"EXIT").draw(win2)  #Escreve EXIT no botão
    

            variavel = 1                 #É definida aqui mais uma variável para o loop infinito de simulação até o utilizador clicar EXIT
            while variavel==1:
                click = win2.getMouse()  #Deteta click e atribui coordenadas
                clickX = click.getX()    #X do click
                clickY = click.getY()    #Y do click
                ext=exitbutton.Clicked(clickX,clickY,100,670)    #Deteta se foi clicado o botão EXIT

                if ext == 'continue':                         #Caso não tenha sido clicado, o click transforma-se num Ponto de Sujidade
                    
                    robot.limpa_sala(20,20,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)  #Limpeza da totalidade da sala
                    block= Rectangle(Point(200,300),Point(900,400))
                    block.setFill('white')
                    block.setOutline('black')
                    block.draw(win2)
                    text= Text(Point(550,350),'Escolha 3 Pontos de Sujidade')
                    text.setFace("courier")
                    text.setStyle("bold")
                    text.setTextColor('black')
                    text.draw(win2)
                    time.sleep(6)                   #Este código acima cria uma mensagem pop up após o aspirador se carregar que durante 6 segundos avisa o utilizador para escolher 3 pontos de sujidade
                    block.undraw()
                    text.undraw()
                    click = win2.getMouse()  #Deteta click e atribui coordenadas
                    clickX = click.getX()    #X do click
                    clickY = click.getY()    #Y do click
                    while mobilia2.y1-60<clickY<mobilia2.y2+60 and mobilia2.x1-60<clickX<mobilia2.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click = win2.getMouse()  
                        clickX = click.getX()    
                        clickY = click.getY()    
                    while mobilia1.y1-60<clickY<mobilia1.y2+60 and mobilia1.x1-60<clickX<mobilia1.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click = win2.getMouse()  
                        clickX = click.getX()    
                        clickY = click.getY()
                    while mobilia3.y1-60<clickY<mobilia3.y2+60 and mobilia3.x1-60<clickX<mobilia3.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click = win2.getMouse()  
                        clickX = click.getX()    
                        clickY = click.getY()    
                    while mobilia4.y1-60<clickY<mobilia4.y2+60 and mobilia4.x1-60<clickX<mobilia4.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click = win2.getMouse()  
                        clickX = click.getX()    
                        clickY = click.getY()
                    while mobilia5.y1-60<clickY<mobilia5.y2+60 and mobilia5.x1-60<clickX<mobilia5.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click = win2.getMouse()  
                        clickX = click.getX()    
                        clickY = click.getY()    
                    while clickY>680 or clickY<20 or clickX>1080 or clickX<20:        #Deteta se o click foi feito demasiado perto da parede, se for esse o caso aguarda novo click
                        click = win2.getMouse()  
                        clickX = click.getX()    
                        clickY = click.getY()
                    pontodesuj=Point(clickX,clickY)           #Definição do ponto de sujidade e das suas propriedades
                    pontodesuj.setFill('red')
                    pontodesuj.setOutline('red')
                    pontodesuj.draw(win2)
                    
                    click2 = win2.getMouse()  #Deteta click e atribui coordenadas
                    clickX2 = click2.getX()    #X do click
                    clickY2 = click2.getY()    #Y do click
                    while mobilia2.y1-60<clickY2<mobilia2.y2+60 and mobilia2.x1-60<clickX2<mobilia2.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click2 = win2.getMouse()  
                        clickX2 = click2.getX()    
                        clickY2 = click2.getY()    
                    while mobilia1.y1-60<clickY2<mobilia1.y2+60 and mobilia1.x1-60<clickX2<mobilia1.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click2 = win2.getMouse()  
                        clickX2 = click2.getX()    
                        clickY2 = click2.getY()
                    while mobilia3.y1-60<clickY2<mobilia3.y2+60 and mobilia3.x1-60<clickX2<mobilia3.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click2 = win2.getMouse()  
                        clickX2 = click2.getX()    
                        clickY2 = click2.getY()    
                    while mobilia4.y1-60<clickY2<mobilia4.y2+60 and mobilia4.x1-60<clickX2<mobilia4.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click2 = win2.getMouse()  
                        clickX2 = click2.getX()    
                        clickY2 = click2.getY()
                    while mobilia5.y1-60<clickY2<mobilia5.y2+60 and mobilia5.x1-60<clickX2<mobilia5.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click2 = win2.getMouse()  
                        clickX2 = click2.getX()    
                        clickY2 = click2.getY()    
                    while clickY2>680 or clickY2<20 or clickX2>1080 or clickX2<20:        #Deteta se o click foi feito demasiado perto da parede, se for esse o caso aguarda novo click
                        click2 = win2.getMouse()  
                        clickX2 = click2.getX()    
                        clickY2 = click2.getY()
                    pontodesuj2=Point(clickX2,clickY2)           #Definição do ponto de sujidade e das suas propriedades
                    pontodesuj2.setFill('red')
                    pontodesuj2.setOutline('red')
                    pontodesuj2.draw(win2)

                    click3 = win2.getMouse()  #Deteta click e atribui coordenadas
                    clickX3 = click3.getX()    #X do click
                    clickY3 = click3.getY()    #Y do click
                    while mobilia2.y1-60<clickY3<mobilia2.y2+60 and mobilia2.x1-60<clickX3<mobilia2.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click3 = win2.getMouse()  
                        clickX3 = click3.getX()    
                        clickY3 = click3.getY()    
                    while mobilia1.y1-60<clickY3<mobilia1.y2+60 and mobilia1.x1-60<clickX3<mobilia1.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click3 = win2.getMouse()  
                        clickX3 = click3.getX()    
                        clickY3 = click3.getY()
                    while mobilia3.y1-60<clickY3<mobilia3.y2+60 and mobilia3.x1-60<clickX3<mobilia3.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click3 = win2.getMouse()  
                        clickX3 = click3.getX()    
                        clickY3 = click3.getY()    
                    while mobilia4.y1-60<clickY3<mobilia4.y2+60 and mobilia4.x1-60<clickX3<mobilia4.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click3 = win2.getMouse()  
                        clickX3 = click3.getX()    
                        clickY3 = click3.getY()
                    while mobilia5.y1-60<clickY3<mobilia5.y2+60 and mobilia5.x1-60<clickX3<mobilia5.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                        click3 = win2.getMouse()  
                        clickX3 = click3.getX()    
                        clickY3 = click3.getY()    
                    while clickY3>680 or clickY3<20 or clickX3>1080 or clickX3<20:        #Deteta se o click foi feito demasiado perto da parede, se for esse o caso aguarda novo click
                        click3 = win2.getMouse()  
                        clickX3 = click3.getX()    
                        clickY3 = click3.getY()
                    pontodesuj3=Point(clickX3,clickY3)           #Definição do ponto de sujidade e das suas propriedades
                    pontodesuj3.setFill('red')
                    pontodesuj3.setOutline('red')
                    pontodesuj3.draw(win2)

                    clickX,clickY=pontoParede(clickX,clickY)    #Análogo à implementação 1 mas para 3 pontos de sujidade
                    robot.buscaPonto_Imp2(clickX,clickY,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)
                    robot.limpaPonto(clickX,clickY,pontodesuj)   
                    robot.retornaBase_Imp2(20,20,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)

                    clickX2,clickY2=pontoParede(clickX2,clickY2)
                    robot.buscaPonto_Imp2(clickX2,clickY2,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)
                    robot.limpaPonto(clickX2,clickY2,pontodesuj2)   
                    robot.retornaBase_Imp2(20,20,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)

                    clickX3,clickY3=pontoParede(clickX3,clickY3)
                    robot.buscaPonto_Imp2(clickX3,clickY3,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)
                    robot.limpaPonto(clickX3,clickY3,pontodesuj3)   
                    robot.retornaBase_Imp2(20,20,mobilia1,mobilia2,mobilia3,mobilia4,mobilia5,700,1100)


                if ext =='clicked':             #Clicou Exit, sai da simulação e volta ao menu inicial
                    win2.close()
                    break

        if opt== 'button3':
            win2= GraphWin("Implementação3Menu",700,700)    #Criação da Janela da 3ª Implementação
            win2.setBackground(color_rgb(0,0,0))
            win2.setCoords(0.0,0.0,700.0,700.0)
            win.close()

            button1 = Rectangle(Point((win2.getWidth()/2)-100,(win2.getHeight()/2)+200),Point((win2.getWidth()/2)+100,(win2.getHeight()/2)+100))
            button1.setFill(color_rgb(255,255,255))
            button1.setOutline(color_rgb(0,0,0))                            #Criação dos botões de seleção do modo de criação de ambiente
            button1.draw(win2)

            button2 = Rectangle(Point((win2.getWidth()/2)-100,(win2.getHeight()/2)-100),Point((win2.getWidth())/2+100,(win2.getHeight()/2)-200))
            button2.setFill(color_rgb(255,255,255))
            button2.setOutline(color_rgb(0,0,0))
            button2.draw(win2)

            text1 = Text(Point(win2.getWidth()/2,(win2.getHeight()/2)+150),'Ficheiro Txt')
            text1.setFace("courier")
            text1.setStyle("bold")
            text1.setTextColor('black')
            text1.draw(win2)

            text2 = Text(Point(win2.getWidth()/2,(win2.getHeight()/2)-150),'Random')
            text2.setFace("courier")
            text2.setStyle("bold")
            text2.setTextColor('black')
            text2.draw(win2)

            escolha2 = win2.getMouse()                   #Deteção do click do mouse para seleção da implementação ou botão exit
            escolha2X = escolha2.getX()               #Componente X do click
            escolha2Y = escolha2.getY()               #Componente Y do click

            if escolha2X>(win2.getWidth()/2)-100 and escolha2X<(win2.getWidth()/2)+100 and escolha2Y>(win2.getHeight()/2)+100 and escolha2Y<(win2.getHeight()/2)+200:
                reader=open("Ambiente.txt","r")                 #Abre o ficheiro ambiente em modo leitura
                ambiente=reader.readlines()                     #Lê todas as linhas do ficheiro e guarda-as num vetor, cada linha corresponde a uma posição
                janelasize= ambiente[1].split()                 #Separa as palavras (neste caso numeros) da linha 2 do ficheiro e atribui cada numero a uma posição de vetor
                win3= GraphWin("Text",janelasize[0],janelasize[1])    #Criação da Janela da 3ª Implementação por leitura de texto
                win3.setBackground(color_rgb(119,76,0))
                win3.setCoords(0.0,0.0,float(janelasize[0]),float(janelasize[1]))
                win2.close() 

                dockloc=re.findall(r'\d+',ambiente[4])           #Função que extrai os números de uma string (Frase) e guarda-os num vetor ordenado
                dock = Rectangle(Point(int(dockloc[0]),int(dockloc[1])),Point(int(dockloc[2]),int(dockloc[3])))               #Criação da docking station
                dock.setOutline(color_rgb(0,0,0))
                dock.setFill(color_rgb(0,0,0))
                dock.draw(win3)
                
                
                movel1=re.findall(r'\d+',ambiente[5])           #Função que extrai os números de uma string (Frase) e guarda-os num vetor ordenado
                
                movel2=re.findall(r'\d+',ambiente[6])            
                
                movel3=re.findall(r'\d+',ambiente[7])

                mobilia1=Movel(int(movel1[0]),int(movel1[2]),int(movel1[1]),int(movel1[3]))         #Cria "Sofá" e guarda as suas coordenadas
                mobilia1.criaSofa(win3)
                mobilia2=Movel(int(movel2[0])-int(movel2[2]),int(movel2[0])+int(movel2[2]),int(movel2[1])-int(movel2[2]),int(movel2[1])+int(movel2[2]))      #Cria "mesa redonda" e guarda as suas coordenadas
                mobilia2.criaMesa(win3)
                mobilia3=Movel(int(movel3[0]),int(movel3[2]),int(movel3[1]),int(movel3[3]))         #Cria "Sofá" e guarda as suas coordenadas
                mobilia3.criaSofa(win3)
                
                robot= Robot(win3, int(dockloc[2])/2, int(dockloc[3])/2)  #Criação do robot com ponto de ancoragem no meio da dockstation  

                exitbutton= Button()                                    
                exitbutton.createButton(0,700,100,670).draw(win3)       #Cria rectângulo para o botão de Exit
                exitbutton.createText(0,700,100,670,"EXIT").draw(win3)  #Escreve EXIT no botão
                
                
                variavel = 1                 #É definida aqui mais uma variável para o loop infinito de simulação até o utilizador clicar EXIT
                while variavel==1:
                    click = win3.getMouse()  #Deteta click e atribui coordenadas
                    clickX = click.getX()    #X do click
                    clickY = click.getY()    #Y do click
                    
                    ext=exitbutton.Clicked(clickX,clickY,100,670)    #Deteta se foi clicado o botão EXIT

                    if ext == 'continue':                         #Caso não tenha sido clicado, o click transforma-se num Ponto de Sujidade
                        button1 = Rectangle(Point((win3.getWidth()/2)-100,(win3.getHeight()/2)+200),Point((win3.getWidth()/2)+100,(win3.getHeight()/2)+100))
                        button1.setFill(color_rgb(255,255,255))
                        button1.setOutline(color_rgb(0,0,0))                #Criação dos botões de seleção do modo de atribuição de pontos de sujidade
                        button1.draw(win3)

                        button2 = Rectangle(Point((win3.getWidth()/2)-100,(win3.getHeight()/2)-100),Point((win3.getWidth())/2+100,(win3.getHeight()/2)-200))
                        button2.setFill(color_rgb(255,255,255))
                        button2.setOutline(color_rgb(0,0,0))
                        button2.draw(win3)

                        text1 = Text(Point(win3.getWidth()/2,(win3.getHeight()/2)+150),'Pontos por Click')
                        text1.setFace("courier")
                        text1.setStyle("bold")
                        text1.setTextColor('black')
                        text1.draw(win3)

                        text2 = Text(Point(win3.getWidth()/2,(win3.getHeight()/2)-150),'Pontos por txt')
                        text2.setFace("courier")
                        text2.setStyle("bold")
                        text2.setTextColor('black')
                        text2.draw(win3)

                        escolha3 = win3.getMouse()                   #Deteção do click do mouse para seleção da implementação ou botão exit
                        escolha3X = escolha3.getX()               #Componente X do click
                        escolha3Y = escolha3.getY()               #Componente Y do click
                        
                        #If para verificar qual dos botões foi selecionado
                        if escolha3X>(win3.getWidth()/2)-100 and escolha3X<(win3.getWidth()/2)+100 and escolha3Y>(win3.getHeight()/2)+100 and escolha3Y<(win3.getHeight()/2)+200:
                            button1.undraw()
                            button2.undraw()        #Apaga menu de pontos de sujidade
                            text1.undraw()
                            text2.undraw()
                            robot.limpa_sala_Imp3(20,20,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0])) #Limpa sala na totalidade
                            block= Rectangle(Point(200,300),Point(900,400))
                            block.setFill('white')
                            block.setOutline('black')
                            block.draw(win3)
                            text= Text(Point(550,350),'Escolha 1 Ponto de Sujidade')
                            text.setFace("courier")
                            text.setStyle("bold")
                            text.setTextColor('black')
                            text.draw(win3)
                            time.sleep(6)                   #Este código acima cria uma mensagem pop up após o aspirador se carregar que durante 6 segundos avisa o utilizador para escolher 1 pontos de sujidade
                            block.undraw()
                            text.undraw()
                            p = win3.getMouse()  #Deteta click e atribui coordenadas
                            pX = p.getX()        #X do click
                            pY = p.getY()        #Y do click

                            while mobilia2.y1-60<pY<mobilia2.y2+60 and mobilia2.x1-60<pX<mobilia2.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                                p = win3.getMouse()  
                                pX = p.getX()    
                                pY = p.getY()    
                            while mobilia1.y1-60<pY<mobilia1.y2+60 and mobilia1.x1-60<pX<mobilia1.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                                p = win3.getMouse()  
                                pX = p.getX()    
                                pY = p.getY()
                            while mobilia3.y1-60<pY<mobilia3.y2+60 and mobilia3.x1-60<pX<mobilia3.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                                p = win3.getMouse()  
                                pX = p.getX()    
                                pY = p.getY()
                            while pY>int(janelasize[1])-20 or pY<20 or pX>int(janelasize[0])-20 or pX<20:        #Deteta se o click foi feito demasiado perto da parede, se for esse o caso aguarda novo click
                                    p = win3.getMouse()  
                                    pX = p.getX()    
                                    pY = p.getY()

                            pontodesuj=Point(pX,pY)           #Definição do ponto de sujidade e das suas propriedades
                            pontodesuj.setFill('red')
                            pontodesuj.setOutline('red')
                            pontodesuj.draw(win3)

                            pX,pY=pontoParede(pX,pY)
                            robot.buscaPonto_Imp3(pX,pY,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))
                            robot.limpaPonto(pX,pY,pontodesuj)   
                            robot.retornaBase_Imp3(20,20,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))
                        
                    if ext =='clicked':             #Clicou Exit, sai da simulação e volta ao menu inicial
                        win3.close()
                        break
                    #If para verificar qual dos botões foi selecionado
                    if escolha3X>(win3.getWidth()/2)-100 and escolha3X<(win3.getWidth()/2)+100 and escolha3Y<(win3.getHeight()/2)-100 and escolha3Y>(win3.getHeight()/2)-200:
                            button1.undraw()
                            button2.undraw()
                            text1.undraw()
                            text2.undraw()
                            robot.limpa_sala_Imp3(20,20,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))  #Limpa sala na totalidade
                            block= Rectangle(Point(200,300),Point(900,400))
                            block.setFill('white')
                            block.setOutline('black')
                            block.draw(win3)
                            text= Text(Point(550,350),'Pontos de Sujidade por texto')
                            text.setFace("courier")
                            text.setStyle("bold")
                            text.setTextColor('black')
                            text.draw(win3)
                            time.sleep(6)                   #Este código acima cria uma mensagem pop up após o aspirador se carregar que durante 6 segundos avisa o utilizador que os pontos de sujidade são lidos de um ficheiro de texto
                            block.undraw()
                            text.undraw()


                            reader2=open("Limpeza.txt","r")         #Abre o ficheiro dos pontos de sujidade em modo leitura
                            pontos=reader2.readlines()              #Lê todas as linhas do ficheiro de texto e coloca cada linha numa posição do vetor
                            
                            px_1=re.findall(r'\d+',pontos[1])       #Função que extrai todos os numeros de uma linha e coloca-os ordenados num vetor
                            pX=int(px_1[0])                         #Primeiro numero do vetor
                            pY=int(px_1[1])                         #Segundo número de um vetor
                            pontodesuj1=Point(pX,pY)           #Definição do ponto de sujidade e das suas propriedades
                            pontodesuj1.setFill('red')
                            pontodesuj1.setOutline('red')
                            pontodesuj1.draw(win3)

                            px_2=re.findall(r'\d+',pontos[2])
                            pX2=int(px_2[0])
                            pY2=int(px_2[1])
                            pontodesuj2=Point(pX2,pY2)           #Definição do ponto de sujidade e das suas propriedades
                            pontodesuj2.setFill('red')
                            pontodesuj2.setOutline('red')
                            pontodesuj2.draw(win3)

                            px_3=re.findall(r'\d+',pontos[3])
                            pX3=int(px_3[0])
                            pY3=int(px_3[1])
                            pontodesuj3=Point(pX3,pY3)           #Definição do ponto de sujidade e das suas propriedades
                            pontodesuj3.setFill('red')
                            pontodesuj3.setOutline('red')
                            pontodesuj3.draw(win3)

                            pX,pY=pontoParede(pX,pY)
                            robot.buscaPonto_Imp3(pX,pY,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))
                            robot.limpaPonto(pX,pY,pontodesuj1)   
                            robot.retornaBase_Imp3(20,20,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))

                            pX2,pY2=pontoParede(pX2,pY2)
                            robot.buscaPonto_Imp3(pX2,pY2,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))
                            robot.limpaPonto(pX2,pY2,pontodesuj2)   
                            robot.retornaBase_Imp3(20,20,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))

                            pX3,pY3=pontoParede(pX3,pY3)
                            robot.buscaPonto_Imp3(pX3,pY3,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))
                            robot.limpaPonto(pX3,pY3,pontodesuj3)   
                            robot.retornaBase_Imp3(20,20,mobilia1,mobilia2,mobilia3,int(janelasize[1]),int(janelasize[0]))
                            
                    if ext =='clicked':             #Clicou Exit, sai da simulação e volta ao menu inicial
                        win3.close()
                        break
                



            #If que obtém a posição do click e o associa à opção RANDOM
            if escolha2X>(win2.getWidth()/2)-100 and escolha2X<(win2.getWidth()/2)+100 and escolha2Y>(win2.getHeight()/2)-200 and escolha2Y<(win2.getHeight()/2)-100:
                win3= GraphWin("Random",1100,700)    #Criação da Janela da 3ª Implementação por leitura de texto
                win3.setBackground(color_rgb(119,76,0))
                win3.setCoords(0.0,0.0,1100.0,700.0)
                win2.close()
                
                x1=random.randint(60,300)
                x2=random.randint(x1,400)
                y1=random.randint(400,500)              #Variáveis aleatórias para criação do sofá, mas entre valores que salvaguardem a passagem do aspirador por toda a sala e sua limpeza
                y2=random.randint(y1,500)

                x3=random.randint(600,700)
                x4=random.randint(x3,900)
                y3=random.randint(400,500)
                y4=random.randint(y3,600)

                x5=random.randint(600,700)
                x6=random.randint(x5,900)
                y5=random.randint(60,200)
                y6=random.randint(y5,300)

                mobilia1=Movel(x1,x2,y1,y2)                #Cria "sofá" e guarda as suas coordenadas
                mobilia1.criaSofa(win3)
                mobilia2=Movel(x3,x4,y3,y4)                #Cria "mesa redonda" e guarda as suas coordenadas
                mobilia2.criaSofa(win3)
                mobilia3=Movel(x5,x6,y5,y6)                #Cria "sofá" e guarda as suas coordenadas
                mobilia3.criaSofa(win3)
                
                dock = Rectangle(Point(0,0),Point(40,40))               #Criação da docking station
                dock.setOutline(color_rgb(0,0,0))
                dock.setFill(color_rgb(0,0,0))
                dock.draw(win3)
                robot= Robot(win3,20,20)                    #Cria robot com ponto de ancoragem no meio da docking station
                exitbutton= Button()                                    
                exitbutton.createButton(0,700,100,670).draw(win3)       #Cria rectângulo para o botão de Exit
                exitbutton.createText(0,700,100,670,"EXIT").draw(win3)  #Escreve EXIT no botão

                variavel = 1                 #É definida aqui mais uma variável para o loop infinito de simulação até o utilizador clicar EXIT
                while variavel==1:
                    click = win3.getMouse()  #Deteta click e atribui coordenadas
                    clickX = click.getX()    #X do click
                    clickY = click.getY()    #Y do click
                    

                    ext=exitbutton.Clicked(clickX,clickY,100,670)    #Deteta se foi clicado o botão EXIT

                    if ext == 'continue':                         #Caso não tenha sido clicado, o click transforma-se num Ponto de Sujidade

                        robot.limpa_sala_Imp3(20,20,mobilia1,mobilia2,mobilia3,700,1100) #limpa a sala na totalidade
                        block= Rectangle(Point(200,300),Point(900,400))
                        block.setFill('white')
                        block.setOutline('black')
                        block.draw(win3)
                        text= Text(Point(550,350),'Escolha 1 Ponto de Sujidade')
                        text.setFace("courier")
                        text.setStyle("bold")
                        text.setTextColor('black')
                        text.draw(win3)
                        time.sleep(6)                   #Este código acima cria uma mensagem pop up após o aspirador se carregar que durante 6 segundos avisa o utilizador para escolher 1 ponto de sujidade
                        block.undraw()
                        text.undraw()
                        p = win3.getMouse()  #Deteta click e atribui coordenadas
                        pX = p.getX()        #X do click
                        pY = p.getY()        #Y do click

                        while mobilia2.y1-60<pY<mobilia2.y2+60 and mobilia2.x1-60<pX<mobilia2.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                            p = win3.getMouse()  
                            pX = p.getX()    
                            pY = p.getY()    
                        while mobilia1.y1-60<pY<mobilia1.y2+60 and mobilia1.x1-60<pX<mobilia1.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                            p = win3.getMouse()  
                            pX = p.getX()    
                            pY = p.getY()
                        while mobilia3.y1-60<pY<mobilia3.y2+60 and mobilia3.x1-60<pX<mobilia3.x2+60:        #Deteta se o click foi feito em cima de uma móvel, se for esse o caso aguarda novo click
                            p = win3.getMouse()  
                            pX = p.getX()    
                            pY = p.getY()
                        while pY>700-20 or pY<20 or pX>1100-20 or pX<20:        #Deteta se o click foi feito demasiado perto da parede, se for esse o caso aguarda novo click
                                p = win3.getMouse()  
                                pX = p.getX()    
                                pY = p.getY()

                        pontodesuj=Point(pX,pY)           #Definição do ponto de sujidade e das suas propriedades
                        pontodesuj.setFill('red')
                        pontodesuj.setOutline('red')
                        pontodesuj.draw(win3)

                        pX,pY=pontoParede(pX,pY)
                        robot.buscaPonto_Imp3(pX,pY,mobilia1,mobilia2,mobilia3,700,1100)
                        robot.limpaPonto(pX,pY,pontodesuj)   
                        robot.retornaBase_Imp3(20,20,mobilia1,mobilia2,mobilia3,700,1100)        
                        
                        
                    if ext =='clicked':             #Clicou Exit, sai da simulação e volta ao menu inicial
                        win3.close()
                        break
                
            
        if opt == 'button4':                    #Clicou exit, sai da aplicação
         win.close()
         break
        

            
    
    

main()
    