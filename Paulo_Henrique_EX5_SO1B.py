#terminar sjf
#calcular tempo medio para sjf
'''Implementar os algoritmos de escalonamento:
1.	FCFS
2.	SJF
3.	SRTF
4.	Round Robin
5.	Multinível
a.	Primeiro nível RR
b.	Segundo nível FCFS
Para todos os algoritmos, deverão constar um menu para as seguintes entradas.
•	Quantidade de processos para simular
•	Tamanho do Burst do processo (manual ou arquivo)
•	Tempo de chegada, quando necessário
•	Prioridade, quando necessário
•	Quantum de tempo, quando necessário
Resultados
•	Lista dos processos com os seus burst, prioridades e tempo de chegada
•	Exibir o Waiting Time e Turnaround Time de cada processo no algoritmo
•	Exibir o Waiting Time médio
•	Exibir o Turnaround Time médio
Padrão Arquivo de Entrada de Dados
@nomeprocesso;burst;tempochegada;prioridade;quantum&
Arquivo para o FCFS
@p1;24;0;0;0&
@p2;3;0;0;0&
Arquivo para o STRF
@p1;8;2;0;0&
@p2;4;4;0;0&
Arquivo para o RR e multinível
@p1;80;0;0;10&
@p1;60;0;0;10&'''

    
import random
import operator

class Processo(object):
  def __init__(self, nome,burst,tcheg,prioridade,quantum):
      self.nome = nome
      self.burst = burst
      self.tcheg = tcheg
      self.prioridade = prioridade
      self.quantum = quantum
  
  def setNome(nome):
    self.nome = nome

  def setBurst(burst):
    self.burst = burst
  
  def setTcheg(tcheg):
    self.tcheg = tcheg

  def setPrioridade(prioridade):
    self.prioridade = prioridade

  def setQuantum(quantum):
    self.quantum = quantum
lista = []
def montaListaAutomatica(arquivo):
  for x in range(len(arquivo)):      
      processo = arquivo[x]
      processo = processo.split('@')[1]
      processo = processo.split('&')[0]
      processo = processo.split(';')

      nomeProcesso = processo[0] #p1
      nomeProcesso = nomeProcesso[1:]#pega apartir o p.. p2 -> 2, p23 -> 23
      burstProcesso = processo[1]
      tChegProcesso = processo[2]
      prioridadeProcesso = processo[3]
      quantumProcesso = processo[4]
      proc = Processo(int(x),int(burstProcesso),int(tChegProcesso),int(prioridadeProcesso),int(quantumProcesso))
      lista.append(proc)
      
  return lista
def tAroundRR(vetorRR):
  vetor = []
  for x in range(len(vetorRR)):
    pass

def desmonta(linha): #recebe nprocesso;burstprocesso sem o P-> 0;8
  linha = linha.split(';')
  numeroProcesso = int(linha[0])
  return numeroProcesso

def formaABostaDoNumero(palavra):
  string = ''
  for x in palavra:
    string += x
  return string
    
    
      
def imprimirResultado(lista,tipoEscalonamento):
  tAround = 0
  tEspera = 0
  tResposta = 0
  turnMedia = 0
  esperaMedia = 0
  qtotal = 0
  print ("Processo\tT.Burst\tT.Chegada\tTurnAround\tT.Resposta\tT.Espera")
  #INICIO FCFS/SJF-------------------------------------------------------------------------------------------
  if tipoEscalonamento == "FCFS/SJF":
    
    for x in lista:
      if int(x.nome) == 0: #caso seja o primeiro processo, tempo de espera, e o tempo de chegada
        tEspera = x.tcheg
      else:
        tEspera = tAround-int(x.tcheg)
      tAround += (int(x.burst)-int(x.tcheg))
      tResposta = tEspera #no fcfs, tempo de resposta é o mesmo de espera
      turnMedia += tAround
      esperaMedia += int(tEspera)
      
      print(int(x.nome)+1,"\t\t",x.burst,"\t",x.tcheg,"\t\t",tAround,"\t\t",tResposta,"\t\t",tEspera)
    print('\nMédias\n')
    print(f'TurnAround: {turnMedia/len(lista)}')
    print(f'Espera: {esperaMedia/len(lista)}')
  #FIM FCFS/SJF----------------------------------------------------------------------------------------------
  #INICIO RR-------------------------------------------------------------------------------------------------
  elif tipoEscalonamento == "RR":
    q = int(lista[0].quantum)
    tFim = 0
    quandoComecou = 0
    parar = 0
    vetorRR = []#p1;burstquandoentrou;burstquandosaiu
    tamanhoVetor = 0
    
    vetorComEntrada = [] #recebe os valores onde cada processo começou
    nProcessoStr = ''
    nProcessoInt = 0
    bProcesso = 0
    vetorAuxiliar = []
    vetorRRResposta = []
    vetorCopiaBurst = []

    for x in lista: #faz uma copia do burst para imprimir nos resultados, durante o codigo o burst é zerado
      vetorCopiaBurst.append(x.burst)
      
    while True:
      numero = 1
      parar = 0
      for x in lista:
        
        if int(x.burst) > 0:
          valorBurst = int(x.burst)
          valorantes = x.nome
          valorantes1 = x.burst
          tInicio = tFim
          while numero <=q:
            if valorBurst > 0:
              valorBurst-=1            
              numero+=1
              tFim+=1
            else:
              break
          numero = 1
          x.burst = valorBurst
          qtotal += q
         
          vetorRR.append('p'+str(x.nome)+';'+str(tInicio)+';'+str(tFim))
          #Pra pegar os registro de espera, pega o len do vetor, e retorna neste intervalo, o tInicio de cada um => 0,7,14,21 [resposta] 
          
          
        if int(x.burst) != 0:
          parar = 1
      if parar == 0:
        break
    
    #TempoResposta - inicio
    #pega a quantidade de processos
    for x in lista:
      if int(x.nome) > tamanhoVetor:
        tamanhoVetor = int(x.nome)


        
    for x in range(len(vetorRR)):
        palavra = vetorRR[x].split(';')
        nProcessoStr = palavra[0]
        nProcessoInt = int(nProcessoStr[1:])
        bProcesso = palavra[1]

        if nProcessoInt not in vetorAuxiliar:
          vetorAuxiliar.append(nProcessoInt)
        
        
    for x in range(len(vetorRR)):
        palavra = vetorRR[x].split(';')
        nProcessoStr = palavra[0]
        nProcessoInt = int(nProcessoStr[1:])
        bProcesso = palavra[1]  
        vetorRRResposta.append(str(nProcessoInt)+';'+str(bProcesso))
        vetorAuxiliar.remove(nProcessoInt)
        if len(vetorAuxiliar) == 0:
          break

    #TempoResposta - Fim

    #Turnaround - inicio
    vetorRRTurnAround = []  
    turnRR = 0
    for y in range(tamanhoVetor+1):
      for x in range(len(vetorRR)):
          palavra = vetorRR[x].split(';')
          nProcessoStr = palavra[0]
          nProcessoInt = int(nProcessoStr[1:])
          bProcesso = palavra[1]
          tProcesso = palavra[2]
          if y == nProcessoInt:
            turnRR = tProcesso
      vetorRRTurnAround.append(turnRR)

      
    
    #turnaround -fim

    #temporesposta - inicio
    vetorRREspera = []
    palavra = ''
    respostaStr = ''    
    respostaInt = 0
    respostaInt1 = 0
    esperaFinal = 0
    turnRR = 0
    bAntigo = 0
    tAntigo = 0
    posicaoAnterior = 0
    mostrar = True
 
    
    for y in range(tamanhoVetor+1):
      palavra = vetorRRResposta[y].split(';')
      respostaStr = palavra[1:]
      respostaInt = int(formaABostaDoNumero(respostaStr))
      esperaFinal = respostaInt
 
      for x in range(len(vetorRR)):
          palavra = vetorRR[x].split(';')
          nProcessoStr = palavra[0]
          nProcessoInt = int(nProcessoStr[1:])          
          bProcesso = palavra[1]
          tProcesso = palavra[2]

          palavra = vetorRR[posicaoAnterior].split(';')
          nProcessoStr = palavra[0]
          nProcessoInt1 = int(nProcessoStr[1:])
          bAntigo = palavra[1]
          tAntigo = palavra[2]          
          
          if y == nProcessoInt:
              if x > 0 and y == 0:                                  
                esperaFinal += (int(bProcesso) - int(tAntigo))
              elif x > 0 and y > 0:
                if mostrar:
                  esperaFinal += (int(bProcesso) - int(tAntigo))
                mostrar = True
      
              posicaoAnterior = x
      mostrar = False
      
      vetorRREspera.append(esperaFinal)
      esperaFinal = 0
      
    #tempoespera - fim
    espera = 0
    resposta = 0
    turnAround = 0
    turnMedia = 0
    esperaMedia = 0
    for x in range(len(lista)):
      espera = vetorRREspera[x]
      resposta = vetorRRResposta[x]
      resposta = resposta.split(';')[1]
      burst = vetorCopiaBurst[x]
      turnAround = vetorRRTurnAround[x]
      print(int(lista[x].nome)+1,"\t\t",burst,"\t",lista[x].tcheg,"\t\t",turnAround,"\t\t",resposta,"\t\t",espera)
      turnMedia += int(turnAround)
      esperaMedia += espera

    
    print('\nMédias\n')
    print(f'TurnAround: {turnMedia/len(lista)}')
    print(f'Espera: {esperaMedia/len(lista)}')  

    #FIM RR---------------------------------------------------------------------------------------------------------------------------------
    #INICIO SRTF----------------------------------------------------------------------------------------------------------------------------
  elif tipoEscalonamento == "SRTF":
    for x in lista:
      print(x.nome)
    while True:
      numero = 1
      parar = 0
      for x in lista:
        print (x.nome)
        
        ''''if int(x.burst) > 0:
          valorBurst = int(x.burst)
        
          i
            if valorBurst > 0:
              valorBurst-=1            
              numero+=1
              tFim+=1
            else:
              break
          numero = 1
          x.burst = valorBurst
          qtotal += q
          print(f'Antes p{valorantes} -> {valorantes1} \n Depois P{x.nome} -> {x.burst}\n\n')
          print(f'Tempo: {qtotal}')
          #vetorRR.append('p'+str(x.nome)+';'+str(valorantes1)+';'+str(x.burst)+';'+str(qtotal-q)+';'+str(tInicio)+';'+str(tFim))
          vetorRR.append('p'+str(x.nome)+';'+str(tInicio)+';'+str(tFim))
          #Pra pegar os registro de espera, pega o len do vetor, e retorna neste intervalo, o tInicio de cada um => 0,7,14,21 [resposta] '''
          
          
        '''if int(x.burst) != 0:
          parar = 1'''
      if parar == 0:
        break
  
    #FIM SRTF-------------------------------------------------------------------------------------------------------------------------------

    
        
        

def FCFS():
  c = input("Burst manual ou arquivo(M/A)?\n ")
  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    arquivo = "fcfs.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()
    lista = montaListaAutomatica(arquivo)      
  else: #manual
    lista = []
    n = int(input("Qual a quantidade de processos?\n"))
    for i in range(n):
        b = int(input("P" + str(i+1) +" Burst:"))
        t = int(input("P" + str(i+1) +" Tempo de Chegada:")) 
        proc = Processo(i,b,t,0,0)
        lista.append(proc)
        
  lista.sort(key = operator.attrgetter("tcheg"), reverse = False) #FCFS -> ordena por tempo de chegada
  imprimirResultado(lista,"FCFS/SJF")


def SJF(): #@nomeprocesso;burst;tempochegada;prioridade;quantum& 
  c = input("Burst manual ou arquivo(M/A)?\n ")
  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    arquivo = "sjf.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()
    #arquivo = ['@p1;15;0&','@p2;3;0&','@p3;4;0&','@p4;2;1&']
    print(arquivo)
    lista= montaListaAutomatica(arquivo)    
    
    
  else:
    lista = []
    n = int(input("Qual a quantidade de processos?\n"))
    #burst e tempo de chegada manual
    for i in range(n):
        b = int(input("P" + str(i+1) +" Burst:"))
        t = int(input("P" + str(i+1) +" Tempo de Chegada:")) 
        proc = Processo(i,b,t,0,0)
        lista.append(proc)  
  lista.sort(key = operator.attrgetter("burst"), reverse = False)
  lista.sort(key = operator.attrgetter("tcheg"), reverse = False)
  imprimirResultado(lista,"FCFS/SJF")

def seila(numeroProcesso, burstProcesso):
  '''@p1;8;0;0;0&
  @p2;4;1;0;0&
  @p3;9;2;0;0&
  @p4;5;3;0;0&'''
  tempoCronos = 0
  
  while True:
    tempoCronos +=1
    burstProc = 0
    nProcessoMenor = 0 #numero do processo que é menor que o atual
    bProcessoMenor = 0 #burst do processo que e menor que o atual
    temMenor = False
    
    break
      
      
        

def SRTF():
  c = input("Burst manual ou arquivo(M/A)?\n ")
  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    arquivo = "srtf.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()
    lista = montaListaAutomatica(arquivo)      
  else: #manual
    lista = []
    n = int(input("Qual a quantidade de processos?\n"))
    for i in range(n):
        b = int(input("P" + str(i+1) +" Burst:"))
        t = int(input("P" + str(i+1) +" Tempo de Chegada:")) 
        proc = Processo(i,b,t,0,0)
        lista.append(proc)
        
  lista.sort(key = operator.attrgetter("tcheg"), reverse = False) #FCFS -> ordena por tempo de chegada
  for x in lista:
    seila(int(x.nome),int(x.burst))
    break
  imprimirResultado(lista,"SRTF")


    
def RR():
  c = input("Burst manual ou arquivo(M/A)?\n ")
  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    arquivo = "rr.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()
    lista = []
    lista = montaListaAutomatica(arquivo)      
  else: #manual
    lista = []
    q = int(input("Qual o quantum?\n"))
    n = int(input("Qual a quantidade de processos?\n"))
    #burst e tempo de chegada manual
    for i in range(n):
        b = int(input("P" + str(i+1) +" Burst:"))
        t = 0
        proc = Processo(i,b,t,0,q)
        lista.append(proc)
  imprimirResultado(lista,"RR")
    
while True:
  print('--------------------------------------------------------------------------------------\n')
  op = input("Para sair digite 'sair':\n")
  if op.lower() == 'sair':
    break
  else:
    esc = int(input('Digite o tipo de escalonamento a ser executado: \n 1 -> FCFS\n 2 -> SJF \n 3 -> SRTF\n 4 -> Round Robin\n MULTI NÍVEL \n 5 -> RR \n 6 -> Segundo nível FCFS\n'))
    del lista[:] #limpa a lista a cada processo
    if esc == 1: #FCFS
      FCFS()
      print('\t\tFIM')
      print('---------------------------------------------------------')
    elif esc == 2: #SJF
      SJF()
      print('\t\tFIM')
      print('--------------------------------------')     
    elif esc == 3: #SRTF
      SRTF()
      print('\t\tFIM')
      print('--------------------------------------')
    elif esc == 4:
      RR()
    elif esc == 5:
      pass      
    elif esc == 6:
      print('segundo fcfs')
