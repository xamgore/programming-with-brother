## What is git and github?

**git** is a tool for comfortable programming of two or more guys (or ladies). They work on a project in the same folder, with the same files. The place where they work is named _repository_ or _repo_. That's just a folder with some magic: you can save your repo (all files) in any moment. Savings are named _commits_. You also can load a commit at any time and continue to write code.

> Our work will be following: I create hometasks (`commit`) → you solve them (`commit`) → I create (`commit`) → …

**github** is a website that keeps repositories. Actually you have your own _local_ repo, I have my _own_ repo, and we want to share it with each other. So we send (push) our repos to the github. And load repo (pull) from it.

 > Github will be our point of connection: I create hometask (`commit`) → send it to github (`push`) ⟹ you load it from github (`pull`) → solve tasks (`commit`) → send it to github (`push`) ⟹ I create…

 [Download git](https://git-scm.com/download/win) and call me in skype to install it properly.

## How to get tasks?

Open some folder, for example `C:\PABCWork.NET` or `C:\Users\mi\Documents\PABCWork.NET`.
In the address bar write `cmd` and press enter.

![address bar](http://i.imgur.com/0oPzMmO.png)

The terminal will be opened. If you don't have the _local_ repository, than you have to create it:

```
git init
git remote add github https://github.com/xamgore/programming-with-brother.git  
git pull github
```

If you want to download new tasks, then just run `git pull`.
This command will update your local repository (from github),
and as a consequence you will get new tasks.

## How to send my solution?

Register a [new account](https://github.com/join?source=header-home) and tell me your user name. I will add you to github repo, so you can send (push) changes.

For example, you have completed tasks and want to push the solution. To do that you need to open `cmd` and run:

1. `git add -A` — you want to add **All** files to commit
2. `git commit -m "Complete 1st task"` — to create a commit with the **message**
3. `git push` — send commit to github

It's better to write commit messages in english, but you may use russian as well.

If you don't understand something from here, you are welcome to ask me.
