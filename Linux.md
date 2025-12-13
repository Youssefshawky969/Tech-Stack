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



## Inode and Inode Numbers

An inode (index node) is a data structure used by the Linux filesystem to store metadata about a file or directory.
It does not store the file name or the actual file data. Instead, it stores information about the file.

Each file, directory, or special object on a Linux filesystem has an inode.

An inode contains important metadata, such as:

- File type (file, directory, link, device, etc.)

- Owner (UID)

- Group (GID)

- Permissions (read, write, execute)

- File size

- Timestamps:

   - Created time

   - Modified time

   - Access time

- Number of links (hard links)

Pointers to data blocks (where the content is stored on disk)

In short:

An inode knows everything about a file except its name and actual data.

Each inode has a unique inode number within the filesystem.
This number acts like the “ID” of the file.

- The inode number points to the inode.

- The file name links to the inode number.

- Hard links use the same inode number.

- Multiple filenames can point to the same inode.

- The file data is removed only when all hard links are deleted.

Example:
` ln file1 file2`
Now `file1` and `file2` share the same inode number.

You can check the inode number using the `ls` command:
`ls -li`

Output example:
`12345 -rw-r--r-- 1 user user 1024 Feb 10 10:00 file.txt`
`12345` is the inode number.

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

#### Display content of the file into screen

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
The `mv` command in Linux is used to move or rename files and directories. It can transfer a file from one location to another, or change the file name in the same location.
` mv [options] source target`

- source: the file or directory you want to move or rename
- target: the destination path or the new name

1- move files:

To move a file from one directory to another 
` mv file.txt /home/user/Documents/`
This command moves file.txt into the Documents directory.

2- Rename a File:

To rename a file in the same directory
`mv oldname.txt newname.txt`

3- Move a Directory

`mv myfolder /home/user/Projects/`

options used with this command
`-i` : Interactive mode (asks before overwriting)
`f` : Force move (overwrite without prompt)
`-v` : Verbose output (shows what is happening)



##### remove files/direcotries

The `rm` command in Linux is used to delete files and directories. When you remove something with `rm`, it does not go to the trash — it is permanently deleted.
Basic Syntax:
`rm [options] file`

1- Remove file

To delete a file
`rm file`
This permanently removes file.txt.

2- Remove Multiple Files

`rm file1.txt file2.txt file3.txt`

3- delete directories

By default, `rm` does not remove directories unless you use options.

`rm -r directory` 
-r (recursive) removes the directory and everything inside it.

`rmdir directory` remove empty dirs

> [!WARNING]
> Use `rm -rf` carefully. Running it on the wrong path can delete critical system files or your entire filesystem.

#### creating file
you can create files by differnet ways
first one you can use `touch file` or if you want to create multiple files at ones `touch file1 file2 FILE3` it is case senstive so take care.
second way is to specify the path ` touch /home/youssef/code.py`


#### grep Command (Search for Text Patterns)
The grep command is used to search for specific text patterns inside files or command outputs. It supports regular expressions, which makes it powerful for filtering and finding matching lines.

The name grep comes from the ed text editor command:

"globally search a regular expression and print."

Basic Syntax:
`grep [options] pattern file`

- pattern: text or regular expression to search for
- file: file(s) to search in

1- Search for a Word in a File

`grep "error" logfile.txt`
This prints all lines containing the word error.

2- Case-Insensitive Search

`grep -i "error" logfile.txt`
The `-i` option ignores upper/lower case.

3- Search in Multiple Files

`grep "error" *.log`

4- Show Line Numbers

`grep -n "error" logfile.txt`
`-n` prints the line number with each match.

5- Count Matches

`grep -c "error" logfile.txt`
`-c` shows how many lines match the pattern.

6- Search Recursively in Directories

`grep -r "error" /var/log`
`-r` (recursive) searches all files inside directories.

7- Search Command Output with Pipes

`ps aux | grep nginx`
This searches for nginx in running processes.


#### Input and Output Redirection in Linux

In Linux, commands normally take input from the keyboard (stdin) and display output on the screen (stdout).
With redirection, you can change this behavior to read input from files and write output to files or other commands.

Linux uses three standard streams:

stdin:   - Standard Input
         - Input to a program (keyboard)
         - File Descriptor (0)

stdout:  - standard output
         - Normal output (screen)
         - File Descriptor (1)

stderr:  - Standard Error
         - Error messages
         - File Descriptor (2)


1- Redirecting Output (`>` and `>>`)

`>` — Overwrite Output to a File.
Redirect command output to a file, replacing its contents:
`
ls > output.txt
`
- Creates output.txt if it doesn’t exist.
- Overwrites the file if it exists.

2- `>>` — Append Output to a File

Append output to an existing file:
`echo "New line" >> output.txt`

- Adds to the bottom without deleting existing content.

2- Redirecting Input (`<`)

`<` — Use File as Command Input

Instead of typing input manually, read it from a file:
`sort < names.txt`

- Reads names from names.txt and sorts them.


3- Redirecting Errors (`2>` and `2>>`)

`>` — Store Errors

Redirect error messages to a file:
`grep "error" file.txt 2> errors.log`

`2>>` — Append Errors

Append error messages:
`grep "error" file.txt 2>> errors.log`

Combine stdout and stderr into one file:
`command > output.log 2>&1`

#### Piping in Linux

In Linux, a pipe (`|`) is used to connect the output of one command to the input of another command.
This allows you to build powerful command chains without creating temporary files.

A pipe works with standard streams as we said before.

- It takes stdout (standard output) from the left command

- And feeds it into stdin (standard input) of the right command

  Basic syntx:
  `command1 | command2`
- `command1`: produces output

- `command2`: processes that output

Example:

`ls | sort`
`ls` shows filenames while `sort` sorts them alphabetically.

More examples:

1- Count the Number of `.txt` Files
`ls *.txt | wc -l`
`ls` list .txt files and `wc -l` stands for "word count" used to count lines, in our example it uses to count number of files

2- Find Running Process
`ps aux | grep nginx`

`ps aux` list processes and `grep nginx` filter results


#### Text Editors in Linux (Vim and Nano)

When working in Linux, especially on servers and CLI environments, you often need to create or edit text files (config files, scripts, code, logs). Two popular terminal-based text editors are Vim and Nano.

They serve the same purpose but are designed for different user experiences.

##### 1. Nano Editor

Nano is a simple, user-friendly text editor ideal for beginners.
It is easy to learn, shows shortcuts at the bottom of the screen, and works like a normal text editor.

`nano filename.txt
`
If the file doesn’t exist, Nano will create it.

Common Shortcuts:
Shortcuts use Ctrl (represented as ^ in the menu):

- save file: Ctrl + O
- Exit: Ctrl + X
- Search text: Ctrl + W
- Cut line: Ctrl + K
- paste: Ctrl + U

  Nano shows help and shortcuts at the bottom, making it very beginner-friendly.

##### 2. Vim Editor
Vim (Vi Improved) is a powerful, feature-rich editor designed for advanced users.
It gives high control for editing, searching, macros, automation, and programming.
It works in different modes (the main difference from Nano).

`vim filename.txt
`

Vim Modes (Important):

Normal Mode: Navigate, delete, copy text to Return to Normal Mode `Esc`
Insert Mode: Type text normally, Enter Insert Mode `i`
Command Mode: Run commands (`:w`, `:q`, etc.)

Common commands:

Save: `:w`

Quit: `:q`

Save and Quit: `:wq`

Force quit: `:!q`

Move up/down: `k`/`j`

Move left/right: `h`/`l`

Go to top line: `gg`

got to bottom: `G`

delete word: `dw`

copy line: `yy`

paste line: `p`

undo: `u`

#### User and Group Management in Linux

Linux is a multi-user operating system, meaning multiple users can share the same system with different permissions. To manage access control, Linux uses UIDs and GIDs, along with tools to manage users, groups, and privileges.

1- User Identifier (UID)

A User Identifier (UID) is a unique number assigned to each user on a Linux system.

- root (superuser) = 0
- System/service accounts = 1-999
- Normal user accounts = 1000+

You can check your UID using:

`id -u
`

The file /etc/passwd stores user information. Example entry:

`mohamed:x:1001:1001::/home/mohamed:/bin/bash
`

- 1001 = UID
- 1001 = Primary GID

2- Group Identifier (GID)

A Group Identifier (GID) is similar to UID but for groups. Groups allow you to assign permissions to multiple users at once.

Group information is stored in `/etc/group`.

Example:

`id
`

`developers:x:2000:mohamed,ahmed`

- 2000 = GID
- members = mohamed, ahmed

3- Gaining Superuser Privileges

The superuser (root) has full control over the system. There are two main ways to get root privileges.

- Using `sudo`

  Runs a single command as root.

  `sudo command`
  
  or
  
  To start a root shell:

  `sudo -i`

- Switching to root user
  
  If you know the root password

  `su - `

  4- Changing Passwords

  - Change your own password
 
    `passwd`

  - Change another user's password (requires root)

    `sudo passwd username`

5- Creating Users

- Create a new user

  `sudo useradd username`

- Create a user and generate a home directory automatically

   `sudo useradd -m username`

6- Modifying Users

- Add user to a group

  `sudo usermod -aG groupname username`

7- Creating Groups `<developers>`

`sudo groupadd developers`

>[!tip]
> Important System Files:
>
>`/etc/passwd` for Stores user information (UID, home directory, shell)
>
>`/etc/shadow` for Stores encrypted passwords
>
>`/etc/group` for Stores group info


### Controlling Access to Files in Linux

Linux controls access to files and directories using a permission and ownership model. This ensures system security by defining who can read, write, or execute a file or directory.

1-  File Ownership

  Every file and directory in Linux has:

   -   User (Owner) – the file creator or assigned owner

   -   Group – a group of users with shared access

   -   Others – all other users on the system

You can view ownership using

` ls -l`

It will return somthing like this

` -rw-r----- 1 mohamed developers 1024 file.txt
`

- Owner: mohamed

- Group: developers

2- File Permissions

Permissions define what actions are allowed.

Permission Types:
`r` for read

`w` for write

`x` for excute

Permission Structure:

`-rwxr-x---
`

`-` for file type 
`rwx` Owner permissions
`r-x` Group permissions
`---` Others permissions

We have two different way to grant permission to user or group 

1- Symbolic Mode

 ` chmod u+x file.sh
    chmod g-w file.txt
    chmod o=r file.txt`

- `u` user , `g` group `o` others, `a` all

2- Numeric Mode (Octal)

`chmod 755 script.sh
`
000 = 0

001 = 1

010 = 2

011 = 3

100 = 4

101 = 5

110 = 6

111 = 7

For file structure every `1` means active and `0` means disactive.

So `000` mean `---------` no permission for owners, no permission for groups, no permission for others.

For `755`  means `rwx` for owner because it represent as `111` in octet, `r-x` for group because it represent as `101` and same for others 

so Whether the group membars of the owner of the file or others can only read and excute the file, and only the owner have the full permission.


3- Changing Ownership (`chown` and `chgrp`)

- Change owner

  ` sudo chown user file.txt`

- Change group

    ` sudo chgrp developers file.txt`

- Change owner and group together

    ` sudo chown user:developers file.txt`

    same concept in directory permission

    ` chmod 755 /project`

  4- Special Permissions (Advanced)

  Program runs with owner's privileges.

  `chmod u+s program`

  Files inherit group ownership.
  
  `chmod g+s directory`

  
