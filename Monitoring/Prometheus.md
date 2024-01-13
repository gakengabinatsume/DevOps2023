# How to make a Jenkins pipeline for a Python script to Docker image ?

**Step 1 : Add the necessary documents in Github.**

- Python script. 
- Docker file
- Jenkins file

**Step 2 : Create a Multibranch Pipeline in Jenkins**
- Add your GitHub repository.
![alt text](BranchSource.jpg)
- Add your Jenkinsfile path from your repository.
![alt text](Build.jpg)
- Add your DockerHub repository.
![alt text](Dockerconf.jpg)

**Step 3 : Scan and trigger the build**

![alt text](Scan.jpg)

**Step 4 : Pull the image from Dockerhub and run it**

![alt text](Dockercontainer.png)
