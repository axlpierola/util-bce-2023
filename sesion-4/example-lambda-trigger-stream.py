import boto3

# Inicializar el cliente de SNS
sns_client = boto3.client('sns')

# ARN del tema de SNS al que quieres enviar el mensaje
sns_topic_arn = "arn:aws:sns:us-west-2:111111111111:nombre-de-tu-topico"

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_image = record['dynamodb']['NewImage']
            status = new_image['Status']['BOOL']
            
            if status:
                task_id = new_image['TaskID']['S']
                message = f"Nuevo registro insertado con TaskID: {task_id}"
                
                sns_client.publish(
                    TopicArn=sns_topic_arn,
                    Message=message,
                    Subject='Nuevo Registro en DynamoDB'
                )
