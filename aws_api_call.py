import requests
import json
import boto3
from requests_aws_sign import AWSV4Sign as Sigv4


def SignedRequests(iamCreds):

    ACCESS_KEY = iamCreds['accessKeyId']
    SECRET_KEY = iamCreds['secretAccessKey']

    try:
        session = boto3.Session(
            aws_access_key_id = ACCESS_KEY,
            aws_secret_access_key = SECRET_KEY
        )

        credentials = session.get_credentials()
        region = 'us-east-1' ## set to the region of the API
        service = 's3' ## set to the service
        url = 'ENDPOINT GOES HERE' ## set to your endpoint
        auth = Sigv4(credentials,region,service)
        return auth

def ExampleApiCall(creds):
    try:
        url = 'some endpoint'
        auth = Sigv4(creds)
        payload = 'some payload' ## omit if the service doesn't post data
        r = requests.post(url,auth=auth,json=payload)
        r = json.loads(r.content.decode())
        print(json.dumps(r, indent=4))
    except Exception as e:
        print(e)

iamCreds = json.loads(open('creds.json','r').read()))['credentials']
Sigv4(iamCreds)
