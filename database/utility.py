from database.connection import database_config, cursor

# add user function
def addUser(username:str, email:str, password:str):
    # add data into users table
    try:
        add_user_query = """
                INSERT INTO USERS(USERNAME, EMAIL, PASSWORD)
                VALUES(%s, %s, %s);"""
        cursor.execute(add_user_query,(username, email, password))
        database_config.commit()
        return True
    except Exception as e:
        return f"Someting wrong in database/utility.py:{e}"
    
# check user exists in users table
def checkUserStatus(username:str):
    try:
        check_user_query = """
                    SELECT USERID FROM USERS 
                    WHERE EMAIL = %s;"""
        cursor.execute(check_user_query,(username,))
        userid = cursor.fetchone()  #(userid, )
        if userid:
            return True
        else:
            return False
        
    except Exception as e:
        return f"Someting wrong in database/utility.py:{e}"

# get password from db
def getPassowordFromDB(username:str):
    try:
        check_user_query = """
                    SELECT password FROM USERS 
                    WHERE EMAIL = %s;"""
        cursor.execute(check_user_query,(username,))
        password = cursor.fetchone()[0]  #(userid, )
        return password
    except Exception as e:
        return f"Someting wrong in database/utility.py:{e}"
    

# update password in database
def updatePassword(email:str, password:str):
    try:
        update_password_query = """UPDATE USERS SET PASSWORD = %s 
                                    WHERE EMAIL = %s;"""
        cursor.execute(update_password_query,(password, email))
        row_count = cursor.rowcount
        if row_count == 1:
            database_config.commit()
            return True
        else:
            database_config.rollback()
            return False
    except Exception as e:
        return f"Someting wrong in database/utility.updatePassword:{e}"
    


## add notes
def addNotesInDB(email:str, title:str, content:str):
    # get userid
    try:
        get_userid_query = """select userid from users where email = %s;"""
        cursor.execute(get_userid_query,(email,))
        userid = cursor.fetchone()[0]
        add_notes_query = """insert into notes(userid, email, title, content)
                            values(%s, %s, %s, %s);"""
        cursor.execute(add_notes_query, (userid, email, title, content))
        database_config.commit()
        return True
    except:
        return False
    


# get  notes from db
def getNotesFromDB(email):
    query = "SELECT noteid, title, content FROM notes WHERE email=%s"
    cursor.execute(query, (email,))
    return cursor.fetchall()


def getNoteById(note_id, email):
    query = """
    SELECT noteid, title, content
    FROM notes
    WHERE noteid=%s AND email=%s
    """
    cursor.execute(query, (note_id, email))
    return cursor.fetchone()
def updateNoteInDB(note_id, email, title, content):
    query = """
    UPDATE notes
    SET title=%s, content=%s
    WHERE noteid=%s AND email=%s
    """
    cursor.execute(query, (title, content, note_id, email))
    database_config.commit()
    return cursor.rowcount == 1

def deleteNoteFromDB(note_id, email):
    query = """
    DELETE FROM notes
    WHERE noteid=%s AND email=%s
    """
    cursor.execute(query, (note_id, email))
    database_config.commit()
    return cursor.rowcount == 1