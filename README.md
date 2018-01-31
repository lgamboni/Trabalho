## Trabalho do curso de Verão 2018 

  - Autor: Lorena Gamboni
  - Professor: Renato Rocha e Flavio Coelho
  - Exchange escolhida: Bitlish
  - Local da exchange: Inglaterra
  - Mercados: ![](https://o56yv98bm.qnssl.com/coin_BCH.png?imageView2/2/w/19) Bitcoin Cash (BCH/BTC), ![](https://o56yv98bm.qnssl.com/coin_LTC.png?imageView2/2/w/19) Litecoin Diamond (LTC/BTC) e ![](https://o56yv98bm.qnssl.com/coin_ETH.png?imageView2/2/w/19) Ether (ETH/BTC)


### Nesse repositório, você encontrará

####   Script para extração dos dados utilizando a biblioteca **`ccxt`**

  - **`/capturador.py`**: possui uma classe chamada **`capturador`** que exectua a extração baseada nos seguintes argumentos: 
    - **`max_dias`**: Quanditade de dias até a data atual
    - **`symbol`**: Tipo de moeda que se deseja obter os valores
    - **`time_frame`**: intervalo de tempo dos dados (ex.: 5 minutos)


####  Script para Banco de dados (MySQL) 
  
  O banco de dados possui uma tabela para a bitlish, e recebe dados de diferentes times frame e moedas. Com uma função para salvar e para obter os dados do banco.
  
 
#### Visualização dos dados apartir do banco. 
    
##### Você precisará, entre outros, de:

  - bokeh
  - numpy
  - ccxt
  - pandas
  - requests
  - mysql.connector

