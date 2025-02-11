## Create a bucket

```sh
aws s3 mb my-habib-bucket
```

## Create bucket policy

```sh
aws s3api put-bucket-policy \
--bucket my-habib-bucket \
--policy file://policy.json
```
