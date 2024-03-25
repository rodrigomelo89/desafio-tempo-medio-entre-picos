
# Solução do Tempo Médio Entre Picos
### Solução proposta por Rodrigo Melo

O desafio consiste em calcular o tempo médio entre os picos de uma determinada forma de onda. Para mais informações sobre o desafio consultar o [Read me](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/README.md). Para solucionar esse problema foi utilizado o Python 3.10.9, mais detalhes sobre as bibliotecas utilizadas podem ser encontradas no [requirements.txt]


## Implementação

Inicialmente, implementei duas funções básicas para melhorar minha visualização dos dados. 

    A primeira é apenas para extrair os dados, valores da forma de onda (ou sinal), que estão armazenados em um arquivo .txt. O nome dessa função é importar_valores e recebe como input uma string com o nome do arquivo txt. Esse arquivo deve está salvo dentro do mesmo diretório/pasta. A função irá retornar uma lista de valores.

    A segunda função é a plotando_exemplo que serve para plotar um gráfico do sinal que está sendo analisado. Essa função recebe como entrada a lista de valores que é retornada pela função importar_valores.

Após a implementação dessas duas funções, analisei o [exemplo](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/exemplo.txt) fornecido. E tentei implementar uma lógica que procuraria os picos e vales, para assim poder determinar quais seriam os máximos locais verdadeiros. Porém, essa estratégia se mostrou muito custosa e ineficiente. Então, mudei de estratégia.

Primeiro, passei a analisar um certo range de valores por vêz para determinar quais seriam os picos de máximos locais. Assim, leio um valor da lista de valores do sinal (valores[i]). Comparo esse valor com os outros 10 valores mais próximos, cinco antes do i e cinco após o i, observando os limites da lista, isto é, do primeiro elemento (valores[0]) até o último elemento, que vai depender do tamanho do sinal. A função responsável por essa parte é chamada de encontra_picos. Tem por input a lista de valores do sinal, e retornar uma lista de valores de onde os máximos locais estão (qual o índice da lista).

Depois que os máximos locais foram encontrados, implementei uma função chamada tempo_medio_entre_picos. Essa nova função recebe como input a lista de máximos locais e imprime na tela o tempo médio entre os picos no formato 00:00. Além disso, a função também retorna o tempo_medio em segundos. A lógica dessa função se resume a somar a diferença de tempo, em segundos, de todos os picos encontrados e depois dividir pela quantidade de picos menos 1.

## Gerando dados para testar a solução

Para testar minha solução, implementei uma função (teste_exemplos) que geraria um sinal aleatório, e salvaria os valores num arquivo txt. Para tal, a função recebe como entrada o tamanho do sinal (a quantidade de entrada de valores). A lógica para implementação consiste em gerar valores aleatórios e multiplicar com a soma de ondas senoides e cosenoides aleatórias. Também é adicionado um ruído branco a geração desses valores. Por fim, os valores encontrados são normalizados para ficar entre 0 e 100, e salvos num arquivo txt.


## Exemplos de entradas para testar a implementação

O teste pode ser realizado através do carregamento de um arquivo txt, usando a função importar_valores('seu_arquivo_de_valores.txt') ou gerando um sinal aleatório através da função teste_exemplos(quantidade_de_amostras_do_sinal). Nesse último caso, os valores ficarão salvos em [valores_onda.txt](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/valores_onda.txt).

## Maiores dificuldades e dúvidas

Uma das grandes dificuldades foi a presença de apenas um exemplo (o erro presente na descrição da solução no read me também atrapalhou um pouco). Já do ponto de vista da implementação, tive um pouco de dificuldade para criar a lógica para a localização dos máximos locais de forma eficiente.

Porém, a maior dificuldades foi para criar a função que gerasse sinais aleatórios da forma que eu queria. Ou seja, com um comportamento imprevisível.

## Como executar a solução

Como mencionado, a função foi elaborada no Python 3.10.9. Então seria necessario instalar essa versão. Além disso, seria necessario instalar todas as bilbiotecas necessarias, para tal basta usar o comando "pip install -r requirements.txt" no terminal.

Com as intalações completas basta executar o código main_entre_picos. Através do terminal, é necessário entrar no diretório onde se clonou o repositório, e rodar o comando "python main_entre_picos.py". O código está para rodar testando com sinais aleatórios gerados pela função teste_exemplos. Caso queira testar com algum sinal específico, basta adicionar o arquivo txt com os valores dentro do repositório, abrir o arquivo main_entre_picos.py e trocar as linhas abaixo:

    teste_exemplos(200)
    valores = importar_valores('valores_onda.txt')

Pela linha:

    valores = importar_valores('nome_do_seu_arquivo.txt')

Por fim, rodar o código com seu arquivo de teste.