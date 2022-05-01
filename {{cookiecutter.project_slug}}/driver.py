from pyspark.sql import SparkSession

from {{ cookiecutter.project_slug }}.main import start_job
from {{ cookiecutter.project_slug }}.utils import get_config

spark = SparkSession.builder \
    .appName("Job1") \
    .getOrCreate()

production_config = get_config("/etc/configs/application.conf")

start_job(spark, production_config)
