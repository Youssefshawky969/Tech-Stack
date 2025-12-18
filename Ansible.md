## SSH 

## Git

### Overview

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

## Modules

Ansible modules are the building blocks of automation. Each module performs one specific action (install a package, manage a service, copy a file, create a user, run a command). In a playbook, every task calls exactly one module with parameters that describe the desired state. Ansible then ensures the system matches that state in an idempotent way (safe to run repeatedly).

How we use module?

A module is used inside a task with this general pattern:

```bash
- name: Human-readable task description
  module_name:
    parameter1: value
    parameter2: value
```

You choose the module based on what you want to manage, then set parameters (often including `state`) to describe the end result. Ansible handles SSH, execution, and change detection.

Common modules with examples:

- Package management
  ```bash
  - name: Install nginx
  package:
    name: nginx
    state: present
  ```
(`package` auto-selects apt/dnf/yum based on OS.)
  
- Service management
  ```bash
  - name: Ensure nginx is running
  service:
    name: nginx
    state: started
    enabled: true
  ```
- File management
  ```bash
  - name: Create directory
  file:
    path: /opt/app
    state: directory
    mode: "0755"
  ```
- Copy files
  ```bash
  - name: Copy config
  copy:
    src: files/app.conf
    dest: /etc/app.conf
  ```

Ansible’s documentation is the authoritative source for all modules and collections. 

- Go to docs.ansible.com → Ansible Collections / Module Index.

- Search by keyword (e.g., package, k8s, ios).

- Open a module page to see parameters, examples, return values, and notes.

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

### State

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

### When 

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

### Variables

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

In `inventroy` file
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

### Tags

Ansible tags are used to label tasks (or plays) so you can run or skip specific parts of a playbook without executing everything. They are especially useful in large playbooks like the example mentioned before, where you have multiple OS-specific tasks (CentOS vs Ubuntu) and different responsibilities (updates vs package installation).

```bash

---
- hosts: all
  become: true
  tasks:

    - name: Install system updates (CentOS)
      tags: always
      dnf:
        update_only: yes
        update_cache: yes
      when: ansible_distribution == "CentOS"

    - name: Install system updates (Ubuntu)
      tags: always
      apt:
        upgrade: dist
        update_cache: yes
      when: ansible_distribution == "Ubuntu"


host: web_server
become: true
tasks
    - name: Install Apache and PHP on Ubuntu servers
      tags: apache,apache2,ubuntu
      apt:
        name:
          - apache2
          - libapache2-mod-php
        state: present
      when: ansible_distribution == "Ubuntu"

    - name: Install Apache and PHP on CentOS servers
      tags: apache,centos,httpd
      dnf:
        name:
          - httpd
          - php
        state: present
      when: ansible_distribution == "CentOS"
host: db_server
become: true
tasks:
    - name: install maraia db package (Centos
      tags: centos,db,maraidb
      dnf:
        name: mariadb
        state: latest
      when: ansible_distribution == "CentOS"

    - name: install maraia db package (Ubuntu)
      tags: ubuntu,db,maraidb
      dnf:
        name: mariadb-server
        state: latest
      when: ansible_distribution == "Ubuntu"


```

This playbook is organized into multiple plays and uses tags to give you fine-grained control over what runs and when, especially in a mixed environment with web servers, database servers, and different Linux distributions.

### Managing file

Managing files in Ansible means creating, copying, modifying, templating, fetching, and deleting files or directories on managed nodes in a declarative and idempotent way. Below are the most common file-related modules, why we use them, and clear examples you can directly relate to real DevOps work.

1- Use `file` when you want to control the existence or attributes of a file or directory.

- Create a directory
  
```bash
- name: Create app directory
  file:
    path: /opt/myapp
    state: directory
    owner: appuser
    group: appuser
    mode: "0755"
```

- Create an empty file

  ```bash
  - name: Create log file
  file:
    path: /var/log/myapp.log
    state: touch
  ```

- Delete a file or directory
  ```bash
  - name: Remove old config
  file:
    path: /etc/myapp.conf
    state: absent
  ```

 2- Use `copy` to push static files. 

 ```bash
- name: Copy application config
  copy:
    src: files/app.conf
    dest: /etc/myapp/app.conf
    owner: root
    group: root
    mode: "0644"
  ```

3- Use fetch for backups and audits.

```bash
- name: Fetch Apache config
  fetch:
    src: /etc/httpd/conf/httpd.conf
    dest: ./backups/
```

4- Unarchive files

```bash
- name: Extract app archive
  unarchive:
    src: /opt/app.tar.gz
    dest: /opt/myapp
    remote_src: yes
```

### Adding users and bootstrapping

Adding users and bootstrapping in Ansible is about preparing a fresh server so it’s ready for automation and day-to-day operations. Bootstrapping usually includes creating users, setting SSH access, configuring sudo, and locking down root access. Below is a clear, practical explanation with examples you can reuse.

- Create a normal user
  ```bash
  - name: Create ansible user
  user:
    name: ansible
    shell: /bin/bash
    groups: sudo
    append: yes
    state: present
  ```

- Managing SSH keys
  ```bash
  - name: Add SSH key for ansible user
  authorized_key:
    user: ansible
    key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
  ```
This used to enable passwordless SSH (best practice)

- Grant sudo access (passwordless)
  ```bash
  - name: Allow ansible user passwordless sudo
  copy:
    dest: /etc/sudoers.d/ansible
    content: "ansible ALL=(ALL) NOPASSWD:ALL"
    mode: "0440"
  ```


## Role

An Ansible role is a standardized, reusable structure for organizing automation content such as tasks, variables, handlers, templates, and files. Instead of placing everything in one large playbook, a role breaks automation into logical components (for example: web, db, security). This makes playbooks cleaner, easier to maintain, and easier to reuse across different projects and environments. Roles are the recommended way to manage production-grade Ansible automation.

A role follows a fixed directory layout that Ansible understands automatically. The most common directories are `tasks/` (main automation logic), `handlers/` (actions triggered by changes, such as service restarts), `vars/` and `defaults/` (variables), `templates/` (Jinja2 templates), and `files/` (static files). This structure allows Ansible to load everything automatically without extra configuration.

The implementation flow starts by identifying a responsibility, such as “configure a web server.” Next, you create the role structure using ansible-galaxy init <role_name>, or manually at this sturcure `/roles/web-server/tasks/main.yml` then repeat this strucure for all group or tasks you have

If you make it by first way i mentioned, then you write tasks in tasks/main.yml, define variables in defaults/main.yml, add templates or files if needed, and create handlers for service reloads. After the role is ready, you attach it to a playbook using the roles keyword and target the appropriate hosts. When the playbook runs, Ansible automatically executes the role in the correct order.

```bash
roles/
└── web/
    ├── tasks/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml
    ├── defaults/
    │   └── main.yml
    ├── templates/
    │   └── apache.conf.j2
    └── files/
```

You then mention the role in the playbook file:

```bash
---
- name: Configure Web Servers
  hosts: web
  become: true
  roles:
    - web
```
That is mean run everything defined in the web role on the web hosts.

Very easy and strightfarward.

Thnaks for reading.





