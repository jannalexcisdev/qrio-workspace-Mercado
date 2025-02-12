#CRUD OPERATIONS

#CREATE
#READ
#UPDATE
#DELETE
import psycopg2

def create_person(conn, firstname, lastname, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)" , (firstname, lastname, age))
    conn.commit()
    cursor.close()

def read_all_persons(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")
    persons = cursor.fetchall()
    cursor.close()
    return persons

def read_person(conn, person_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person WHERE age = %s",  (person_id,)) 
    persons = cursor.fetchone()
    cursor.close()
    return persons

def update_person(conn, person_id, person_firstname):
    cursor = conn.cursor()
    cursor.execute("UPDATE person SET firstname =%s WHERE id =%s", (person_firstname, person_id))
    conn.commit()
    cursor.close()


def delete_person(conn, person_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM person WHERE id = %s", (person_id,))
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    conn = psycopg2.connect (
        host="localhost",
        database="postgres",
        user="jann",
        password="@dmin098"
    )
#C
    #create_person(conn, "John", "Doe", 30)
#R all
    #persons = read_all_persons(conn)
    #print(persons)
#R one
    #persons = read_person(conn, person_id=30)
    #print(persons)
#U
    #update_person(conn, person_id = 3, person_firstname="Alexciss")
#D
    #delete_person (conn, person_id=2)
#close
    #conn.close()