import mysql.connector

class DataPool:
    def __init__ (self,test_case,module=None):
        self.test_case=test_case
        self.module=module

    def get(self,name):
        where=""
        if self.module:
            where="AND module='%s'" % self.module
        
        sql=''' SELECT value FROM test_data 
                WHERE test_case='%s'
                AND name='%s'
                AND status='active'
                '%s' ''' % (self.test_case,name,where)
        data=self.select_data(sql)
        if data:
            return data[0]
        else:
            raise Exception("no data")

    def select_data(self,sql):
        db=mysql.connector.connect(user='root',passwd="xl19760313",db="datapool")
        cursor=db.cursor()
        cursor.execute(sql)
        data=cursor.fetchone()
        db.close()
        return data

