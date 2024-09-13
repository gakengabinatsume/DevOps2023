**Step 1 : Create an EC2 and install Git & Ansible with user_data to install Jenkins, Docker, PHP and Composer

- Create Ansible structure in GitHub :

   1. Jenkins-playbook.yml

   2. PHP-playbook.yml

   3. Composer-playbook.yml

- Check in AWS instance connect that everything went well
```
cd /var/log/
          
cat user-data.log 
```
**Step 2 : Configure Jenkins**

- Take the EC2 public IP from **** and connect on port 8080
(ec2-public-ip:8080) and follow the bellow instructions:

**Step A : Unlocking Jenkins**

Browse to http://localhost:8080 and from the Jenkins console log output, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks)

![alt text](https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-01-unlock-jenkins-page.jpg)

**Step B : Create first admin user**

![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--mIX091HC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lx5vfv5a9vo8hhb68cm9.png)

**Step C : Manage plugins to send e-mail notification**

-System-wide configuration
Before using this plugin from a project, you must first configure some system-wide settings. Go to the Jenkins system-wide configuration page (Manage Jenkins, Configure System).

The configuration for this plugin can be found in the section entitled Extended E-mail Notification. This configuration should match the settings for your SMTP mail server. This section mirrors that of the Mailer plugin in the E-mail Notification section; however, there are a few additions. The fields labeled Default Subject and Default Content allow you to configure the subject and content on a system-wide level. The field labeled Default Recipients can be used to set a default list of email addresses for all projects using this plugin (and can be overridden at the project level); this can be used to greatly simplify the configuration you need to do for all projects.

-Project configuration
For a project to use this plugin, you need to enable it in the project configuration page. In the Post-build Actions section, click on Add post-build action and then select Editable Email Notification.

There are three main fields that you can edit when this plugin is enabled:

Project Recipient List
This is a comma (or whitespace) separated list of email recipients. Allows you to specify a single recipient list for each email that is sent.

Default Subject
This allows you to configure a token (more about tokens later) that can be used to easily configure all email subjects for the project.

Default Content
Same as Default Subject, but for the email body instead of the subject.

**Step 3 : Create your Jenkins job**

- Create a Multibranch Pipeline
- Add your GitHub repository.
![Branch Source](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/677b5e18-2443-4a57-9c53-f48ffcada8c8)
- Add your Jenkinsfile path from your repository.
![Build](https://github.com/gakengabinatsume/DevOps2023/assets/141765846/09e5114a-27a9-41b5-acfa-125fcdab610c)
-Scan and trigger the build

