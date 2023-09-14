import boto3
import json

# Configuración inicial
sqs_queue_url = 'YOUR_SQS_QUEUE_URL' # Reemplaza con la URL de tu cola SQS
eventbridge_bus_name = 'e-commerce-events'

# Inicializar clientes de EventBridge
eventbridge_client = boto3.client('events')

def lambda_handler(event, context):
    # AWS Lambda invocada por SQS pasa el mensaje como parte del evento
    for record in event['Records']:
        # Cargar el cuerpo del mensaje (que contiene nuestro evento original)
        sqs_message = json.loads(record['body'])
        
        # Cambiar el detail-type a "OrderApproved"
        sqs_message['detail-type'] = 'OrderApproved'
        
        # Depositar el evento modificado en EventBridge
        eventbridge_client.put_events(
            Entries=[
                {
                    'EventBusName': eventbridge_bus_name,
                    'Source': sqs_message['source'],
                    'DetailType': sqs_message['detail-type'],
                    'Detail': json.dumps(sqs_message['detail'])
                }
            ]
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Processed message successfully.')
    }
