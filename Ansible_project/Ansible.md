# Ansible master & nodes
**Ansible is an open-source automation tool that allows users to automate various IT tasks, such as configuration management, application deployment, and orchestration. It uses a simple and human-readable language called YAML to define tasks and playbooks, which are sets of instructions for Ansible to execute on remote systems.**

**nsible operates over SSH and does not require any additional software to be installed on the managed nodes, making it easy to set up and use. It is widely used in DevOps practices to streamline and automate infrastructure management processes.**

![alt text](https://www.devopsschool.com/blog/wp-content/uploads/2019/07/Understanding-Ansible-Architecture-using-diagram1.png)

**Step 1 : Install ansible on the master node**

`sudo apt-get update`

`sudo apt install software-properties-common`

`sudo add-apt-repository --yes --update ppa:ansible/ansible`

`sudo apt install ansible`

**Step 2 : Check if it is done correctly**

`ansible --version`

**Step 3 : Generate a ssh key and copy it in the worker nodes**

`ssh-keygen`

`ssh-copy-id root@10.106.0.2`

`ssh-copy-id root@10.106.0.4`

`ssh-copy-id root@10.106.0.3`

**Step 4 : Create inventory file in ansible directory**

`cd /etc/ansible/`

`nano inventory`

**Step 5 : Check the ssh connection to the nodes**

` ansible -m ping all`
