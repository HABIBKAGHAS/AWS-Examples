## create a bucket

```sh
aws s3 mb s3://my-habib-bucket
```

## Create a file and put object with SS3-S3

```sh
echo "hello world" > hello.txt
aws s3 cp hello.txt s3://my-habib-bucket
```

## List KMS keys

```sh
aws kms list-keys
```

## Create KMS key

```sh
aws kms create-key
```

## put object with encryption with KMS

```sh

aws s3api put-object \
--bucket my-habib-bucket \
--key hello.txt \
--body hello.txt \
--server-side-encryption aws:kms \
--ssekms-key-id dbbcbf9e-5db8-432c-8b06-f481abba6785
```

## download the file

```sh
aws s3 cp s3://my-habib-bucket/hello.txt hello.txt
```

## put object with SSE-C [Failed attempt]

```sh
export BASE64_ENCODED_KEY=$(openssl rand -base64 32)
echo $BASE64_ENCODED_KEY

export MD5_VALUE=$($BASE64_ENCODED_KEY | md5sum | awk '{print $1}' | base64 -w0)
echo $MD5_VALUE

aws s3api put-object \
--bucket my-habib-bucket \
--key hello.txt \
--body hello.txt \
--sse-customer-algorithm AES256 \
--sse-customer-key $BASE64_ENCODED_KEY \
--sse-customer-key-md5 $MD5_VALUE
```

## put object with SSE-C [Success attempt]

```sh
openssl rand -out ssec.key 32

aws s3 cp hello.txt s3://my-habib-bucket/hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

## download the file encrypted with sse-c

```sh
aws s3 cp s3://my-habib-bucket/hello.txt hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

## cleanup

```sh
aws s3 rm s3://my-habib-bucket/hello.txt
aws s3 rb s3://my-habib-bucket
```
