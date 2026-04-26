import boto3
import uuid
from datetime import datetime

# Configuración de clientes
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('AuditoriaRecursos')

def ejecutar_respaldo():
    nombre_archivo = "evidencia_punto10.txt"
    bucket_nombre = "proyecto-devops-avance-767398131772"
    
    # 1. Crear archivo localmente
    contenido = f"Evidencia de respaldo generada el {datetime.now()}"
    with open(nombre_archivo, "w") as f:
        f.write(contenido)
    
    try:
        # 2. Subir a S3
        print(f"Subiendo {nombre_archivo} a S3...")
        s3.upload_file(nombre_archivo, bucket_nombre, nombre_archivo)
        
        # 3. Registrar en DynamoDB
        id_log = f"LOG-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        print(f"Registrando evento {id_log} en DynamoDB...")
        
        tabla.put_item(
            Item={
                'id': id_log,
                'fecha': str(datetime.now()),
                'servicio': 'S3/Dynamo',
                'estado': 'Activo'
            }
        )
        print("¡Proceso completado con éxito!")
        
    except Exception as e:
        print(f"Error en la ejecución: {e}")

if __name__ == "__main__":
    ejecutar_respaldo()