from email.charset import BASE64
import pandas as pd






def best_corr(df, col: str, n: int, m: int) -> list:

    '''retorna uma lista com as 'm' colunas com maior correlação e as 'n' com menor correlação'''
    
    base = df.corr()[col].sort_values(ascending=False)
    
    # base.drop(labels=col, inplace=True)
    
    base.dropna(inplace=True)
        
    lista_tail = base.tail(n).keys().to_list()
    lista_head = base.head(m).keys().to_list()
    
    lista = lista_head + lista_tail
    
    
    return lista

def columns_null(df, n: int) -> list:

    '''retorna uma lista com as 'n' colunas com maior numero de valores nulos'''
    
    lista = df.isnull().sum().sort_values(ascending=False).keys().to_list()[:n]
    
    return lista


def drop_outlier(df, col_name: str) -> pd.DataFrame():
    
    '''retorna um dataframe sem os outliers'''
    
    base = df[col_name]
    
    q1 = base.quantile(0.25)
    q3 = base.quantile(0.75)
    
    qr = q3-q1 
    
    low  = q1-1.5*qr
    high = q3+1.5*qr
    
    df_out = df.loc[(base > low) & (base < high)]
    
    return df_out