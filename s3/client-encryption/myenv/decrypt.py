from Crypto.Cipher import AES
import base64
import boto3


# Load the encryption key
with open("my_s3_encryption_key.txt", "rb") as key_file:
    encryption_key = base64.b64decode(key_file.read().strip())

def decrypt_data(encrypted_data):
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    cipher = AES.new(encryption_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

def download_and_decrypt(bucket, key, output_file):
    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=bucket, Key=key)
    encrypted_data = response["Body"].read()
    decrypted_data = decrypt_data(encrypted_data)
    
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

download_and_decrypt("my-habib-bucket", "encrypted/test.txt", "decrypted_test.txt")
