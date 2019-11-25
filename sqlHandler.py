import cx_Oracle

# Creating connection with local dabatase, with DRCP connection type.
con = cx_Oracle.connect('P10277040', '774411996633', '127.0.0.1:/orcl:pooled', 
             cclass = "HOL", purity = cx_Oracle.ATTR_PURITY_SELF)


# Functions to create and update data.

# Receive table_name [string], values [array] (default: all values are sent),
#  if dont send a value, need to send fields[array]: all fields that were sent
#  return true if success
def insert_new_data(table_name, values, fields= None):
    cur = con.cursor()
    str_values = ', '.join(values)
    str_fields = (" ("+ ', '.join(fields) + ")") if fields else "" 
    sql_str = 'insert into ' + table_name + str_fields + ' values (' + str_values + ')'

    cur.execute(sql_str)
    con.commit()
    return true


# Receveive table_name [string], columns[array of strings] and values[array of strings], 
#  key_name[string] and key_value[string], returns true if succes
def update_data(table_name, columns, values, key_name, key_value):
    cur = con.cursor()
    str_set = ', '.join([(columns[i] + " = \"" + values[i] + "\"") for i in range(len(columns))])
    str_condition = key_name + " = \"" + key_value + "\""
    sql_str = 'alter table ' + table_name + ' set ' + str_set + ' where ' + str_condition
    cur.execute(sql_str)
    con.commit()
    return true


# update_data('name_tabela', ['coluna1', 'coluna2'], ['valor1', 'valor2'], 'chave', 'valor')


def search_game(table_name, values, columns):
    cur = con.cursor()
    str_select = ' AND '.join([(columns[i] + " = \"" + values[i] + "\"") for i in range(len(columns))])
    sql_str = 'select * from JOGO as J join GENERO_JOGO as GJ on J.NUMERO_MESA = GJ.JOGO' +
        'join PLATAFORMA_JOGO as PJ on J.NUMERO_MESA = PJ.JOGO where ' + str_select

    cur.execute(sql_str)
    return cur

# Optional param: event_name[string]
# return [int]: number of participants in given event, or [array], with name and counter of participants in each event 
# present in the database  
def participant_event(event_name = None):
    cur = con.cursor()

    if event_name:
        sql_str =  "select A.NOME count(*) from participante as P join PARTIPAEVENTO" + 
            "as E on P.CODIGO_INGRESSO = E.PARTICIPANTE join ATRACAO as A on E.ATRACAO = A.NUMERO" + 
            "where A.NOME = " + event_name
    else:
        sql_str = "select count(*) from participante as P join PARTIPAEVENTO " +
            "as E on P.CODIGO_INGRESSO = E.PARTICIPANTE join ATRACAO as A on E.ATRACAO = A.NUMERO group by A.NOME"

    cur.execute(sql_str)
    
    return cur.fetchone()


# Closing conection with database
def close_connection():
    cur.close()
    con.close()