import os
from datetime import date, timedelta
import datetime

def Validacao_input (msg):

    while True:
         
        teste = input(msg)

        if teste.isdigit() and len(teste) == 8:
            return teste

        else:
            print('Entrada de dados invalida tem que ser neste formato (dd/mm/aaaa) com 8 digitos e apenas numeros sem sibolo algum nem espaços')
           
            
            resposta =  input('Deseja tentar novamente ? [S/N]').strip().lower()

            if resposta == 's' or resposta == 'sim':
                niver == 0
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
               
            else:
                 
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()

def calc_idade (niver):

        dataAtual = datetime.date.today().strftime('%d%m%Y')
        # para pegar quantos dias teve no mes anterior
        primeiro_dia_mes_atual = date.today().replace(day=1)

        ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)

        dias_do_mes_anterior = ultimo_dia_mes_anterior.day

        #Agora pegando o do mes anterior do anterior

        ultimo_dia_mes_anterior_2 = ultimo_dia_mes_anterior.replace(day=1) - timedelta(days=1)

        dias_do_mes_anterior_2 = ultimo_dia_mes_anterior_2.day

        # Separação do dia Atual para calculo
        Atual_Dia = dataAtual[:2]
        Atual_Mes = dataAtual[2:4]
        Atual_Ano = dataAtual[4:8]

        # Separação do aniversario do usuario
        Aniversario_Dia = niver[:2]
        Aniversario_Mes = niver[2:4]
        Aniversario_Ano = niver[4:8]

        #fazendo a subtração dos dias/meses/anos
        idadeAno = int(Atual_Ano) - int(Aniversario_Ano)
        idadeMes = int(Atual_Mes) - int(Aniversario_Mes)
        idadeDia = int(Atual_Dia) - int(Aniversario_Dia)

        # Validaçoes de meses e dias pra não haver meses e dias negativos 

        if idadeMes < 0:
            idadeMes +=12
            idadeAno -=1

        if idadeDia < 0:    
            idadeDia += dias_do_mes_anterior 
            if idadeDia < 0:
                idadeDia += dias_do_mes_anterior_2 

        # Resultado
        print ('Sua idade é ',idadeAno,'anos ',idadeMes,'meses ',idadeDia,'dias' ) 


niver = Validacao_input('Informe sua data de aniversário sem nenhum simbolo apenas numeros nesta order (dia/Mês/Ano): ')
calc_idade (niver)


