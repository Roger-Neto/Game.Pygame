import pygame

#inicio
try:
    pygame.init()
except:
    print("Erro")

#tela
x=640
y=480

#cores
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

#variaveis game
clock=0
room=0
itens_end_1=0
itens_end_2=0
itens_end_3=0
itens_end_4=0
itens_end_T=0
m1911=0
bottle=0
note1=0
note2=0
note3=0

#textos
rooms={"intro1":'''16 de agosto de 1919. Hoje eu me apressei para com os
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
buracos.''',
       "intro2":'''A tarde foi revigorante. O almoço sob as árvores e a
música alegrou o lugar, tornando a tarde mais refrescante.
Casais dançaram pelo pátio externo, incluindo Elliot e sua
esposa, Carmem. Como ele já tinha me descrito: Carmem
estava linda e sorridente, dançando levemente nos braços
dele. Seus olhos tinham um brilho jovial, mas um tanto
misterioso. Não esperava nada de diferente, já que Elliot
sempre gostou de mistérios. Mas chamou ainda mais
atenção o discurso... &quot;Enfático&quot;, se podemos dizer assim,
do pai de Elliot, Adam, ou como ele prefere, Coronel Ferri. Altivo, sério e com um tom autoritário e intimidador, ele fez
um discurso curto, típico de um ex-militar. Um rosto severo,
com rugas de preocupação, apesar de não ser tão velho.
Um bigode grande e largo completava aquela face
conhecida e temida. Antes do almoço ele fez o seu
discurso, parabenizando Elliot por seu aniversário e pela
sua promoção recente para o cargo de investigador chefe
na polícia de Nova Orleans.''',
       "intro3":'''Seguido do almoço, Elliot me chamou a um reservado,
apresentando sua família a mim devidamente. Já conhecia
a muito seu pai, contudo, a mim foi apresentada a sua nova
esposa, Veronica. Uma mulher jovem, seria como o pai de
Elliot, porém com um ar mais gracioso que apenas uma
dama pode deter. Ele também me convidou para participar
do jantar daquela noite, ainda ali, na propriedade,
destinado apenas a pessoas próximas e familiares. Apesar
das pesadas nuvens no céu, decidi ficar.''',
       "intro4":'''O jantar decorreu de uma forma mais branda, lenta e
solene. As pessoas conversavam de forma baixa, mas
ocorreu um problema. Com o decorrer do jantar, tais vinhos
e carnes me destrairam, e acabei não percebendo a
tempestade que se aproximava. Ao fim do jantar, a estrada
de volta era um grande lamaçal e, como previsto, eu não
tinha uma forma de voltar a cidade. Elliot e Carmem se
ofereceram a me abrigar naquele dia, me oferecendo o
quarto de hóspedes. Uma gentileza indescritível.''',
       "intro5":'''Aproveitamos a noite, já que eu dormiria lá. Tomamos chá
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
tempo, estendido no chão frio, pálido e morto.''',
       "living":"",
       "bed1":"",
       "bed2":"",
       "kitchen":"",
       "bath":""
       "note1":"",
       "note2":"",
       "note3":"",
      }

#modulos
back=pygame.display.set_mode((x,y))
pygame.display.set_caption("ASSASSINATO")
font=pygame.font.SysFont(None,30)
def text(msg,color):
    text1=font.render(msg,True,color)
    fundo.blit(text1,[x/2,y/2])

#funções
def intro(mcqueen):
def bed1(room):
def bed2(room):
def living(room):
def kitchen(room):
def bath(room):

def mv
def mv
def mv
def mv
def mv
def mv
def mv
def mv
def mv
def mv
def mv

def play():
    exit=True
    while exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=False
            if event.type==pygame.KEYDOWN:
            if event.key==pygame.
            if event.key==pygame.K_0:
                exit=False
            if event.key==pygame.K_1:
                room=1
                def living()
            if event.key==pygame.K_2:
            if event.key==pygame.K_3:
            if event.key==pygame.K_4:
            if event.key==pygame.K_5:

        back.fill(back_color)
        relogio.trick(20)
        pygame.display.update()

    pygame.quite()