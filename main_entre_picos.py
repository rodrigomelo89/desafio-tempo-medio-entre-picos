import matplotlib.pyplot as plt
import numpy as np
import random


def importar_valores(filename):
    # importa os valores salvos em um arquivo para a variavel valores
    with open(filename, 'r') as file:
        valores = [float(line.strip()) for line in file]

    return valores 


def plotando_exemplo(valores):    
    # gera o eixo x com a quantidade de segundos necessários
    segundos = list(range(1, len(valores) + 1))
    
    # plota o sinal
    plt.plot(segundos, valores)
    plt.xlabel('tempo')
    plt.ylabel('valores')
    plt.grid(True)
    plt.show()


def encontra_picos(valores):
    # variavel para salvar os maximos locais
    picos_maximos_locais = []

    for index in range(0, len(valores)):
        # variavel que vai determinar o range que é analisado pra verificar se é um máximo local ou não
        idx_range = -5
        # variavel para contar quantos valores menores dentro do range existe
        quantidade_valores_menores = 0
        # variavel para contar quantos valores existem dentro do range
        quantidade_valores_possiveis = 0

        # o range vai de -5 a 5
        while idx_range < 6:
            # verifica se a soma do index mais o valor do range está dentro dos limites do vetor de valores
            if 0 <= index + idx_range <= len(valores) - 1 and idx_range != 0:
                quantidade_valores_possiveis += 1
                # verifica se o valor atual é maior do que os vizinhos
                if valores[index] >= valores[index + idx_range]:
                    # verifica se o valor atual é superior a 50 (valor minimo para ser considerado máximo)
                    if valores[index] >= 50:
                        quantidade_valores_menores += 1
                else:
                    idx_range = 6
        
            idx_range += 1

        # verifica se a quatidade de valores menores é a mesma da quantidade de valores dentro do range
        # o que confirma que o valor atual é o maior dentro do range  
        if quantidade_valores_menores == quantidade_valores_possiveis:
            picos_maximos_locais.append(index + 1)

    return picos_maximos_locais


def tempo_medio_entre_picos(picos):
    # variavel para somar a diferença de tempo entre os picos
    tempo_total_picos = 0
    for index in range(len(picos)):
        if index > 0:
            tempo_total_picos += picos[index] - picos[index - 1]

    # verifica se tem mais de 1 pico
    if len(picos) > 1:
        # calcula o tempo médio dividindo pela quantidade de picos menos 1
        tempo_medio = int(np.round(tempo_total_picos / (len(picos) - 1)))
    else:
        tempo_medio = 0

    # calcula o tempo em minutos e segundos
    minutos = tempo_medio // 60

    dezenas_minutos = minutos // 10
    unidades_minutos = minutos % 10

    segundos = tempo_medio % 60

    dezenas_segundos = segundos // 10
    unidades_segundos = segundos % 10

    # imprime o valor no formato 00:00
    print(f'{dezenas_minutos}{unidades_minutos}:{dezenas_segundos}{unidades_segundos}')

    return tempo_medio


def teste_exemplos(tamanho):
    # cria um vetor para armazenar os valores do sinal
    valores_onda = []
    # cria um valor aleatório para guardar como valor inicial
    valor_anterior = random.randint(0, 100)  
    # cria uma variavel para armezar o valor a ser adicionado ao vetor de valores
    # igual ao valor_anterior menos 1 para garantir o funcionamento do loop while
    valor_aleatorio = valor_anterior - 1
    for i in range(tamanho):
        # loop para verificar se não tá gerando 2 valores iguais
        while (valor_aleatorio == valor_anterior):
            # ruido branco
            ruido = random.randint(-10, 10)  

            # mediana da onda
            media = random.randint(-50,50)

            # forma da onda
            variacao = random.randint(-50,50) * (random.random() * np.sin(2 * np.pi * random.uniform(0,10) * random.randint(0,10)) 
                                                + random.random() * np.cos(2 * np.pi * random.uniform(0,10) * random.randint(0,10))
                                                + random.random() * np.cos(np.pi * random.uniform(0,10) * random.randint(0,10))
                                                + random.random() * np.sin(np.pi * random.uniform(0,10) * random.randint(0,10)))
            
            # gera um valor para ser adicionado ao vetor de valores da onda
            valor_aleatorio = int(np.round(media + variacao))
            valor_aleatorio += valor_anterior + ruido
        
        valores_onda.append(valor_aleatorio)
        valor_anterior = valor_aleatorio

    # normaliza os valores entre 0 e 100
    valores_onda = 100 - 100 * ((np.max(valores_onda) - np.array(valores_onda)) / (np.max(valores_onda) - np.min(valores_onda)))

    # transforma os valores em inteiros
    valores_onda = np.round(valores_onda).astype(int)

    # Salvar os valores gerados em um novo arquivo de texto
    with open('valores_onda.txt', 'w') as file:
        for valor in valores_onda:
            file.write(str(valor) + '\n')


if __name__ == '__main__':   
    teste_exemplos(200)
    valores = importar_valores('valores_onda.txt')
    picos = encontra_picos(valores)
    print(picos)
    tempo = tempo_medio_entre_picos(picos)
    print(tempo)
    plotando_exemplo(valores)