## SSH 

## Git
### Intro

When we talk about tech company dealing with servers, code, new feature, and configuration everyday. Its important to have a centerlized repo or registry containiing the code andour configuration.
In this part of the series we will get in touch little bit with Git, not deep dive but only the core basics.

### Configure Git

First, if you do not have git you have to install it by checking ```git --version```.
if it there so its okay, but if not try.
```bash
sudo apt update
sudo apt install git -y
```

Now, you need to login into github.com then create a new repo 
- go to your profile icon, then settings,
- hit the `SSH keys` tap
- click `New SSH key`
- Grap your publick key from your machine `cat .ssh/id_225519.pub` we generated before
- Paste the key into the box then save
- Clone your repo then
- in your machine
  
  ```bash
   git clone <link provided>
  ```

   So thats is good now you have cloned your repo in your machine

  If you list files

   ```bash
   ls
   ```

  The expected output
  
  ```bash
  README.md
  ```
  For example, it may vary you may have more files in your repo.

  before we work in our file, we need to tell git first who we are.
  
  ```bash
  git config --global user.name "< your user name >"
  git config --global user.email "< your email address >"
  ```
   
  You can edit your file by

  ```bash
  nano README.md
  ```

   Edit what you need then commit the changes by

```bash
git status
git add README.md
git commit -m "updated README.md file"
git push origin master
```


That's it, very simple :) 

Thanks for reading.


## Running ad-hoc command

## Playbook

### Overview

An Ansible Playbook is a YAML-based automation definition that describes what tasks should be executed, on which hosts, and in what order, using Ansible modules to enforce a desired system state. A playbook consists of one or more plays, and each play targets a set of hosts defined in the inventory and executes a sequence of tasks. Unlike ad-hoc commands, playbooks are designed to be repeatable, version-controlled, and production-ready, making them the primary mechanism for configuration management, application deployment, and operational automation in Ansible.

### Writing our first playbook

The main benefits of using playbooks include readability, as YAML syntax is human-friendly and self-documenting; idempotency, meaning the same playbook can be run multiple times without causing unintended changes because tasks describe the desired state (for example, state: present installs a package only if it is missing); consistency and reliability, since the same automation can be applied across development, staging, and production environments; reusability and scalability, as playbooks can use variables, roles, and inventories to adapt to different hosts and environments; and automation safety, because changes are predictable, auditable, and easy to review through version control systems like Git.

For example, a simple playbook that installs apache2 on servers looks like this:
```bash
---

- hosts: all
  become: true
  tasks:
  - name: install apache2 package
    apt:
      name: apache2
```

In this example, the playbook targets the all hosts group, installs apache2 if it is not already installed. Running the playbook multiple times will not reinstall or restart apache2 unnecessarily, demonstrating idempotent behavior.

In practice, playbooks are used to automate common operational tasks such as provisioning servers, configuring applications, deploying updates, backing up configurations, and enforcing security baselines, which significantly reduces manual effort, configuration drift, and operational risk.

The tasks section is the core of the playbook. It is an ordered list of tasks, where each task calls exactly one Ansible module to perform a specific action. Tasks usually include a `name` for readability and a module with its parameters. One of the most important parameters you will see in many modules is `state`, which defines the desired end state of a resource. 

For example, `state: present` ensures a package, user, file, or resource exists; `state: absent` ensures it is removed; `state: started` or `stopped` controls whether a service is running; and `state: latest` ensures a package is installed and updated to the newest version.

By using state, Ansible achieves idempotency, meaning the same playbook can be run multiple times without causing unnecessary changes.

Tasks can also include additional attributes such as `when` for conditional execution, `loop` for repeating a task over multiple items, `register` to store the output of a task in a variable, `notify` to trigger handlers, and `tags` to allow selective execution of parts of the playbook. 

Handlers are special tasks, usually defined in a `handlers` section, that run only when notified by another task—commonly used for actions like restarting services after configuration changes.

Together, these attributes and sections allow a playbook to clearly define intent, control execution flow, manage system state through parameters like `state`, and deliver reliable, repeatable automation across different environments. We will see more examples further.

#### State

As we said before, state used to define the desired end state of a resourse. 

For example:

```bash
---

- hosts: all
  become: true
  tasks:
  - name: install apache2 package
    apt:
      name: apache2
      state: latest or present
```

This ensures that the apache2 is install in latses version.

what about if i need to uninstall it:

```bash
---

- hosts: all
  become: true
  tasks:
  - name: uninstall apache2 package
    apt:
      name: apache2
      state: absent
```

#### When 

The when attribute in Ansible is used to control whether a task runs or is skipped based on a condition. Simply put, it allows you to tell Ansible “run this task only if this condition is true.” This is important because environments are not always the same, and you often need different behavior depending on the operating system, variable values, host roles, or the result of previous tasks. Using `when` makes playbooks flexible, safe, and reusable, instead of hard-coding separate playbooks for each case.

A basic example is running a task only on Ubuntu systems:

```bash
- name: Install nginx on Ubuntu
  apt:
    name: nginx
    state: present
  when: ansible_distribution == "Ubuntu"
```
Here, the task runs only if the host is Ubuntu; on other systems, it is skipped.

```bash
- name: Install nginx on Debian and CentOS
  hosts: all
  become: true
  tasks:

    - name: Install nginx on Debian/Ubuntu
      apt:
        name: nginx
        state: present
        update_cache: true
      when: ansible_os_family == "Debian"

    - name: Install nginx on CentOS/RHEL
      dnf:
        name: nginx
        state: present
      when: ansible_os_family == "RedHat"
```

Ansible gathers system facts at the start of the playbook, including the operating system family (`ansible_os_family`). When the playbook runs, Ansible evaluates each when condition per host. If the condition is true, the task runs; if not, the task is skipped. Debian-based systems execute the `apt` task, while CentOS/RHEL systems execute the `dnf` task. avoids writing separate playbooks for each distribution, prevents errors from running the wrong package manager, and keeps automation portable, clean, and safe across mixed environments.

#### Variables

If you have different Linux distributions and you want to handle them using variables instead of hard-coding `apt` or `dnf` in tasks, the idea is to abstract the difference into variables and let the playbook logic stay the same. This makes the playbook cleaner, reusable, and easier to extend when new distributions are added.

In `playbook` file
```bash
---

- hosts: all
  become: true
  tasks:
  - name: install apache and php
    package:
      name:
        - " {{ apache_package }}
        - " {{ php_package }}
      state: latest
      update_cache: yes
```

In `inventory file` we will define those variables
```bash
<server 1 Debian-based IP> apache_package=apache2 php_package=libapache2-mod-php
<server 1 Centos-based IP> apache_package=httpd php_package=php
```

So here, playbook uses inventory variables to abstract OS-specific package names while relying on the generic package module, allowing the same playbook to work across Debian and CentOS systems without conditional logic.

#### Targting nodes

What if we have many hosts with different OS and we want to install apache and php on them

Simply is to grouping them by its role like if it work as Web or DB 

IN `inventroy` file
```bash
[web]
<server 1 Debian-based IP> 
<server 1 Centos-based IP>

[db]
<server 2 Debian-based IP> 
<server 3 Debian-based IP>
```

In `playbook` file

```bash
---
- hosts: all
  become: true
  tasks:

    - name: Install system updates (CentOS)
      dnf:
        update_only: yes
        update_cache: yes
      when: ansible_distribution == "CentOS"

    - name: Install system updates (Ubuntu)
      apt:
        upgrade: dist
        update_cache: yes
      when: ansible_distribution == "Ubuntu"

    - name: Install Apache and PHP on Ubuntu servers
      apt:
        name:
          - apache2
          - libapache2-mod-php
        state: present
      when: ansible_distribution == "Ubuntu"

    - name: Install Apache and PHP on CentOS servers
      dnf:
        name:
          - httpd
          - php
        state: present
      when: ansible_distribution == "CentOS"
```
This playbook targets all hosts and uses the when condition with Ansible facts to execute OS-specific package management tasks, ensuring the correct package manager and packages are used for each distribution.

The play runs on every server in the inventory, each task runs only on the matching OS, and Tasks that don’t match the OS are skipped automatically.


