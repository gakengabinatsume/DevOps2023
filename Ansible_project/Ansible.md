# Ansible master & nodes
**Ansible is an open-source automation tool that allows users to automate various IT tasks, such as configuration management, application deployment, and orchestration. It uses a simple and human-readable language called YAML to define tasks and playbooks, which are sets of instructions for Ansible to execute on remote systems.**

**nsible operates over SSH and does not require any additional software to be installed on the managed nodes, making it easy to set up and use. It is widely used in DevOps practices to streamline and automate infrastructure management processes.**

![alt text](https://www.devopsschool.com/blog/wp-content/uploads/2019/07/Understanding-Ansible-Architecture-using-diagram1.png)

**Step 1 : Install ansible on the master node**

`sudo apt-get update`

`sudo apt install software-properties-common`

`sudo add-apt-repository --yes --update ppa:ansible/ansible`

`sudo apt install ansible`
