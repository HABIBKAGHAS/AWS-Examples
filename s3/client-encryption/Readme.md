## Create a bucket

```sh
aws s3 mb s3://my-habib-bucket
```

## Create a file

```sh
echo "hello world" > hello.txt
aws s3 cp hello.txt s3://my-habib-bucket/hello.txt
```
