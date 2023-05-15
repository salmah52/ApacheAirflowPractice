# define the DAG
dag = DAG(
    dag_id='sample-etl-dag',
    default_args=default_args,
    description='Sample ETL DAG using Bash',
    schedule_interval=timedelta(days=1),
)


#Here we are creating a variable named dag by instantiating the DAG class with the following parameters.

#sample-etl-dag is the ID of the DAG. This is what you see on the web console.

#We are passing the dictionary default_args, in which all the defaults are defined.

#description helps us in understanding what this DAG does.

#schedule_interval tells us how frequently this DAG runs. In this case every day. (days=1).
