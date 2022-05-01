from pyhocon import ConfigFactory
from pyspark.sql import SparkSession


def get_config(application_path):
    return ConfigFactory.parse_file(application_path)


class PySparkLogger:
    def __init__(self, spark: SparkSession):
        self.log4jLogger = spark.sparkContext._jvm.org.apache.log4j

    def get_logger(self, name: str):
        return self.log4jLogger.LogManager.getLogger(name)
