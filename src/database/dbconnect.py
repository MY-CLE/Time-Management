import psycopg2
from pathlib import Path
from configparser import ConfigParser

# General Path fix for windows/linux
def config(filename=Path('src/database/database.ini'), section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def connect(sql):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        ##params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host='localhost', 
            dbname='postgres', 
            user='postgres', 
            password='postgresadmin', 
            port='5432')
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute(sql)
        
        conn.commit()
        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()