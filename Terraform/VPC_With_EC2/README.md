# VPC_With_EC2 in AWS with Terraform

**Step 1 : Install Terraform**

[Install](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

[Instructions](https://stackoverflow.com/questions/1618280/where-can-i-set-path-to-make-exe-on-windows)

**Step 2 : Install AWS CLI and add your access key**

[Install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

[Instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

![Access_key](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/35815b72-4fa2-4bca-9c0b-8e6a20a56583)

**Step 3 : Add the files on your system**

Files needed:
- main.tf
- outputs.tf
- terraform.tfvars
- variables.tf
- YourZoneKeyPair.perm
  
**Step 4 : Use the below command to create the infrastructure**
```
terraform init && terraform validate && terraform plan && terraform apply --auto-approve
```
**Step  : Use the below command to destroy the infrastructure**
```
terraform destroy --auto-approve
```
