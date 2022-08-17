import pandas as pd



def missing_values_table(df):
    

        mis_val = df.isnull().sum()
        
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        print ("Seu dataframe tem " + str(df.shape[1]) + " colunas.\n"      
            "Há " + str(mis_val_table_ren_columns.shape[0]) +
              " colunas que possuem valores ausentes.")
        
        return mis_val_table_ren_columns


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