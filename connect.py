import psycopg2
from ocr_final import ocr

from datetime import datetime
now = datetime.now()


def db_add(car):
    def insert_entry(car_no,entry_time):
        """ insert a new vendor into the vendors table """
        max_id_sql = """ SELECT MAX(id) from entry"""
        sql = """INSERT INTO entry(id,car_no,entry_time)
                 VALUES(%s,%s,%s) ;"""
        conn = None
        try:
            # connect to the PostgreSQL database
            conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(max_id_sql)
            id = cur.fetchone()[0]
            if id == None:
                new_id=0
            else:
                new_id=int(id)+1
            cur.execute(sql, (new_id,car_no,entry_time))

            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def update_park(car_no):
        """ update vendor name based on the vendor id """
        sql = """ UPDATE park
                    SET car_no=%s
                    WHERE id=(SELECT id FROM park WHERE alloted = FALSE
                    ORDER BY id LIMIT 1)"""

        conn = None
        updated_rows = 0
        try:
            # connect to the PostgreSQL database
            conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
            # create a new cursor
            cur = conn.cursor()
            # execute the UPDATE  statement
            cur.execute(sql, (car_no,))
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


    def update_alloted(car_no):
        """ update vendor name based on the vendor id """
        sql = """ UPDATE park
                    SET alloted = TRUE
                    WHERE car_no = %s """

        conn = None
        updated_rows = 0
        try:
            # connect to the PostgreSQL database
            conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
            # create a new cursor
            cur = conn.cursor()
            # execute the UPDATE  statement
            cur.execute(sql, (car_no,))
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

    def update_park1(car_no):
        """ update vendor name based on the vendor id """
        sql = """ UPDATE entry
                    SET parking_alloted=(SELECT parking FROM park
                    WHERE car_no = %s LIMIT 1)
                    WHERE car_no = %s """

        conn = None
        updated_rows = 0
        try:
            # connect to the PostgreSQL database
            conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
            # create a new cursor
            cur = conn.cursor()
            # execute the UPDATE  statement
            cur.execute(sql, (car_no,car_no,))
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

    def select(car_no):
        conn = None
        par = ""
        try:
            # connect to the PostgreSQL database
            conn = psycopg2.connect("dbname=Car user=postgres password=chinku")
            # create a new cursor
            cur = conn.cursor()
            sql = "SELECT parking_alloted from entry where car_no = '" + car_no + "'"
            # execute the UPDATE  statement
            cur.execute(sql)
            par = cur.fetchone()[0]
            # get the number of updated rows

            # Commit the changes to the database
            conn.commit()
            # Close communication with the PostgreSQL database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return par

    insert_entry(car ,now)
    update_park(car)
    update_alloted(car)
    update_park1(car)
    return select(car)




