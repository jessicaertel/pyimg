import boto3
import json

# Configurar o cliente do S3
s3_client = boto3.client('s3')

# Nome do bucket e do arquivo
bucket_name = 'nome-do-seu-bucket'
file_name = 'nome-do-seu-arquivo.json'

# Baixar o arquivo JSON do S3
def baixar_arquivo_json(bucket, file):
    response = s3_client.get_object(Bucket=bucket, Key=file)
    conteudo = response['Body'].read().decode('utf-8')
    dados_json = json.loads(conteudo)
    return dados_json

# Carregar os dados JSON no S3
def carregar_arquivo_json(bucket, file, dados):
    conteudo_json = json.dumps(dados)
    s3_client.put_object(Bucket=bucket, Key=file, Body=conteudo_json)

# Exemplo de uso
dados = baixar_arquivo_json(bucket_name, file_name)
print(dados)

# Modificar os dados JSON
dados['novo_campo'] = 'novo_valor'

# Carregar o arquivo modificado no S3
carregar_arquivo_json(bucket_name, file_name, dados)
