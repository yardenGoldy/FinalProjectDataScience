from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def do_something(x):
    return x + 'hello'

sample_udf = udf(lambda x: do_something(x), StringType())