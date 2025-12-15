## SSH 

## Git
### Intro

When we talk about tech company dealing with servers, code, new feature, and configuration everyday. Its important to have a centerlized repo or registry containiing the code andour configuration.
In this part of the series we will get in touch little bit with Git, not deep dive but only the core basics.

### Configure Git

First, if you do not have git you have to install it by checking `git --version`.
if it there so its okay, but if not try.
`
sudo apt update
sudo apt install git -y
`

Now, you need to login into github.com then create a new repo 
- go to your profile icon, then settings,
- hit the `SSH keys` tap
- click `New SSH key`
- Grap your publick key from your machine ` cat .ssh/id_225519.pub` we generated before
- Paste the key into the box then save
- Clone your repo then
- in your machine ` git clone <link provided>`

   so thats is good now you have cloned your repo in your machine

  if you list `ls` the expected output
  
  `
  README.md
  `
  for example, it may vary you may have more files in your repo.

  before we work in our file, we need to tell git first who we are.
  
  `git config --global user.name "youssef shawky"
  git config --global user.email "yshawky@gmail.com"
  `
   
you can edit your file by

`nano README.md` 

edit what you need then commit the changes by

`
git status
git add README.md
git commit -m "updated README.md file"
git push origin master
`


That's it, very simple :) 
Thanks for reading.

