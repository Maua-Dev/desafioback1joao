import boto3

def list_s3_objects(bucket_name, region="sa-east-1"):
    s3_client = boto3.client('s3', region_name=region)
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"Arquivo: {obj['Key']}")
    else:
        print("Nenhum arquivo encontrado no bucket.")

# Chame a função
list_s3_objects("challenge-storage-devcommunitymaua")
