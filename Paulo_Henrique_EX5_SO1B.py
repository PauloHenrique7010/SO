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
      
def imprimirResultado(lista,tipoEscalonamento):
  tAround = 0
  tEspera = 0
  tResposta = 0
  turnMedia = 0
  esperaMedia = 0
  qtotal = 0
  print ("Processo\tT.Burst\tT.Chegada\tTurnAround\tT.Resposta\tT.Espera")
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
  #FIM FCFS----------------------------------------------------------------------------------------------
  #INICIO SJF--------------------------------------------------------------------------------------------
  elif tipoEscalonamento == "SJF":
    for x in lista:
      if int(x.nome) == 0: #caso seja o primeiro processo, tempo de espera, e o tempo de chegada
        tEspera = x.tcheg
      else:
        if int(x.tcheg) < int(x.burst):
          tEspera = int(x.burst) - int(x.tcheg)        
        else:
          tEspera = int(x.tcheg) - int(x.burst)
      tAround += (int(x.burst)-int(x.tcheg))
      tResposta = tEspera #no fcfs, tempo de resposta é o mesmo de espera
      turnMedia += tAround      
      esperaMedia += int(tEspera)  
      print(int(x.nome)+1,"\t\t",x.burst,"\t",x.tcheg,"\t\t",tAround,"\t\t",tResposta,"\t\t",tEspera)
    print('\nMédias\n')
    print(f'TurnAround: {turnMedia/len(lista)}')
    print(f'Espera: {esperaMedia/len(lista)}')



    if t < b:
        return b - t
    else:
        return t - b
  #FIM SJF----------------------------------------------------------------------------------------------
  elif tipoEscalonamento == "RR":
    q = int(lista[0].quantum)
    tFim = 0
    quandoComecou = 0
    parar = 0
    vetorRR = []#p1;burstquandoentrou;burstquandosaiu
    
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
          print(f'Antes p{valorantes} -> {valorantes1} \n Depois P{x.nome} -> {x.burst}\n\n')
          print(f'Tempo: {qtotal}')
          vetorRR.append('p'+str(x.nome)+';'+str(valorantes1)+';'+str(x.burst)+';'+str(qtotal-q)+';'+str(tInicio)+';'+str(tFim))
          
        if int(x.burst) != 0:
          parar = 1
      if parar == 0:
        break
      
    print(vetorRR)         
        
        

def FCFS(): 
  c = input("Burst manual ou arquivo(M/A)?\n ")
  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    arquivo = "fcfs.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()
    lista = []
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
    lista = []
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

def SRTF():
  c = input("Burst manual ou arquivo(M/A)?\n ")
  tempoPassado = 0
  nomeAtual = 0
  burstAtual = 0
  tchegAtual = 0
 
  def vetorTempo(processoQueEstaAgora,tempopassado):
    for x in range(len(lista)):
      if x == processoQueEstaAgora:
        nomeAtual = lista[x].nome
        burstAtual = lista[x].burst
        tchegAtual = lista[x].tcheg
      
      if x != processoQueEstaAgora:
        if (burstAtual-tchegAtual) < (lista[x].burst-lista[x].tcheg):
          lista[nomeAtual].burst-=1
          tempoPassado+=1
        else:
          vetorTempo(lista[x],int(tempoPassado))
          
      
      
  

  
  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    '''arquivo = "fcfs.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()'''
    arquivo = ['@p1;15;0&','@p2;2;2&','@p3;3;5&','@p2;2;7&']
    print(arquivo)
    lista = []

    for x in range(len(arquivo)):
      prepara = arquivo[x]
      prepara = prepara.split('@')
      separa = prepara[1]
      separa = separa.split('&')
      gol = separa[0]
      gol = gol.split(';')
      processo = gol[0]
      processo = int(processo[1:])
      burst = int(gol[1])
      tchegada = int(gol[2])

      if x == 0:
        tresposta = tchegada
        taround = burst
        tresposta = tchegada
      else:
        tresposta = taround - tchegada
        taround += burst-tchegada
        
      proc = Processo(x,burst,tchegada,taround,tresposta)
      lista.append(proc)
    lista.sort(key = operator.attrgetter("tcheg"), reverse = False)
    vetorTempo(0,0)
    
    
      
      
      
  else:
    lista = []
    n = int(input("Qual a quantidade de processos?\n"))
    #burst e tempo de chegada manual
    for i in range(n):
        b = int(input("P" + str(i+1) +" Burst:"))
        t = int(input("P" + str(i+1) +" Tempo de Chegada:")) 
        if i == 0:
          tresposta = t
          taround = b
          tresposta = t
        else:
          tresposta = taround - t
          taround += b-t
          

        proc = Processo(i,b,t,taround,tresposta)
        lista.append(proc)  
  
    lista.sort(key = operator.attrgetter("burst"), reverse = False)
    lista.sort(key = operator.attrgetter("tcheg"), reverse = False)    


  print ("Todos os processos...")
  print ("Processo","Tempo de Burst","Tempo de chegada","TurnAround","Tempo de resposta","Tempo de Espera")
  contador = 0
  for i in lista:
    if contador == 0:
      print("\t",i.nome,"\t\t\t",i.burst,"\t\t",i.tcheg,"\t\t\t",i.taround,"\t\t\t",i.tresposta,"\t\t\t\t",i.tresposta)
    else:
      print("\t",i.nome,"\t\t\t",i.burst,"\t\t\t",i.tcheg,"\t\t\t",i.taround,"\t\t\t",i.tresposta,"\t\t\t",i.tresposta)
    contador +=1
    
while True:
  print('--------------------------------------------------------------------------------------\n')
  op = input("Para sair digite 'sair':\n")
  if op.lower() == 'sair':
    break
  else:
    esc = int(input('Digite o tipo de escalonamento a ser executado: \n 1 -> FCFS\n 2 -> SJF \n 3 -> SRTF\n 4 -> Round Robin\n MULTI NÍVEL \n 5 -> RR \n 6 -> Segundo nível FCFS\n'))
    if esc == 1: #FCFS
      FCFS()
      print('\t\tFIM')
      print('---------------------------------------------------------')
    elif esc == 2: #SJF
      SJF()
      print('\t\tFIM')
      print('--------------------------------------')

     
    elif esc == 3:
      SRTF()
      print('\t\tFIM')
      print('--------------------------------------')
    elif esc == 4:
      pass
    elif esc == 5:
      lista = []
      RR()
    elif esc == 6:
      print('segundo fcfs')
