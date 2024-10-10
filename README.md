# Final project DevOps 2023

![Capture](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/cb5d92ee-dfa0-4189-ae5d-020322012810)

**Step 1 : Creating an EC2 using Terraform while Ansible installs Jenkins and Docker** 

- Create Terraform and AWS structure on your windows.
[Instructions](https://github.com/gakengabinatsume/Terraform/tree/main/VPC_With_EC2)

- Create Ansible structure in GitHub :

   1. Jenkins-playbook.yml

   2. Docker-playbook.yml
   
- Create Monitoring structure in GitHub :
   1. docker-compose.yaml

   2. prometheus.yaml
   
- Check in AWS instance connect that everything went well
```
cd /var/log/
          
cat user-data.log 
```
**Step 2 : Log into Docker on the EC2 and configure Jenkins**

```
docker login
sudo usermod -a -G docker jenkins #add jenkins user to docker group
sudo systemctl restart docker
sudo apt  install docker-compose
```

- Take the EC2 public IP from the output variables after Terraform created the infrastructure and connect on port 8080
(ec2-public-ip:8080) and follow the instructions from step 3.
[Instructions](https://github.com/gakengabinatsume/Jenkins_project/blob/main/Jenkins.md)

**Step 3 : Create your Jenkins job**

- Follow the instructions :
[Instructions](https://github.com/gakengabinatsume/Jenkins_project/tree/main)
- Make sure there are no # in your index.html file

**Step 4 : Monitor it with Prometheus and Grafana**
 ```
 cd /Ansible/DevOps2023/Monitoring/
```
- Follow the instructions :
[Instructions](https://github.com/gakengabinatsume/Monitoring)

**Step 5 : Create the docker container and open localhost:5000**
```
docker pull gabimiron96/final-project:tagname
```
```
docker run -p 5000:5000 -d imageid
```
```
docker stop containerid
```
