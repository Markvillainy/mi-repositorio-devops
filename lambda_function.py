import json
import random

def lambda_handler(event, context):
    """
    Función Lambda para el Proyecto Final de DevOps.
    Genera una respuesta JSON aleatoria simulando un microservicio activo.
    """
    
    mensajes = [
        "Servidor Serverless activo",
        "Conexión exitosa a la red central",
        "Microservicio A procesando datos...",
        "Arquitectura de nube validada"
    ]
    
    # Construcción de la respuesta
    respuesta = {
        'mensaje': random.choice(mensajes),
        'estudiante': 'Mark',
        'proyecto': 'DevOps Final AWS',
        'status': 'Online'
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(respuesta)
    }