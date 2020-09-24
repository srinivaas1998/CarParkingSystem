import psycopg2
from ocr_final import ocr

from datetime import datetime
now = datetime.now()


def insert_entry(id,car_no,entry_time):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO entry(id,car_no,entry_time)
             VALUES(%s,%s,%s) ;"""
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (id,car_no,entry_time))

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_park(id,car_no):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE park
                SET car_no = %s
                WHERE id = %s"""

    conn = None
    updated_rows = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (car_no, id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def update_alloted():
    """ update vendor name based on the vendor id """
    sql = """ UPDATE park
                SET alloted = TRUE
                WHERE car_no is not null"""

    conn = None
    updated_rows = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def update_park1():
    """ update vendor name based on the vendor id """
    sql = """ UPDATE entry
                SET  parking_alloted=p.parking 
                FROM entry e,park p
                WHERE (e.car_no = p.car_no) and (e.id = p.id) """

    conn = None
    updated_rows = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    insert_entry(2, ocr("000.png") ,now)
    update_park(2, ocr("000.png"))
    update_alloted()
    update_park1()



