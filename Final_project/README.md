# Final project DevOps 2023
**Step 1 : Creating an EC2 using Terraform while Ansible installs Jenkins and Docker** 
-Create Terraform and AWS structure on your windows.
[Instructions](https://github.com/gakengabinatsume/DevOps2023/tree/main/Terraform/VPC_With_EC2)

-Create Ansible structure in GitHub

Files needed : 
1.Jenkins-playbook.yml
2.Docker-playbook.yml

-Check in AWS instance connect that everything went well
```
cd /var/log/

cat user-data.log 
```
**Step 2 : Configure Jenkins**
-Take the EC2 public IP from the output variables after Terraform created the infrastructure and connect on port 8080 (ec2-public-ip:8080) and follow the instructions from step 3.
[Instructions](https://github.com/gakengabinatsume/DevOps2023/blob/main/Jenkins.md)

**Step 3 : Create your Jenkins job**
Follow the below instructions :

[Instructions](https://github.com/gakengabinatsume/DevOps2023/tree/main/Jenkins_project)
