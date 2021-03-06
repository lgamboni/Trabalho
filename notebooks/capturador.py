import urllib, json
import time,datetime
import pandas as pd
import ccxt
import numpy as np
import mysql.connector
 

class capturador(object):
    

    def __init__(self,max_dias,symbol,time_frame):
        self.time_frame = time_frame
        base = datetime.datetime.today()
        data_inicial = (base - datetime.timedelta(days=max_dias)).date()
        time1 = time.mktime(data_inicial.timetuple())
        self.time1 = time1
        self.symbol = symbol
        
        
  
    def get_gatecoin_captura(self):
            gatecoin = ccxt.gatecoin()
            ohclv = gatecoin.fetch_ohlcv(symbol=self.symbol,timeframe=self.time_frame,since=self.time1)
            ohclv = np.array(ohclv)
            mercado = self.symbol
            l_timestamp = list(ohclv[:,0]/1000)
            l_date = []
            l_open = list(ohclv[:,1])
            l_high  = list(ohclv[:,2])
            l_close  = list(ohclv[:,3])
            l_low  = list(ohclv[:,4])
            l_volume  = list(ohclv[:,5])
             
            for i in range(len(ohclv)):
                timestamp = l_timestamp[i]
                t = datetime.datetime.fromtimestamp(timestamp)
                #lista_date.append(str(t.year)+'-'+str(t.month)+'-'+str(t.day))
                l_date.append(t)
                #l_timestamp.append(ohclv[i][0]/1000)
                #l_close.append(ohclv[i][2])
            
            struct_df = {
                        "datetime": l_date,
                         "timestamp":l_timestamp,
                         "close":l_close,
                         "high":l_high,
                         "low":l_low,
                         "open":l_open,
                         "volume":l_volume,
                         }
            gatecoin = pd.DataFrame(struct_df)
            return(gatecoin)
                  
  
def connecta():
        conn = mysql.connector.connect(user='henriqu2_lorena', password='verao2018',
            host='77.104.156.92',database='henriqu2_storageCoin')
        return(conn)          


def save(data1,symbol):
    conn = connecta()
    cursor = conn.cursor()
    for i in range(len(data1.datetime)):    
        if data1.low[i] is None:
            cursor.execute('insert into gatecoin(date,timestamp,open,high,close,volume,mercado) values("'+str(data1.datetime[i]) +'",'+str(data1.timestamp[i]) + ','+str(data1.open[i]) + ',' +str(data1.high[i]) + ',' + str(data1.close[i]) +  ',' +str(data1.volume[i]) + ',"' + str(symbol) + '")')
        else:
            cursor.execute('insert into gatecoin(date,timestamp,open,high,close,low,volume,mercado) values("'+str(data1.datetime[i]) +'",'+str(data1.timestamp[i]) + ','+str(data1.open[i]) + ',' +str(data1.high[i]) + ',' + str(data1.close[i]) + ',' + str(data1.low[i]) + ',' +str(data1.volume[i]) + ',"' + str(symbol) + '")')
        conn.commit()
    conn.close()



def get(symbol,datainicio = None ,datafim = None):
    if not symbol:
        return(print("Insira a moeda, para poder capturar os valores \n do banco!"))
    conn = connecta()
    if datainicio is None and datafim is None:    
        df =  pd.read_sql('Select * from gatecoin where mercado =' + '"' + str(symbol) + '"',conn)
    elif datainicio is None:
        df =  pd.read_sql('Select * from gatecoin where mercado =' + '"' + str(symbol) + '"' + 'and date <= ' + '"' + str(datafim) + '"',conn)
    elif datafim is None:
        df =  pd.read_sql('Select * from gatecoin where mercado =' + '"' + str(symbol) + '"' + 'and date >= ' + '"' + str(datainicio) + '"' ,conn)
    else:   
        df =  pd.read_sql('Select * from gatecoin where mercado =' + '"' + str(symbol) + '"' +  'and date BETWEEN ' + '"' + str(datainicio) + '"' + ' and ' + '"' + str(datafim) + '"',conn)
    conn.close()
    return df
            

