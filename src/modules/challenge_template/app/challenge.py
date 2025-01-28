import boto3
from base64 import b64encode
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

s3 = boto3.client('s3')
ses = boto3.client('ses', region_name="sa-east-1")

BUCKET_NAME = 'challenge-storage-devcommunitymaua'
OBJECT_KEY = 'kick buttowski.png'
SOURCE_EMAIL = 'joao@devmaua.com'  
DESTINATION_EMAILS = ['22.01082-3@maua.br', '21.00410-2@maua.br']


def compose_email(image_base64):
    return f"""
    <html>
        <body>
            <p>Olá!</p>
            <p>Aqui está a imagem do personagem principal que Charles adorava assistir quando criança:</p>
            <img src="{image_base64}" alt="Imagem do Charles" style="max-width:50; height: auto;" />
        </body>
    </html>
    """


def lambda_handler(event, context):
    try:

        response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
        image_data = response['Body'].read()

     
        image_base64 = f"data:image/png;base64,{b64encode(image_data).decode('utf-8')}"

        email_body = compose_email(image_base64)

    
        response = ses.send_email(
            Source=SOURCE_EMAIL,
            Destination={'ToAddresses': DESTINATION_EMAILS},
            Message={
                'Subject': {
                    'Data': 'Imagem Favorita de Charles',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': email_body,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )

        return LambdaHttpResponse(status_code=200, body={"message": "E-mail enviado com sucesso!", "response": response}).toDict()

    except Exception as e:
        return LambdaHttpResponse(status_code=500, body={"error": str(e)}).toDict()
