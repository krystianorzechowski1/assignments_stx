from pyspark.sql.types import StructType,IntegerType,BooleanType, FloatType, StringType, StructField
import pyspark

from pyspark.sql import SparkSession

def write_for_df(idx, dframe:pyspark.sql.DataFrame):
    dframe.write.format('jdbc').options(
      url='jdbc:mysql://foo_db_1:3306/spark',
      driver='com.mysql.jdbc.Driver',
      dbtable=f'assignment_{idx}',
      user='spark',
      password='spark',
      truncate=True
      ).mode('Overwrite').save()


def process(queries):
	for idx, query in enumerate(queries):
		df = spark.sql(query)
		write_for_df(idx + 1, df)

spark = SparkSession.builder.appName("").getOrCreate()
schema = StructType([
    StructField('Survived', IntegerType()),
    StructField('Pclass', IntegerType()),
    StructField('Name', StringType()), 
    StructField('Sex', StringType()),
    StructField('Age', IntegerType()),
    StructField('Siblings/Spouses Aboard', IntegerType()),
    StructField('Parents/Children Aboard', IntegerType()),
    StructField('Fare', FloatType()),
    ])

df = spark.read.option('header',True).schema(schema).csv('/home/jovyan/data/titanic.csv')

df = df.withColumn("Survived",df.Survived.cast(BooleanType()))
df.createOrReplaceTempView("titanic")

q1 = '''
    select 
        count(*) * 100.0 / (select count(*) from titanic) as result
    from 
        titanic 
        where survived == true and age < 18
    '''
# #jaki procent dzieci przeżył katastrofę
q2 = '''
    select 
        count(*) * 100.0 / (select count(*) from titanic) as result
    from 
        titanic 
        where survived == true and age between 18 and 40
    '''
# #jaki procent dorosłych do 40 roku życia przeżył katastrofę
q3 = '''
    select
        sex,
        count(*) * 100.0 / (select count(*) from titanic) as result
    from 
        titanic 
        where survived == true and age between 18 and 40
        group by sex
    '''
# #jaki procent dorosłych do 40 roku życia przeżył katastrofę z podziałem na płeć
q4 = '''
    select
        count(*) * 100.0 / (select count(*) from titanic) as result
    from 
        titanic 
        where survived == true and age > 40
    '''
q5 = '''
    select
        sex,
        count(*) * 100.0 / (select count(*) from titanic) as result
    from 
        titanic 
        where survived == true and age > 40
        group by sex
    '''
q6 = '''
    select
        Pclass,
        sex,
        count(*) * 100.0 / (select count(*) from titanic) as result
    from 
        titanic 
    where 
        survived == true and age > 40
    group by Pclass, sex
    order by Pclass, sex
    '''

process([q1,q2,q3,q4,q5,q6])
