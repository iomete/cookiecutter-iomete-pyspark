#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

from {{ cookiecutter.project_slug }}.main import start_job
from {{ cookiecutter.project_slug }}.utils import get_config
from tests._spark_session import get_spark_session

# set in the application.conf
test_table_name = "tbl1"


def test_happy_path():
    # create test spark instance
    test_config = get_config("application.conf")
    spark = get_spark_session()

    # run target
    start_job(spark, test_config)

    # check
    df = spark.sql(f"select * from {test_table_name}")
    df.printSchema()
    assert df.count() > 0
