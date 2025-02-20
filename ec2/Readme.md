## generate key

```sh
ssh-keygen -t rsa -f ec2connect
```

## Send SSH key to AWS

```sh
aws ec2-instance-connect send-ssh-public-key \
--region eu-north-1 \
--instance-id i-00ac951018ba5d9b3 \
--availability-zone eu-north-1a \
--instance-os-user ec2-user \
--ssh-public-key file://ec2connect.pub
```

## Connect with EC2 using ssh

```sh
ssh -i ec2connect ec2-user@ec2-13-61-149-128.eu-north-1.compute.amazonaws.com
```
