## Create a bucket

aws s3 mb s3://my-habib-bucket

## create a file

echo "Hello World" > file.txt
aws s3 cp file.txt s3://my-habib-bucket --storage-class STANDARD_IA

## Cleanup

aws s3 rm s3://my-habib-bucket/file.txt
aws s3 rb s3://my-habib-bucket
