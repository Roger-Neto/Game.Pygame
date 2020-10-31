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
##aos deuses dos fóruns e um agradecimentto especial para todos os
##senhores e senhoras do stackoverflow (principalmente os do pt. S2 amo vcs).
##
##ass. Um Dev Noob.

##Adaptação para o codigo funcionando sem o modulo pygame

##TEXTOS

t_tutorial='''Utilize o teclado númerico no jogo.
DIGITE UM NÚMERO ENTRE 1 E 5 PARA CONTINUAR OU 6 PARA SAIR'''
t_intro1='''16 de agosto de 1919. Hoje eu me apressei para com os
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
DIGITE UM NÚMERO ENTRE 1 E 5 PARA CONTINUAR OU 6 PARA SAIR'''

t_intro2='''A tarde foi revigorante. O almoço sob as árvores e a
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
DIGITE UM NÚMERO ENTRE 1 E 5 PARA CONTINUAR OU 6 PARA SAIR'''

t_intro3='''Seguido do almoço, Elliot me chamou a um reservado,
apresentando sua família a mim devidamente. Já conhecia
a muito seu pai, contudo, a mim foi apresentada a sua nova
esposa, Veronica. Uma mulher jovem, seria como o pai de
Elliot, porém com um ar mais gracioso que apenas uma
dama pode deter. Ele também me convidou para participar
do jantar daquela noite, ainda ali, na propriedade,
destinado apenas a pessoas próximas e familiares. Apesar
das pesadas nuvens no céu, decidi ficar.
DIGITE UM NÚMERO ENTRE 1 E 5 PARA CONTINUAR OU 6 PARA SAIR'''

t_intro4='''O jantar decorreu de uma forma mais branda, lenta e
solene. As pessoas conversavam de forma baixa, mas
ocorreu um problema. Com o decorrer do jantar, tais vinhos
e carnes me destrairam, e acabei não percebendo a
tempestade que se aproximava. Ao fim do jantar, a estrada
de volta era um grande lamaçal e, como previsto, eu não
tinha uma forma de voltar a cidade. Elliot e Carmem se
ofereceram a me abrigar naquele dia, me oferecendo o
quarto de hóspedes. Uma gentileza indescritível.
DIGITE UM NÚMERO ENTRE 1 E 5 PARA CONTINUAR OU 6 PARA SAIR'''

t_intro5='''Aproveitamos a noite, já que eu dormiria lá. Tomamos chá
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
DIGITE UM NÚMERO ENTRE 1 E 5 PARA CONTINUAR OU 6 PARA SAIR'''

t_living='''Todos ainda estão na sala, contudo,
afastados do corpo e dos móveis na sala temos apenas um sofá,
uma poltrona, uma estante e… o corpo dele.'''

t_kitchen='''A cozinha está vazia.
Alguns armário, uma mesa e o fogão ainda quente'''

t_bath='''O banheiro é um pouco apertado.
Uma ducha, um vaso, a pia e um  pequeno armário.'''

t_bed1='''O quarto principal é grande, mas
tem  poucos elementos: a cama, um guarda roupa e criados  mudos.
Estamos em  uma casa de campo, afinal.'''

t_bed2='''O quarto de hóspedes é um pouco apertado e têm
poucos elementos: a cama, um guarda roupa e criados  mudos.
Estamos em  uma casa de campo, afinal.'''

t_end1='''Depois da noite, tentei juntar as peças. Pensei bastante. O
resultado...
Foi inútil. Sem provas, não pude encontrar o assassino.
A culpa me consome até hoje. Me perdoe, Elliot...'''

t_end2='''Depois da noite, tentei juntar as peças. Pensei bastante. O
resultado...
Foi único. As provas me levaram a pensar em apenas
um culpado: Adam Ferri. Apesar de ser pai de Elliot,
tudo levava a ele. Ainda havia pontas soltas, mas nem
eu nem a polícia chegamos a algum resultado. Adam
foi preso e condenado pelo assassinato de Elliot Ferri,
cometido na noite de 16 de agosto de 1919.'''

t_end3='''Depois da noite, tentei juntar as peças. Pensei bastante. O
resultado...\n
Foi único. As provas me levaram a pensar em apenas
uma culpada: Carmem Ferri. Apesar de ser esposa de
Elliot, tudo levava a ela. Ainda havia pontas soltas, mas
nem eu nem a polícia chegamos a algum resultado.
Carmem foi presa e condenada pelo assassinato de
Elliot Ferri, cometido na noite de 16 de agosto de 1919.'''

t_end4='''Depois da noite, tentei juntar as peças. Pensei bastante. O
resultado...
Foi único. As provas me levaram a pensar em apenas
uma culpada: Veronica Ferri. Apesar de ser madrasta de
Elliot, tudo levava a ela. Ainda havia pontas soltas, mas
nem eu nem a polícia chegamos a algum resultado.
Apesar de se declarar inocente, Veronica foi presa e
condenada pelo assassinato de Elliot Ferri, cometido
na noite de 16 de agosto de 1919.
'''
t_endT='''Depois da noite, tentei juntar as peças. Pensei bastante. O
resultado...
Fez tudo fazer sentido. Elliot estava tendo um caso
com a sua madrasta, Veronica. Carmem e Adam
descobriam a traição deles e decidiram se vingar. Em
interrogatório o Coronel foi impassível. Carmem,

porém, abriu logo a boca. Ela e o Coronel planejaram a
vingança contra ambos. Eles os matariam naquela
noite com o Nitroprussiato, mas Veronica acabou
vomitando o veneno. O desespero assustou Carmem,
que pensou em dar um fim rápido em Elliot. O veneno
já estava atuando nele, porém, ela decidiu dar uma
facada. Acabou dando errado, naquele escuro. Uma
vingança desnecessária, já que, de acordo com
Carmem, ela e o Coronel deitaram-se juntos antes,
quando descobriram, mas o fogo da vingança não se
apagou tão facilmente. Ambos foram condenados por
homicídio qualificado, deixando uma mulher solitária e
uma casa vazia em um pântano de amargura.'''

t_body='''O que aconteceu com ele? Quem poderia ter feito isso?!
Ele parece ter uma ferida... Um corte nas costas... Parece...
Não sei, não parece fatal...'''
t_mv_bookcs='''Livros, bibelôs e pastas. Era típico dele ser
desorganizado...'''
t_mv_desk='''Brachela de chá e alguns biscoitos. Nada de
mais.'''
t_mv_cabinet='''Cerais e grãos. Algumas latas também. Parece que tem
o bastante pra muito tempo.'''
t_mv_cooker='''Cinzas e... '''
t_mv_sink='''Nenhuma goteira por aqui.'''
t_mv_bed='''Lençóis esticados e bem arrumados. Perfeito.'''
t_mv_wardrobe='''Não tem nenhuma peça. Vazio, como pensei.'''
t_mv_nightstand='''Vazia. Um pouco bem cuidado, mas ainda tem poeira nas
gavetas.'''

t_m1911='''Meu Deus! Uma M1911? Por quê isso aqui?
Calma... Está vazia? O pente está aqui, mas... Ainda tem
uma bala na agulha...'''
t_knife='''O que é isso aqui emmbaixo? Uma faca... Está cheia de
sangue!'''
t_flask='''"Nitroprussiato"?Eu não me lembro de Elliot
tomar remédios...'''
t_note1='''O quê é isso, um bilhete? "Me encontre amanhã.
Quero lhe ver, estou com saudades. Assinado, A"...
Curioso...'''
t_note2='''Papel queimado...Talvez alguém esteja escondendo algo aqui...'''
t_note3='''Uma carta. Endereçada para Veronica?
"Amada Veronica,
Não consigo mais resistir aos dias nessa casa fria.
Desde aquela noite não paro de pensar em você, no
perfume da sua pele, no calor do seu corpo. Irei me
afastar de Carmem se é isso que você quer. Por favor,
quero lhe ver novamente. Velha ao café da última vez.
Lhe encontrarei lá na segunda, às 10:00, e de lá
sairemos dessa cidade e dessa vida maldita com a
única coisa que importa: nós dois.
Com amor,
Elliot"
Mas, com a própria madrasta?!'''

##Variaveis aplicadas no jogo

room=0
a_cont=0 ##contadora de ações
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

##JOGO

##funções
def tutorial():
    print(f'{t_tutorial}')
    choice=(input(''))
    if choice=='6':
        game_over=0
        return game_over
    else:
        if choice in '12345':
            intro1()
        else:
            print("Digite um número válido nas opções ou digite 6 para sair")
            tutorial()
        
def intro1():
    print(f'{t_intro1}')
    choice=(input(''))
    if choice=='6':
        game_over=0
        return game_over
    else:
        if choice in '12345':
            intro2()
        else:
            print("Digite um número válido nas opções ou digite 6 para sair")
            intro1()

def intro2():
    print(f'{t_intro2}')
    choice=(input(''))
    if choice=='6':
        game_over=0
        return game_over
    else:
        if choice in '12345':
            intro3()
        else:
            print("Digite um número válido nas opções ou digite 6 para sair")
            intro2()

def intro3():
    print(f'{t_intro3}')
    choice=(input(''))
    if choice=='6':
        game_over=0
        return game_over
    else:
        if choice in '12345':
            intro4()
        else:
            print("Digite um número válido nas opções ou digite 6 para sair")
            intro3()

def intro4():
    print(f'{t_intro4}')
    choice=(input(''))
    if choice=='6':
        game_over=0
        return game_over
    else:
        if choice in '12345':
            intro5()
        else:
            print("Digite um número válido nas opções ou digite 6 para sair")
            intro4()

def intro5():
    print(f'{t_intro5}')
    choice=(input(''))
    if choice=='6':
        game_over=0
        return game_over
    else:
        if choice in '12345':
            living()
        else:
            print("Digite um número válido nas opções ou digite 6 para sair")
            intro5()

############################################################################

def end():
    if prove_note1>0 and prove_knife>0:
        print(f'{t_end2}')
        game_over=0
        return game_over

    elif prove_note2>0 and prove_flask>0:
        print(f'{t_end3}')
        game_over=0
        return game_over

    elif prove_note3>0 and prove_knife>0:
        print(f'{t_end4}')
        game_over=0
        return game_over

    elif prove_nota1>0 and prove_nota2>0 and prove_nota3>0 and prove_m1911>0 and prove_flask>0:
        print(f'{t_endT}')
        game_over=0
        return game_over

    elif itens_end_4 == itens_end_2:
        print(f'{t_end1}')
        game_over=0
        return game_over

    elif itens_end_2 == itens_end_3:
        print(f'{t_end1}')
        game_over=0
        return game_over

    elif itens_end_4 == itens_end_3:
        print(f'{t_end1}')
        game_over=0
        return game_over

    elif itens_end_4 == itens_end_3 and itens_end_4 == itens_end_2:
        print(f'{t_end1}')
        game_over=0
        return game_over

############################################################################

def body():
    global a_cont
    print(f'{t_body}')
    a_cont+=1
    if a_cont>=50:
        end()
    else:
        return a_cont
        living()

def mv_sofa():
    global a_cont
    global prove_knife
    print(f'{t_prove_knife}')
    prove_knife+=1
    a_cont+=1
    if a_cont>=50:
        end()
    else:
        return prove_knife and a_cont
        living()

def mv_bookcs():
    global a_cont
    print(f'{t_mv_bookcs}')
    a_cont+=1
    if a_cont>=50:
        end()
    else:
        return a_cont
        living()

def mv_armchair():
    global a_cont
    global prove_note1
    print(f'{t_note1}')
    prove_note1+=1
    a_cont = a_cont+1
    if a_cont>=50:
        end()
    else:
        return prove_note1 and a_cont
        living()

def mv_desk():
    global a_cont
    print(f'{t_mv_desk}')
    a_cont+=1
    if a_cont>=50:
        end()
    else:
        return a_cont
        kitchen()

def mv_cabinet(room):
    global a_cont
    global prove_note2
    a_cont+=1
    if room==2:
        print(f'{t_note2}')
        prove_note2+=1
        if a_cont>=50:
            return prove_note2
            end() 
        else:
            return a_cont and prove_note2
            kitchen()
    else:
        print(f'{t_mv_cabinet}')
        if a_cont>=50:
            end() 
        else:
            return a_cont
            bath()

def mv_cooker():
    global a_cont
    print(f'{t_mv_cooker}')
    a_cont+=1
    if a_cont>=50:
        end()
    else:
        return a_cont
        kitchen()

def mv_sink(room):
    global a_cont
    global prove_flask
    a_cont+=1
    if room==3:
        print(f'{t_flask}')
        prove_flask+=1
        if a_cont>=50:
            return prove_flask
            end() 
        else:
            return prove_flask and a_cont
            bath()
    else:
        print(f'{t_mv_sink}')
        if a_cont>=50:
            end()
        else:
            return a_cont 
            kitchen()   

def mv_bed(room):
    global a_cont
    global prove_m1911
    a_cont+=1
    if room==2:
        print(f'{t_m1911}')
        prove_m1911+=1
        if a_cont>=50:
            return prove_m1911
            end() 
        else:
            return prove_m1911 and a_cont
            bed2() 
    else:
        print(f'{t_mv_bed}')
        if a_cont==50:
            end()
        else:
            return a_cont
            bed1()     

def mv_wardrobe():
    global a_cont
    print(f'{t_mv_wardrobe}')
    a_cont+=1
    if a_cont==50:
        end()
    else:
        if room==4:
            return a_cont
            bed1()
        if room==5:
            return a_cont
            bed2()

def mv_nightstand(room):
    global a_cont
    global prove_note3
    a_cont+=1
    if room==4:
        print(f'{note3}')
        prove_note3+=1
        if a_cont==50:
            end()
        else:
            return a_cont and prove_note3
            bed1()
    else:
        print(f'{t_mv_nightstand}')
        if a_cont==50:
            end()
        else:
            if room==4:
                return a_cont
                bed1()
            if room==5:
                return a_cont
                bed2()

############################################################################

def living():
    global a_cont
    global game_over
    global room
    print(f'{t_living}')
    choice=(input('''Para onde?\n 
    1-Investigar móveis\n 
    2-Ir para a cozinha\n 
    3-Ir para o banheiro\n 
    4-Ir para o quarto principal\n 
    5-Ir para o quarto de hóspedes\n'''))
    if choice not in '123456':
        print("Digite um número válido nas opções ou digite 6 para sair")
        living()
    else:
        if choice=='6':
            game_over=0
            return game_over
        else:
            a_cont+=1
            if choice=='2':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    kitchen()
            elif choice=='3':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bath()
            elif choice=='4':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed1()
            elif choice=='5':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed2()
            elif choice=='1':
                choice=(input("O que investigar agora?\n"))
                if choice not in '12346':
                    print("Digite um número válido nas opções ou digite 6 para sair")
                    living()
                else:
                    if choice=='6':
                        game_over=0
                        return game_over
                    else:
                        room = 1
                        a_cont+=1
                        if a_cont>=50:
                            end()
                        else:
                            return room and a_cont
                            if choice=='1':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_body()
                            elif choice=='2':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_bookcs()
                            elif choice=='3':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_armchair()
                            elif choice=='4':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_sofa()

def kitchen():
    global a_cont
    global game_over
    global room
    print(f'{t_kitchen}')
    choice=(input('''Para onde?\n 
    1-Ir para a sala\n 
    2-Investigar móveis\n 
    3-Ir para o banheiro\n 
    4-Ir para o quarto principal\n 
    5-Ir para o quarto de hóspedes\n'''))
    if choice not in '123456':
        print("Digite um número válido nas opções ou digite 6 para sair")
        kitchen()
    else:
        if choice=='6':
            game_over=0
            return game_over
        else:
            a_cont+=1
            if choice=='1':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    living()
            elif choice=='3':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bath()
            elif choice=='4':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed1()
            elif choice=='5':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed2()
            elif choice=='2':
                choice=(input("O que investigar agora?\n"))
                if choice not in '1236':
                    print("Digite um número válido nas opções ou digite 6 para sair")
                    kitchen()
                else:
                    if choice=='6':
                        game_over=0
                        return game_over
                    else:
                        room=2
                        a_cont+=1
                        if a_cont>=50:
                            end()
                        else:
                            return room and a_cont
                            if choice>='1':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_cooker()
                            if choice>='2':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_sink()
                            if choice>='3':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_desk()

def bath():
    global a_cont
    global game_over
    global room
    print(f'{t_bath}')
    choice=(input('''Para onde?\n 
    1-Ir para a sala\n 
    2-Ir para o cozinha\n 
    3-Investigar móveis\n 
    4-Ir para o quarto principal\n 
    5-Ir para o quarto de hóspedes\n'''))
    if choice not in '123456':
        print("Digite um número válido nas opções ou digite 0 para sair")
        bath()
    else:
        if choice=='6':
            game_over=0
            return game_over
        else:
            if choice=='1':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    living()
            elif choice=='2':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    kitchen()
            elif choice=='4':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed1()
            elif choice=='5':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed2()
            elif choice=='3':
                choice=(input("O que investigar agora?\n"))
                if choice not in '126':
                    print(f'Digite um número válido nas opções ou digite 6 para sair')
                    bath()
                else:
                    if choice=='6':
                        game_over=0
                        return game_over
                    else:
                        room=3
                        a_cont+=1
                        if a_cont>=50:
                            end()
                        else:
                            return room and a_cont
                            if choice=='1':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_sink()
                            if choice=='2':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_cabinet()

def bed1():
    global a_cont
    global game_over
    global room
    print(f'{t_bed1}')
    choice=(input('''Para onde?\n 
    1-Ir para a sala\n 
    2-Ir para o cozinha\n 
    3-Ir para o banheiro\n 
    4-Investigar móveis\n 
    5-Ir para o quarto de hóspedes\n'''))
    if choice not in '123456':
        print("Digite um número válido nas opções ou digite 6 para sair")
        bed1()
    else:
        if choice=='6':
            game_over=0
            return game_over
        else:
            if choice=='1':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    living()
            elif choice=='2':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    kitchen()
            elif choice=='3':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bath()
            elif choice=='5':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed2()
            elif choice=='4':
                choice=(input("O que investigar agora?\n"))
                if choice not in '1236':
                    print(f'Digite um número válido nas opções ou digite 6 para sair')
                    bed1()
                else:
                    if choice=='6':
                        game_over=0
                        return game_over
                    else:
                        room=4
                        a_cont=a_cont+1
                        if a_cont>=50:
                            end()
                        else:
                            return room and a_cont
                            if choice=='1':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_bed()
                            if choice=='2':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_wardrobe()
                            if choice=='3':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_nightstand()

def bed2():
    global a_cont
    global game_over
    global room
    print(f'{t_bed2}')
    choice=(input('''Para onde?\n 
    1-Ir para a sala\n 
    2-Ir para o cozinha\n 
    3-Ir para o banheiro\n 
    4-Ir para o quarto principal\n
    5-Investigar móveis\n'''))
    if choice not in '123456':
        print("Digite um número válido nas opções ou digite 6 para sair")
        bed2()
    else:
        if choice=='6':
            game_over=0
            return game_over
        else:
            a_cont+=1
            if choice=='1':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    living()
            elif choice=='2':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    kitchen()
            elif choice=='3':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bath()
            elif choice=='4':
                if a_cont>=50:
                    end()
                else:
                    return a_cont
                    bed1()
            elif choice=='5':
                choice=(input("O que investigar agora?\n"))
                if choice not in '1236':
                    print(f'Digite um número válido nas opções ou digite 6 para sair')
                    bed2()
                else:
                    if choice=='6':
                        game_over=0
                        return game_over
                    else:
                        room=5
                        a_cont+=1
                        if a_cont==50:
                            end()
                        else:
                            return room and a_cont
                            if choice=='1':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_bed()
                            if choice=='2':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_wardrobe()
                            if choice=='3':
                                if a_cont>=50:
                                    end()
                                else:
                                    return a_cont
                                    mv_nightstand()

############################################################################

##Play
tutorial()

game_over=1

if game_over==0:
    quit()
