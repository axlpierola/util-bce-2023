def lambda_handler(event, context):
    # Obtiene el nombre del archivo del evento de S3
    s3_event = event['Records'][0]['s3']
    file_name = s3_event['object']['key']
    
    print(f"Archivo procesado: {file_name}")

    return {
        'statusCode': 200,
        'body': f"Archivo {file_name} procesado con éxito!"
    }

