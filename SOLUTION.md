# Solução do Tempo Médio Entre Picos
### Proposta por Rodrigo Melo

O desafio consiste em calcular o tempo médio entre os picos de uma determinada forma de onda. Para mais informações sobre o desafio, consulte o [Read me](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/README.md). A solução para este problema foi desenvolvida utilizando Python 3.10.9. Mais detalhes sobre as bibliotecas utilizadas podem ser encontrados no arquivo [requirements.txt](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/requirements.txt).

## Implementação

Inicialmente, foram implementadas duas funções básicas para melhorar a visualização dos dados.

A primeira função, chamada `importar_valores`, extrai os valores da forma de onda (ou sinal) armazenados em um arquivo .txt. Ela recebe como input uma string com o nome do arquivo txt, o qual deve estar salvo no mesmo diretório/pasta. A função retorna uma lista de valores.

A segunda função, `plotando_exemplo`, é utilizada para plotar um gráfico do sinal que está sendo analisado. Ela recebe como entrada a lista de valores retornada pela função `importar_valores`.

Após a implementação dessas duas funções, foi analisado o [exemplo](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/exemplo.txt) fornecido. Tentei inicialmente implementar uma lógica para identificar os picos e vales, a fim de determinar os máximos locais verdadeiros. No entanto, essa estratégia se mostrou custosa e ineficiente, então optei por mudar de abordagem.

Primeiramente, comecei a analisar um certo intervalo de valores por vez para determinar os picos de máximos locais. Para isso, comparei um valor da lista de valores do sinal (valores[i]) com os outros 10 valores mais próximos, cinco antes de i e cinco após i, observando os limites da lista (do primeiro elemento até o último, dependendo do tamanho do sinal). A função responsável por essa parte é chamada `encontra_picos`. Ela recebe como entrada a lista de valores do sinal e retorna uma lista de índices onde os máximos locais estão localizados.

Após encontrar os máximos locais, implementei a função `tempo_medio_entre_picos`. Esta nova função recebe como input a lista de máximos locais e imprime na tela o tempo médio entre os picos no formato 00:00. Além disso, a função também retorna o tempo médio em segundos. A lógica dessa função consiste em somar as diferenças de tempo, em segundos, entre todos os picos encontrados e depois dividir pela quantidade de picos menos 1.

## Gerando dados para testar a solução

Para testar a solução, foi implementada uma função chamada `teste_exemplos` que gera um sinal aleatório e salva os valores em um arquivo txt. Esta função recebe como entrada o tamanho do sinal (a quantidade de amostras do sinal). A lógica para implementação consiste em gerar valores aleatórios e multiplicá-los pela soma de ondas senoides e cosenoides aleatórias. Um ruído branco também é adicionado à geração desses valores. Por fim, os valores encontrados são normalizados para ficarem entre 0 e 100 e salvos em um arquivo txt.

## Exemplos de entradas para testar a implementação

O teste pode ser realizado carregando um arquivo txt utilizando a função `importar_valores('seu_arquivo_de_valores.txt')` ou gerando um sinal aleatório através da função `teste_exemplos(quantidade_de_amostras_do_sinal)`. Neste último caso, os valores ficarão salvos em [valores_onda.txt](https://github.com/rodrigomelo89/desafio-tempo-medio-entre-picos/blob/main/valores_onda.txt).

## Maiores dificuldades e dúvidas

Uma das maiores dificuldades encontradas foi a presença de apenas um exemplo (o erro presente na descrição da solução no readme também atrapalhou um pouco). Do ponto de vista da implementação, houve um pouco de dificuldade em criar a lógica para localizar os máximos locais de forma eficiente.

No entanto, a maior dificuldade foi criar a função que gerasse sinais aleatórios da forma que eu desejava, ou seja, com um comportamento imprevisível.

## Como executar a solução

Como mencionado, a função foi elaborada em Python 3.10.9. Portanto, é necessário instalar esta versão. Além disso, é necessário instalar todas as bibliotecas necessárias, o que pode ser feito com o comando "pip install -r requirements.txt" no terminal.

Com as instalações completas, basta executar o código `main_entre_picos`. No terminal, navegue até o diretório onde o repositório foi clonado e execute o comando "python main_entre_picos.py". O código está configurado para executar testes com sinais aleatórios gerados pela função `teste_exemplos`. Se desejar testar com algum sinal específico, basta adicionar o arquivo txt com os valores no repositório, abrir o arquivo `main_entre_picos.py` e modificar as linhas abaixo:

```
teste_exemplos(200)
valores = importar_valores('valores_onda.txt')
```

para:

```
valores = importar_valores('nome_do_seu_arquivo.txt')
```

Por fim, execute o código com o seu arquivo de teste.