from Crypto.Cipher import AES
import base64
import boto3

# Load the encryption key
with open("my_s3_encryption_key.txt", "rb") as key_file:
    encryption_key = base64.b64decode(key_file.read().strip())

def encrypt_data(data):
    cipher = AES.new(encryption_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext

def upload_encrypted_file(file_path, bucket, key):
    s3_client = boto3.client("s3")
    with open(file_path, "rb") as file:
        encrypted_data = encrypt_data(file.read())
        s3_client.put_object(Bucket=bucket, Key=key, Body=encrypted_data)

upload_encrypted_file("test.txt", "my-habib-bucket", "encrypted/test.txt")
