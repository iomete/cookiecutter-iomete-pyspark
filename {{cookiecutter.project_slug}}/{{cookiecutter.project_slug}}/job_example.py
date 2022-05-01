import logging

from pyspark.sql import SparkSession

from {{ cookiecutter.project_slug }}.utils import PySparkLogger

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

project_logger = logging.getLogger("src")
project_logger.setLevel(logging.DEBUG)

logger = logging.getLogger("JobExample")
logger.setLevel(logging.DEBUG)


class JobExample:
    def __init__(self, spark: SparkSession, config):
        self.spark = spark
        self.config = config

        # self.spark.sparkContext.setLogLevel("INFO")
        self.logger = PySparkLogger(spark).get_logger(__name__)

        self.logger.info("pyspark script logger initialized")

    def create_table_from_dataset(self):
        self.logger.info("create_table_from_dataset started")

        table_name = self.config["table_name"]

        self.logger.debug("Destination table name is {}".format(table_name))

        data = [
            ('James', {'hair': 'black', 'eye': 'brown'}),
            ('Michael', {'hair': 'brown', 'eye': None}),
            ('Robert', {'hair': 'red', 'eye': 'black'}),
            ('Washington', {'hair': 'red', 'eye': 'grey'}),
            ('Jefferson', {'hair': 'red', 'eye': ''})
        ]

        df = self.spark.createDataFrame(data=data, schema=["name", "properties"])

        df.createOrReplaceTempView("tmpTable")

        self.spark.sql(f"""create or replace table {table_name} as select * from tmpTable""")

        self.logger.info("create_table_from_dataset finished!")
