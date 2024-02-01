# How to make a Jenkins pipeline for a Python script to Docker image ?

**Step 1 : Add the necessary documents in Github.**

- Python script. 
- Docker file
- Jenkins file

**Step 2 : Create a Multibranch Pipeline in Jenkins**
- Add your GitHub repository.
![Branch Source](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/677b5e18-2443-4a57-9c53-f48ffcada8c8)
- Add your Jenkinsfile path from your repository.
![Build](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/09e5114a-27a9-41b5-acfa-125fcdab610c)
- Add your DockerHub repository.
![Docker conf](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/df7d50e4-da6f-42ef-8266-7ccbba39df46)
- Make sure Jenkins is in the docker group, if not use the comand :
```
sudo usermod -a -G docker jenkins
```

**Step 3 : Scan and trigger the build**

![Scan](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/5f7510c6-cf58-4b63-a209-e2286c6be15e)

**Step 4 : Pull the image from Dockerhub and run it**

![alt text](Dockercontainer.png)



