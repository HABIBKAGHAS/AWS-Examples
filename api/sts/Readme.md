## Create a user with no permissions

```sh
aws iam create-user --user-name sts-machine-user

aws iam create-access-key \
    --user-name sts-machine-user

aws configure --profile sts

aws sts get-caller-identity --profile sts

aws s3 ls --profile sts # make sure we dont have access to s3
```

## Create a Role

## Use new user credentials and assume role

```sh
aws iam put-user-policy \
--user-name sts-machine-user \
--policy-name assumeRolePolicy \
--policy-document file://policy.json
```

```sh
aws sts assume-role \
 --role-arn arn:aws:iam::376129873245:role/my-sts-stack-StsRole-7s2pYq0ghDKj \
 --role-session-name s3-sts-fun \
 --profile sts
```

```sh
aws sts get-caller-identity --profile assumedRole
aws s3 ls --profile assumedRole
```

## Clean up

tear down the stack
