import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')
    db_instance_id = "rds-auto-start-stop-poc"
    response = rds.stop_db_instance(DBInstanceIdentifier=db_instance_id)
    print(f"Stopping RDS instance: {db_instance_id}")
    return response