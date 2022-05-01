FROM iomete/spark-py:3.2.1.0

WORKDIR "/app"

# Reset to root to run installation tasks
USER 0

COPY .. /app/

RUN pip install .

# Specify the User that the actual main process will run as
ARG spark_uid=185
USER ${spark_uid}
