
class MyConnection:


    def getMyConnection():
        
        from sqlalchemy import create_engine, text
        import psycopg2
        
        engine = psycopg2.connect(
        database="healthshare",
        user="postgres",
        password="123456",
        host="localhost",
        port='5432')

        return engine