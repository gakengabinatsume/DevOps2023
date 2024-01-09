# Jenkins
**Jenkins is an open-source automation server that is widely used for continuous integration and continuous delivery (CI/CD) processes in software development. It allows developers to automate the building, testing, and deployment of their applications, making the development process more efficient and reliable. Jenkins supports a wide range of plugins and integrations, enabling it to work with various tools and technologies. It is highly customizable and can be configured to meet specific project requirements.**

![alt text](https://i.ytimg.com/vi/PKcGy9oPVXg/maxresdefault.jpg)

**Step 1 : Install Java & Jenkins**

`sudo apt-get update`

`sudo apt install fontconfig openjdk-17-jre`

`sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian/jenkins.io-2023.key`

`echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null`

`sudo apt-get update`

`sudo apt-get install jenkins`

**Step 2 : Start Jenkins**

`sudo systemctl enable jenkins`

`sudo systemctl start jenkins`

`sudo systemctl status jenkins`

**Step 3 : Unlocking Jenkins**

Browse to http://localhost:8080 and from the Jenkins console log output, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks)

![alt text](https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-01-unlock-jenkins-page.jpg)

**Step 4 : Customizing Jenkins with plugins**

Manage Jenkins -> Manage Plugins

![alt text](https://www.jenkins.io/doc/book/resources/managing/plugin-manager-update.png)

**Step 5 : Create first admin user**
![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--mIX091HC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lx5vfv5a9vo8hhb68cm9.png)