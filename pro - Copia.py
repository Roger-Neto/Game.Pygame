##NOTA DE CONSIDERAÇÃO
##Olá! Eu sou um iniciante em pygame e ggostaria de
##utilizar desse espaço para algumas declarações.
##Devo dar nota que o teclado está quebrado
##(para sofrimento único e exclusivo meu, claro).
##A primeira coisa é: pygame não é uma engine convidativa.
##A forma de instalação (em pip), pode ser comum  para dev's
##que trabalham em python, mas não é nada fácil para um
##iniciante. A forma de aplicação das funções e a falta de
##praticiade em muitas delas é muitoo desconfortavel e complexa
##de forma desnecessária muita das vezes(ao meu ver).
##Tendo adicionado isso durante a criação desse projeto, espero que,
##com o tempo e com mais experiência, no futuro próximo eu possa tirar
##essa nota de dor e pesar.
##
##Aqui também deixo meus agradecimentos aos tutoriais no youtube,
##aos deuuses ddos forruns e um agrradecimentto especial para todos os
##senhores e senhoras do stackoverflow (principalmente os do pt. S2 amo vcs).
##
##ass. Um Dev Noob.

import pygame

##inicio
try:
    pygame.init()
except:
    print("Erro")

##tela
x=640
y=480

##cores
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
orange=(255,165,0)
purple=(128,0,128)
brown=(165,42,42)
yellow=(255,255,0)
back_color=(0,0,50)

##variaveis game
clock=0
room=0
choice=0

itens_end_1=0
itens_end_2=0
itens_end_3=0
itens_end_4=0
itens_end_T=0

prove_m1911=0
prove_flask=0
prove_knife=0
prove_note1=0
prove_note2=0
prove_note3=0

c_intro=0
c_action=0

##textos
intro1='''16 de agosto de 1919. Hoje eu me apressei para com os
eventos diários, já que ao final da tarde eu teria um
compromisso. Hoje é o aniversário de meu caro amigo
Elliot, quem não vejo a muito, e eu fui convidado para a sua
festa de aniversário, nos jardins de sua magnífica
propriedade familiar, uma casa de campo no Bayou. Uma
viagem de avião é deveras exaustante, mas não há nada
que eu não possa fazer por ele. Elliot já é amigo a muito
tempo, desde os tempos de colégio e faculdade, em
Boston. Ambos seguimos o direito, mas por ramos
diferentes. Ele decidiu ser um policial, e hoje vive nessa
quente e úmida cidade, junto a sua esposa. Após finalizar
meu serviço de sábado, fui buscar uma forma de seguir o
caminho. Uma carroça foi a forma mais prática encontrada
para percorrer por aquelas estradas irregulares e cheias de
buracos.
PRESSIONE ESPAÇO PARA PROSSEGUIR'''
intro2='''A tarde foi revigorante. O almoço sob as árvores e a
música alegrou o lugar, tornando a tarde mais refrescante.
Casais dançaram pelo pátio externo, incluindo Elliot e sua
esposa, Carmem. Como ele já tinha me descrito: Carmem
estava linda e sorridente, dançando levemente nos braços
dele. Seus olhos tinham um brilho jovial, mas um tanto
misterioso. Não esperava nada de diferente, já que Elliot
sempre gostou de mistérios. Mas chamou ainda mais
atenção o discurso... &quot;Enfático&quot;, se podemos dizer assim,
do pai de Elliot, Adam, ou como ele prefere, Coronel Ferri.
Altivo, sério e com um tom autoritário e intimidador, ele fez
um discurso curto, típico de um ex-militar. Um rosto severo,
com rugas de preocupação, apesar de não ser tão velho.
Um bigode grande e largo completava aquela face
conhecida e temida. Antes do almoço ele fez o seu
discurso, parabenizando Elliot por seu aniversário e pela
sua promoção recente para o cargo de investigador chefe
na polícia de Nova Orleans.
PRESSIONE ESPAÇO PARA PROSSEGUIR'''
intro3='''Seguido do almoço, Elliot me chamou a um reservado,
apresentando sua família a mim devidamente. Já conhecia
a muito seu pai, contudo, a mim foi apresentada a sua nova
esposa, Veronica. Uma mulher jovem, seria como o pai de
Elliot, porém com um ar mais gracioso que apenas uma
dama pode deter. Ele também me convidou para participar
do jantar daquela noite, ainda ali, na propriedade,
destinado apenas a pessoas próximas e familiares. Apesar
das pesadas nuvens no céu, decidi ficar.
PRESSIONE ESPAÇO PARA PROSSEGUIR'''
intro4='''O jantar decorreu de uma forma mais branda, lenta e
solene. As pessoas conversavam de forma baixa, mas
ocorreu um problema. Com o decorrer do jantar, tais vinhos
e carnes me destrairam, e acabei não percebendo a
tempestade que se aproximava. Ao fim do jantar, a estrada
de volta era um grande lamaçal e, como previsto, eu não
tinha uma forma de voltar a cidade. Elliot e Carmem se
ofereceram a me abrigar naquele dia, me oferecendo o
quarto de hóspedes. Uma gentileza indescritível.
PRESSIONE ESPAÇO PARA PROSSEGUIR''',
intro5='''Aproveitamos a noite, já que eu dormiria lá. Tomamos chá
com biscoitos, preparado por Carmem e Veronica,
conversamos sobre o tempo que ficamos separado, o que
fizemos depois da faculdade e o dia a dia no trabalho,
apesar dos dias dele serem mais interessante. Próximo da
hora de nos recolhermos, quando Carmem já tinha
preparado o banho para Elliot se deitar, houve uma
inesperada queda de energia, já que a tempestade já tinha
enfraquecido. No desespero, batemos em móveis ao tentar
circular pela sala e procurar velas e lamparinas. Depois de
algum tempo, escuto um urro vindo do meio da sala e um
baque. Rapidamente, passando as mãos por dentro das
gavetas, eu encontro velas e algumas caixas de fósforo,
mas, assim que acendo o pavio escuto o grito de Veronica
e vejo Carmem cair ao meu lado. Ao olhar para trás, vejo
no chão da sala o corpo de Elliot, meu amigo de tanto
tempo, estendido no chão frio, pálido e morto.
PRESSIONE ESPAÇO PARA PROSSEGUIR'''
##living=''''''
##bed1=''''''
##bed2=''''''
##kitchen=''''''
##bath=''''''
##end1=''''''
##end2=''''''
##end3=''''''
##end4=''''''
##endT=''''''
##
##moveis e objetos
##t.body=''''''
##t.mv_sofa=''''''
##t.mv_bookcs=''''''
##t.mv_armchair=''''''
##t.mv_desk=''''''
##t.mv_cabinet=''''''
##t.mv_cooker=''''''
##t.mv_sink=''''''
##t.mv_bed=''''''
##t.mv_wardrobe=''''''
##t.mv_nightstand=''''''
##
##provas
##m1911=''''''
##knife=''''''
##flask=''''''
##note1=''''''
##note2=''''''
##note3=''''''


##modulos
back=pygame.display.set_mode((x,y))
pygame.display.set_caption("Assassinatos em  N.O.")
font=pygame.font.SysFont(None,30)
def text(msg,color):
    text1=font.render(msg,True,color)
    fundo.blit(text1,[x/2,y/2])

##FUNÇÕES
##comodos
def intro1(escolha):
    text([intro1], purple)
def intro2(escolha):
    text([intro1], purple)
def intro3(escolha):
    text([intro1], purple)
def intro4(escolha):
    text([intro1], purple)
def intro5(escolha):
    text([intro1], purple)
def living():
    text(living,yellow)
    choice=int(imput)
    if choice not in '1234':
        error_choice
    room=1
    if choice==1:
        mv_body()
    if choice==2:
        mv_bookcs()
    if choice==3:
        mv_armchair()
    if choice==4:
        mv_sofa
def kitchen():
    text(living,yellow)
    choice=int(imput)
    if choice not in '1234':
        error_choice
    room=1
    if choice==1:
        mv_cooker()
    if choice==2:
        mv_cabinet()
    if choice==3:
        mv_sink()
    if choice==4:
        mv_desk()
def bath():
    text(bath,yellow)
    choice=int(imput)
    if choice not in '12':
        error_choice
    room=1
    if choice==1:
        mv_sink()
    if choice==2:
        mv_cabinet()
def bed1():
    text(bed1,yellow)
    choice=int(imput)
    if choice not in '123':
        error_choice
    room=1
    if choice==1:
        mv_bed()
    if choice==2:
        mv_wardrobe()
    if choice==3:
        mv_nightstand()
def bed2():
    text(bed2,yellow)
    choice=int(imput)
    if choice not in '123':
        error_choice
    room=1
    if choice==1:
        mv_bed()
    if choice==2:
        mv_wardrobe()
    if choice==3:
        mv_nightstand()

def error_choice():
    text("Escolha entre as opções dadas ou digite 0 para sair",red)
    

##moveis
def body():
    text(t.body,purple)
    
def mv_sofa(room):
    text(knife,blue)
    prove_knife+=1
    return prove_knife

def mv_bookcs():
    text(t.mv_body)
    
def mv_armchair(room):
    if room==1:
        text(note,blue)
    prove_note1 = prove_note1+1
    return prove_note1

def mv_desk():
    text(t.mv_desk,purple)

def mv_cabinet(room):
    if room==4:
        text(note2,blue)
    prove_note2 = prove_note2+1
    return prove_note2

def mv_cooker():
    text(t.mv_cooker,purple)
def mv_sink(room):
    if room==5:
        text(flask,blue)
    prove_flask = prove_flask+1
    return prove_flask

def mv_bed(room):
    if room==2:
        text(m1911,blue)
    prove_m1911 = prove_m1911+1
    return prove_m1911

def mv_wardrobe():
    text(t.mv_wardrobe,purple)
    
def mv_nightstand(room):
    if room==3:
        text(note3,blue)
    prove_note3 = prove_note3+1
    return prove_note3

##Finais
def proves(prove_m1911,prove_flask,prove_knife,prove_note1,prove_note2,prove_note3):
    if prove_note1>0 and prove_knife>0:
        itens_end_2=1
        return itens_end_2
    if prove_note2>0 and prove_flask>0:
        itens_end_3=1
        return itens_end_3
    if prove_note3>0 and prove_knife>0:
        itens_end_4=1
        return itens_end_4
    if prove_nota1>0 and prove_nota2>0 and provee_nota3>0 and prove_m1911>0 and prove_flask>0:
        itens_end_T=1
        return itens_end_T
    if itens_end_4==1 == itens_end_2==1:
        itens_end_1=1
        return itens_end_1
    if itens_end_2==1 == itens_end_3==1:
        itens_end_1=1
        return itens_end_1
    if itens_end_4==1 == itens_end_3==1:
        itens_end_1=1
        return itens_end_1
    if itens_end_4==1 == itens_end_3==1 and itens_end_4==1 and itens_end_2==1:
        itens_end_1=1
        return itens_end_1
        
def end(itens_end_1,itens_end_2,itens_end_3,itens_end_4,itens_end_T):
    if itens_end_4 > itens_end_2 and itens_end_3 and itens_end4:
        text(end4, blue)
    if itens_end_3 > itens_end_2 and itens_end_3 and itens_end4:
        text(end3, green)
    if itens_end_2 > itens_end_2 and itens_end_3 and itens_end4:
        text(end2, purple)
    if itens_end_1 > itens_end_2 and itens_end_3 and itens_end4:
        text(end1, red)
    if itens_end_T > itens_end_1 or itens_end_2 or itens_end_3 or itens_end_4:
        text(endT, yellow)
def play():
    exit=True
    while exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=False
            text("aperte 0 para sair", green)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_0:
                    exit=False
                if event.type==pygame.K_BACKSPACE:
                    if c_intro==0:
                        intro1()
                        c_intro+=1
                    if c_intro==1:
                        intro2()
                        c_intro+=1
                    if c_intro==2:
                        intro3()
                        c_intro+=1
                    if c_intro==3:
                        intro4()
                        c_intro+=1
                    if c_intro==4:
                        intro5()
                        c_intro+=1
                if event.key==pygame.K_1:
                    room=1
                    c_action+=1
                    living()
                if event.key==pygame.K_2:
                    room=2
                    c_action+=1
                    bed1()
                if event.key==pygame.K_3:
                    room=3
                    c_action+=1
                    bed2()
                if event.key==pygame.K_4:
                    room=4
                    c_action+=1
                    kitchen()
                if event.key==pygame.K_5:
                    room=5
                    c_action+=1
                    bath()
            if c_action==50:
                proves()

        back.fill(back_color)
        relogio.trick(20)
        pygame.display.update()

    pygame.quite()
