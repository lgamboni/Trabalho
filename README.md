# CryptoMarketAnalysis  ![](https://crunchbase-production-res.cloudinary.com/image/upload/c_lpad,h_256,w_256,f_jpg/v1492172910/ht0sgoxvzc2fw7qkkyft.png)
## Trabalho do curso de Verão 2018 

  - Autor: Lorena Gamboni
  - Professor: Renato Rocha e Flavio Coelho
  - Exchange escolhida: Bitlish
  - Local da exchange: Inglaterra
  - Mercados: ![](https://o56yv98bm.qnssl.com/coin_BCH.png?imageView2/2/w/19) Bitcoin Cash (BCH/BTC), ![](https://o56yv98bm.qnssl.com/coin_LTC.png?imageView2/2/w/19) Litecoin Diamond (LTC/BTC) e ![](https://o56yv98bm.qnssl.com/coin_ETH.png?imageView2/2/w/19) Ether (ETH/BTC)


### Estrutura do trabalho
 

#### 1 -  Obtendo os dados 
       
Escolhida a exchange **`bitlish`**, os dados são obtidos através da biblioteca **`ccxt`**

  - **`src/capturador.py`**: possui uma classe chamada **`capturador`** que exectua a extração baseada nos seguintes argumentos: 
    - **`max_dias`**: Quanditade de dias até a data atual
    - **`symbol`**: Tipo de moeda que se deseja obter os valores
    - **`time_frame`**: intervalo de tempo dos dados (ex.: 5 minutos)


#### 2 -  Banco de dados (MySQL) 

Com o banco de dados online, uma tabela foi criada para os dados da exchange escolhida. Com uma chave primária composta (date e mercado). É possível armazenar em um unico lugar, dados de diferentes moedas e time frames sem duplicatas. 

Estando o banco online, não há necessidade de recriar o storage toda vez que o script for rodado em um ambiente novo. 

  - **`src/capturador.py`**: possui uma função chamada **`save`** que armazena os dados extraídos do capturador e outra chamada **`get`**. Argumentos:
  
    - **`data1`**: objeto com os dados da moeda
    - **`symbol`**: Tipo de moeda que se deseja obter os valores


#### 3 - Visualização dos dados apartir do banco. 
    
A visualização está no jupyter notebook
  

##### Dependências para rodar os códigos

  - bokeh
  - numpy
  - ccxt
  - pandas
  - requests
  - mysql.connector

