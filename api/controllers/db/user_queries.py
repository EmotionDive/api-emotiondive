from api.controllers.db.db_connection import get_db

def insert_user(
    username: str, 
    email: str, 
    password: str, 
    age: int, 
    sex: str, 
    civil_status: str, 
    housing_situation: int, 
    active_account: str
):
    """
    Insert a new user on the table 'usuarios'.

    :username: The username provided by the user
    :email: The email of the user
    :password: Hashed password of the user
    :age: Age of the user
    :sex: Sex of the user
    :civil_status: Civil status provided by the user
    :housing_situation: Housing status ID provided by the user's selected option
    :active_acount: Describes the status of the account
    """
    db_connection = get_db()
    with db_connection.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(username, correo, edad, sexo, estado_civil, id_situacion_habitacional, active_account) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (username, email, age, sex, civil_status, housing_situation, active_account))
        cursor.execute("INSERT INTO usuario_password(username_usuario, user_password) VALUES (%s, %s)",
                       (username, password))
    db_connection.commit()
    db_connection.close()

def get_user(username: str) -> list:
    """
    Function to get info of a user given their username.

    :username: username provided by the user
    :return: Returns a list of the user data
    """
    db_connection = get_db()
    user_data = None
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario WHERE username = %s ", (username))
        user_data = cursor.fetchone()       
    db_connection.close()
    return user_data

def update_user(
    username: str,
    age: int, 
    sex: str, 
    civil_status: str, 
    housing_situation: str,
):
    """
    Permits to update certain info of the user account on the table 'usuarios'.

    :username: The username of the user
    :age: Age of the user
    :sex: Sex of the user
    :civil_status: Civil status provided by the user
    :housing_situation: Housing status provided by the user
    """
    db_connection = get_db()
    with db_connection.cursor() as cursor:
        cursor.execute("UPDATE usuario SET age = %i, sex = %s, civil_status = %s, housing_situation = %s WHERE username = %s",
                       (age, sex, civil_status, housing_situation, username))
    db_connection.commit()
    db_connection.close() 

def delete_user(username: str):
    """
    Function to delete a user from the table 'usuarios'.

    :username: Username provided by the user
    """
    db_connection = get_db()
    with db_connection.cursor() as cursor:
        cursor.execute("DELETE FROM usuario_password WHERE username_usuario = %s ", (username))
        cursor.execute("DELETE FROM usuario WHERE username = %s ", (username))
    db_connection.commit()          
    db_connection.close()

