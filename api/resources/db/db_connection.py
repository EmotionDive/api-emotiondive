import pymysql

def get_db():
    """
    Creates a connection through a database given the provided data.
    """
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='emotion_dive'
    )
