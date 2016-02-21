from django.db import models
from django.db import connection

# Create your models here.



class Universe(models.Model):
    camis = models.IntegerField(db_column='CAMIS', primary_key=True)
    dba = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    cuisine_description = models.CharField(max_length=200)
    inspection_date = models.CharField(max_length=500)
    action = models.CharField(max_length=500)
    violation_cd = models.CharField(max_length=10)
    violation_desc = models.TextField()
    critical_flag = models.CharField(max_length=25)
    grade = models.CharField(max_length=2)
    grade_date = models.CharField(max_length=500)
    violation_count = models.IntegerField()

    def get_univ_ids(self):
        cursor = connection.cursor()
        cursor.execute('''SELECT DISTINCT a.CAMIS,a.DBA,a.address, a.CUISINE_DESCRIPTION,
            a.INSPECTION_DATE,a.VIOLATION_COUNT, c.GRADE FROM
             (SELECT aa.CAMIS,aa.DBA,(aa.BUILDING||' '||aa.STREET||' '||aa.ZIPCODE) as address, aa.CUISINE_DESCRIPTION,
            aa.INSPECTION_DATE,COUNT(aa.VIOLATION_CD) as VIOLATION_COUNT FROM RESTAURANTS aa
            WHERE substr(aa.INSPECTION_DATE,7,4)||substr(aa.INSPECTION_DATE,1,2)||substr(aa.INSPECTION_DATE,4,2) =
             (SELECT DT FROM (SELECT CAMIS,
             MAX(substr(bb.INSPECTION_DATE,7,4)||substr(bb.INSPECTION_DATE,1,2)||substr(bb.INSPECTION_DATE,4,2))
             AS DT FROM RESTAURANTS bb
             WHERE aa.CAMIS = bb.CAMIS
             GROUP BY bb.CAMIS)
             )
             GROUP BY aa.CAMIS,aa.INSPECTION_DATE,aa.DBA,aa.BUILDING,aa.STREET,aa.ZIPCODE, aa.CUISINE_DESCRIPTION
             ) a
             LEFT OUTER JOIN
             (SELECT CAMIS,INSPECTION_DATE, GRADE FROM RESTAURANTS ) c
             on c.CAMIS=a.CAMIS and a.INSPECTION_DATE = c.INSPECTION_DATE''')
        row = cursor.fetchall()
        return row






