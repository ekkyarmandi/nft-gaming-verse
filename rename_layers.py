import sqlite3
import os

from numpy import source

def create_table(table_name):
    con = sqlite3.connect('source\\layers_configuration.db')
    cur = con.cursor()
    cmd = f'''CREATE TABLE {table_name} (
        layers_name TEXT,
        current_index INTEGER,
        new_index INTEGER DEFAULT 0
    )
    '''
    cur.execute(cmd)
    con.close()

def collect_layers(source_path,database='source\\layers_configuration.db'):
    con = sqlite3.connect(database)
    cur = con.cursor()

    for file in os.listdir(source_path):
        if file.endswith('png'):
            splits = file.split('_')
            index = splits[0]
            file_name = "_".join(splits[1:])

            cur.execute('INSERT or IGNORE INTO layers(layers_name,current_index) VALUES(?,?)',(file_name,index)) 

    con.commit()
    con.close()

def rename_layers(source_path='layers'):
    con = sqlite3.connect('source\\layers_configuration.db')
    cur = con.cursor()
    cur.execute('SELECT current_index,new_index,layers_name FROM layers') 
    layers = cur.fetchall()
    for layer in layers:
        file_name = "_".join([str(layer[0]),layer[2]])
        new_file_name = "_".join([str(layer[1]),layer[2]])
        os.rename(
            src=os.path.join(source_path,file_name),
            dst=os.path.join(source_path,new_file_name)
        )
        cur.execute('UPDATE layers SET current_index=? WHERE layers_name=?',(layer[1],layer[2]))
    con.commit()
    con.close()

if __name__ == "__main__":

    # create_table('layers')

    collect_layers('layers')

    # rename_layers()