## Create a bucket

```sh
aws s3api create-bucket --bucket my-habib-bucket \
--create-bucket-configuration LocationConstraint=eu-north-1
```

## Turn off block public access for ACLs

```sh
aws s3api put-public-access-block \
    --bucket my-habib-bucket \
    --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

## get publi access configuration

```sh
aws s3api get-public-access-block \
    --bucket my-habib-bucket
```

## change bucket ownership

```sh
aws s3api put-bucket-ownership-controls \
 --bucket my-habib-bucket \
 --ownership-controls="Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
```

## Cleanup

```sh
aws s3 rm s3://my-habib-bucket/file.txt
aws s3 rb s3://my-habib-bucket
```
