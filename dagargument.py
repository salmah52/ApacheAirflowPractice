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
