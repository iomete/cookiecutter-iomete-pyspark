"""Main module."""

from pyspark.sql import SparkSession

from {{ cookiecutter.project_slug }}.job_example import JobExample


def start_job(spark: SparkSession, config):
    job = JobExample(spark, config)
    job.create_table_from_dataset()
