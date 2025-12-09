Hello everyone, in this document I will introduce Linux, explain how it works, describe its architecture, explore the network types used in virtual environments, and cover additional important concepts. The goal is to provide a clear and practical understanding of Linux from both a structural and operational perspective.

## Linux Architecture

The hardware is the core of the system and the main component that executes physical operations. However, to control the hardware and perform actions, we need software capable of issuing instructions. This is the role of the kernel. The kernel is responsible for managing and interacting directly with the hardware.

Since communicating with the kernel requires deep technical knowledge and is not user-friendly, we use a higher-level interface. This interface is the shell. The shell acts as a translator between the user and the kernel. It receives user commands, converts them into a form the kernel understands, and ensures they are executed on the hardware.

In simple terms:

Hardware performs the actual work.

Kernel communicates with the hardware.

Shell communicates with the kernel on behalf of the user.

<img width="516" height="478" alt="image" src="https://github.com/user-attachments/assets/6a12e8a5-fe63-4ce7-8cc4-5cdc01b79dd7" />


## VM Network Configuration Modes

When configuring virtual machines, there are three common network modes: Bridged, NAT, and Host-Only. Each mode determines how the VM connects to the host, other VMs, and external networks.

### 1. Bridged Mode

In Bridged Mode, the VM is connected to the physical network through a virtual bridge.

A virtual switch is created between the host and the VMs.

Each VM receives an IP address from the same subnet as the host machine.

VMs can communicate with each other and with other devices on the local network.

Internet access is direct, using the VM’s own network identity on the local network.

This mode makes the VM appear as a separate machine on the same network as the host.

### 2. NAT (Network Address Translation) Mode

In NAT Mode, the VM is placed behind a virtual NAT device managed by the hypervisor.

A virtual switch is created, but the VMs are assigned an IP address from a different internal subnet (not the host’s subnet).

VMs can communicate with each other inside the virtual network.

When accessing the internet, traffic is translated using the host’s IP address through the virtual NAT.

External devices cannot directly reach the VMs unless port forwarding is configured.

This mode provides internet access while isolating the VMs from the external network.

### 3. Host-Only Mode

In Host-Only Mode, the VM network is isolated from external networks.

A private virtual network is created between the host and the VMs only.

VMs can communicate with each other and with the host.

No internet access is provided unless additional routing is configured.

This mode is useful for test environments, labs, or isolated systems where no external connectivity is required.

<img width="1381" height="595" alt="image" src="https://github.com/user-attachments/assets/3a42300f-b81a-44eb-a4dc-d95b6fdbc2e2" />



## What is Command Line or CLI
The Command Line Interface (CLI) is a method for interacting with the operating system by typing text-based commands. When a user enters a command using the CLI, the shell processes it and passes the instruction to the kernel, which then performs the requested operation on the hardware.

In simple terms, the CLI allows users to communicate with the system through the shell, which acts as the interface between the user and the kernel.

## What is Bash Shell
Bash (Bourne Again SHell) is the default shell used on most Linux distributions. It interprets user commands, executes programs, manages scripts, and provides features like command history, variables, piping, and automation.

Bash is the most widely used shell in Linux environments and is commonly used for system administration, scripting, and automating tasks.


## Understanding the Shell Prompt
The shell prompt is the text displayed in the terminal that shows the current state of your session and indicates that the system is ready to receive commands. The prompt usually contains useful information such as the current user, hostname, and working directory.


A common Linux shell prompt looks like this:
`user@hostname:~$
`
The symbol `~` (tilde) indicates that the current working directory is the home directory of the logged-in user.
For example:

If the user is youssef, `~` refers to /home/youssef.

For the root user, `~` refers to /root.

The character at the end of the prompt tells you the user privilege level:

`$` indicates a regular (non-privileged) user.

`#` indicates the root user (superuser), who has full system privileges.

This visual indicator helps you avoid running privileged commands unintentionally.

## Understanding command syntax

The command consist of 3 things Command, Option(s), Argument(s)

Example:

`usermod -L user01`
this mean `usermod` is the command, `-L` which is the option that mean lock, `user01` which is the user which will lock it so the full meaning of the syntax is to lock the password of the `user01`

`ls -l /dev`
this mean `ls` is to list `-l` means long list and `/dev` is the directory which we want to list its content

## The File System Hierarchy
- /usr: installed software, shared libraries, include files and read-only program data, important subdirectoreis like:
   - /usr/bin: user commands
   - /usr/sbin: system admin commands
   - /usr/local: localy customized softwrare
 
- /etc: configuration files spaecfic to this system
- /var: variable data specfic to that system that should persist between boots. Files that dynnamicaly change such as: databases, cache dirctories, log files and website content may be found under `/var`
- /home: home directories where the users stored thier personal data and configuration files
- /root: home directory related to the super user
- /tmp: a world-writable space for temporary files
- /boot: files that neede in order to start the boot process
- /dev: contain special device files that are used by the system to access hardware.\
   

<img width="1176" height="479" alt="image" src="https://github.com/user-attachments/assets/dba7597d-f117-4c13-b5fa-a2d954271963" />

## File Types

<img width="1124" height="461" alt="image" src="https://github.com/user-attachments/assets/07dec5d1-0ea7-4669-b432-d348c69b33fe" />

` ls -l`

<img width="1016" height="393" alt="image" src="https://github.com/user-attachments/assets/5112bb18-1188-4a54-a48e-38d3f61b9a18" />

## Rules for Naming in linux

- It should be descriptive and only alphanumric characters UPPERCASE, lowercase, numbers,sympols 
- Also are case senstive and filename starting by `.` are hidden

  
## Basic commands

##### date command
`date` command is used to display the whole date like this:
`MON SEP 26 12:17:58 AM EET 2025`

if you need to print only the time only so you need to be spacefic in your option as well like this
`date +%R` it will display 
`1:23`

if you need only the date as a day month year `date +%X`
`12/09/2025`

##### passwd command 
`passwd` is used to change the password of the current user

##### file command
`file` is used to check the type of the file like `file /etc/passwd` 
it will display that `etc/passwd: ASCII text`

## Display content of the file into screen

##### cat command
if i typed `cat /etc/passwd` it will display the content of this file 
i can also display multiple contnet like `cat file1 file2` 

##### less command 
`less` command displays the content page by page and you can swape between pages by click space

##### head/tail command 
`head` display the first 10 lines of the file you can also modify the option by adding `-n` then the number of the lines you need to display like:
`head -n 5 file1` this means display the fist 5 lines of the file1 

`tail` is the same concept but it displays the last 10 lines and also you can modify the lines you need to display

##### History command
`history` used to list the last pervious commands used, it will return:
`
1 date
2 date +%R
3 cat /etc/passwd
`

- you can choose a spaecfic command again by `!` then the number of the command like 3 for example `!3` so it will return the `cat /etc/passwd`

- you can also write `!!` means point to the last command ran which is `cat /etc/passwd`
   
#### pwd command
`pwd` stands for print working directory, used to display the full path name of the current working directory of that shell.

For example:
`pwd`
`/home/youssef
#### cd command
`cd` stands for change directory used to change your shell's directory if you did not specify any argument

For example:
if you are at home direcotry and you want to go to youssef directory so
`cd /home/youssef` or `cd /youssef` or `cd` directly 

If you want to go back to the parent directory
`cd ..` will make one step back.

#### ls command
`ls` used for listing the content of the directory, it has multiple options.
`ls -l` for long listing.
`ls -a` for listing all files including the hidden files.
`ls -R` recursive, to include the contents of all subdirectories.
`ls -lh` for humen readable listing.
`ls -lt` for sorting by last time modified at the top.
`ls -ltr` same like `-lt` but with revers order which make the last modifeid at the bottom.


#### Line file mangment commands
when managing files, you need to be able to create, copy, remove, and move.

##### creating directory
`mkdir` used to make directories

##### copy files
`cp file new-file` for copying the content in the file.
`cp -r directory new-directory` copy directory and its content

##### move file
`mv file new-file`

##### remove files/direcotries
`rm file` for remove files
`rm -r directory` for remove directories
`rmdir directory` remove empty dirs


#### creating file
you can create files by differnet ways
first one you can use `touch file` or if you want to create multiple files at ones `touch file1 file2 FILE3` it is case senstive so take care.
second way is to specify the path ` touch /home/youssef/code.py`








