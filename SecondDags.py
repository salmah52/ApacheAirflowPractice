# Create the imports block.
# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#Task 2: Create the DAG Arguments block. You can use the default settings

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Salmah Salmah',
    'start_date': days_ago(0),
    'email': ['lasisisalmah52@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


#Task 3: Create the DAG definition block. The DAG should run daily.

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_Server_Access_Log_Processing',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)

#Task 4: Create the download task.

#download task must download the server access log file which is available at the 
#URL: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-
#SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt

# define the tasks

# define the task 'download'

download = BashOperator(
    task_id='download',
    bash_command='wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt"',
    dag=dag,
)

#Here's a breakdown of the code:
#task_id='download': Sets the task identifier to 'download'. This is a unique name for the task within the DAG.
##dag=dag: Associates the task with a specific DAG (Directed Acyclic Graph). The dag parameter refers to the DAG object to which this task belongs.
#Task 5: Create the extract task.

#The server access log file contains these fields.
#a. timestamp - TIMESTAMP
#b. latitude - float
#c. longitude - float
#d. visitorid - char(37)
#e. accessed_from_mobile - boolean
#f. browser_code - int
#The extract task must extract the fields timestamp and visitorid.

# define the task 'extract'

extract = BashOperator(
    task_id='extract',
    bash_command='cut -f1,4 -d"#" web-server-access-log.txt > /home/project/airflow/dags/extracted.txt',
    dag=dag,
)

#Here's a breakdown of the code:

#task_id='extract': Sets the task identifier to 'extract'. This is a unique name for the task within the DAG.
#bash_command='cut -f1,4 -d"#" web-server-access-log.txt > /home/project/airflow/dags/extracted.txt': Specifies the Bash command to be executed. 
#The command uses the cut utility to extract fields 1 and 4 from the file 'web-server-access-log.txt'. The fields are delimited by the '#' character.
#The extracted data is then redirected to the file '/home/project/airflow/dags/extracted.txt'.
#dag=dag: Associates the task with a specific DAG (Directed Acyclic Graph). The dag parameter refers to the DAG object to which this task belongs.
#Overall, this task executes a Bash command to extract specific fields from a log file and stores the extracted data in a new file


#Task 6: Create the transform task.

#The transform task must capitalize the visitorid.

# define the task 'transform'

transform = BashOperator(
    task_id='transform',
    bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/extracted.txt > /home/project/airflow/dags/capitalized.txt',
    dag=dag,
)
#Here's a breakdown of the code:

#The command uses the tr utility to transform lowercase letters to uppercase. It reads the input from the file '/home/project/airflow/dags/extracted.txt' 
#and writes the transformed output to the file '/home/project/airflow/dags/capitalized.txt'.


#Task 7: Create the load task.

#The load task must compress the extracted and transformed data.


# define the task 'load'

load = BashOperator(
    task_id='load',
    bash_command='zip log.zip capitalized.txt' ,
    dag=dag,
)

#bash_command='zip log.zip capitalized.txt': Specifies the Bash command to be executed.
 #The command uses the zip utility to create a ZIP file named 'log.zip' containing the file 'capitalized.txt'.

#Task 8: Create the task pipeline block.
  # task pipeline

download >> extract >> transform >> load

 #cp  ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags




