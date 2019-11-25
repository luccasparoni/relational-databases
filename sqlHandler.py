import cx_Oracle

# Creating connection with local dabatase, with DRCP connection type.
con = cx_Oracle.connect('P10277040', '774411996633', '127.0.0.1:/orcl:pooled', 
             cclass = "HOL", purity = cx_Oracle.ATTR_PURITY_SELF)


# Functions to create and search data.

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

def search_game(table_name, values, columns):
    cur = con.cursor()
    str_select = ' AND '.join([(columns[i] + " = \"" + values[i] + "\"") for i in range(len(columns))])
    sql_str = 'select * from JOGO as J join GENERO_JOGO as GJ on J.NUMERO_MESA = GJ.JOGO' +
        'join PLATAFORMA_JOGO as PJ on J.NUMERO_MESA = PJ.JOGO where ' + str_select

    cur.execute(sql_str)
    res = cur
    cur.close()
    return res

# Closing conection with database
def close_connection():
    cur.close()
    con.close()