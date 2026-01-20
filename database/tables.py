from database.connection import database_config, cursor

# creating tables function defination
def create_tables():
    
    users_table_query = """CREATE TABLE IF NOT EXISTS USERS (
            USERID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique ID for each user
            USERNAME VARCHAR(40),                        -- Optional username
            EMAIL VARCHAR(50) NOT NULL UNIQUE,           -- Unique email
            PASSWORD VARCHAR(255) NOT NULL          -- Store hashed password, not plain text
        );"""
    cursor.execute(users_table_query)

    notes_table_query = """CREATE TABLE IF NOT EXISTS NOTES (
                    NOTEID INT AUTO_INCREMENT,
                    USERID INT NOT NULL,
                    EMAIL VARCHAR(30) NOT NULL,
                    TITLE VARCHAR(100) NOT NULL,
                    CONTENT MEDIUMTEXT,
                    LAST_UPDATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (NOTEID),
                    FOREIGN KEY (USERID) REFERENCES USERS(USERID)
                        ON DELETE CASCADE
                        ON UPDATE CASCADE
                    );"""
    cursor.execute(notes_table_query)
    database_config.commit()
    print("Tables created successfully")