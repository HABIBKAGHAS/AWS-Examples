## Convert to json

```sh
yq eval -o=json '.' policy.yml > policy.json

```

## Create policy

```sh
aws iam create-policy \
--policy-name my-test-policy \
--policy-document file://policy.json
```

## attach user policy

```sh
aws iam attach-user-policy \
--policy-arn arn:aws:iam::376129873245:policy/my-test-policy \
--user-name test-policy-users
```
