#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Salmah Lasisi',
    'start_date': days_ago(0),
    'email': ['lasisisalmah52@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



#DAG arguments are like settings for the DAG.

#he above settings mention

#the owner name,
#when this DAG should run from: days_age(0) means today,
#the email address where the alerts are sent to,
#whether alert must be sent on failure,
#whether alert must be sent on retry,
#the number of retries in case of failure, and
t#he time delay between retries.
