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
  def __init__(self, nome,burst,tcheg, taround,tresposta):
      self.nome = nome
      self.burst = burst
      self.tcheg = tcheg
      self.taround = taround
      self.tresposta = tresposta
  
  def setNome(nome):
    self.nome = nome

  def setBurst(burst):
    self.burst = burst
  
  def setTcheg(tcheg):
    self.tcheg = tcheg

  def setTcheg(taround):
    self.taround = taround
  def setTresposta(tresposta):
    self.tresposta = tresposta

def FCFS(): 
  c = input("Burst manual ou arquivo(M/A)?\n ")  

  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    '''arquivo = "fcfs.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()'''
    arquivo = ['@p1;15;0&','@p2;3;0&','@p3;4;0&','@p4;8;2&']
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
  
def SJF(): #@nomeprocesso;burst;tempochegada;prioridade;quantum& 
  c = input("Burst manual ou arquivo(M/A)?\n ")  

  if c == "A" or c == "a":
    #burst e tempo de chegada automático
    '''arquivo = "fcfs.txt"
    arquivo = open(arquivo)
    arquivo = arquivo.read()
    arquivo = arquivo.split()'''
    arquivo = ['@p1;15;0&','@p2;3;0&','@p3;4;0&','@p4;8;2&']
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

    lista.sort(key = operator.attrgetter("burst"), reverse = False)
    lista.sort(key = operator.attrgetter("tcheg"), reverse = False)
      
      
      
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
      print('RR')
    elif esc == 6:
      print('segundo fcfs')