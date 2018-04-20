#  Project control for owner

## Open Project

For example, owner `dev` create an empty remote repository. note: _There has another way to accomplish it_
```
fanhonglingdeMacBook-Pro:tangfeixiong fanhongling$ git clone http://172.17.4.59:10080/dev/ctf-java ctf-java
Cloning into 'ctf-java'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
```

```
fanhonglingdeMacBook-Pro:tangfeixiong fanhongling$ cd ctf-java/
```

Create 2 files: _README.md_ and _.gitignore_
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

Initial project repository
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git add --all
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git commit -m "open project"
[master (root-commit) 1adf3ff] open project
 2 files changed, 16 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 367 bytes | 0 bytes/s, done.
Total 4 (delta 0), reused 0 (delta 0)
Username for 'http://172.17.4.59:10080': dev
Password for 'http://dev@172.17.4.59:10080': 
To http://172.17.4.59:10080/dev/ctf-java
 * [new branch]      master -> master
```

## Merge Requests

[接着beginner-team-development.md的合并请求](./beginner-team-development.md#pull-request)

上游仓库所有者需要处理pull requests
![屏幕快照 2018-04-20 下午2.19.02.png](屏幕快照%202018-04-20%20下午2.19.02.png)

选择bala bala， 检查有没有冲突
![屏幕快照 2018-04-20 下午2.25.54.png](./屏幕快照%202018-04-20%20下午2.25.54.png)

那么， 就点击合并按钮