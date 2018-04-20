# Team Development - Git Repository Operation

## Table of contents

1. [第一步](#first-step) First Step
1. [在命令行下的协同示例](#general-progress) General Progress
1. [请求合并](#pull-request) Pull Request
1. [从上游拉取](#merge-upstream) Merge Upsteam
1. 用Eclipse代替命令方式
1. 用Idea代理命令方式

## 警告

如果git操作中发生状况, 千万不要盲目地删除, 要及时去求助

## First Step

### Login then going to project upstream

For example __dev/ctf-java__

![屏幕快照 2018-04-20 上午11.59.45.png](./屏幕快照%202018-04-20%20上午11.59.45.png)

### Fork

For example in __gogs__ , 点击 _派生_ 按钮

![屏幕快照 2018-04-20 下午12.05.55.png](屏幕快照%202018-04-20%20下午12.05.55.png)

## General Progress

### Clone

For example in __Mac__ CLI
```
fanhonglingdeMacBook-Pro:stackdocker fanhongling$ git clone http://172.17.4.59:10080/demo/ctf-java ctf-java
Cloning into 'ctf-java'...
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (4/4), done.
Checking connectivity... done.
```

### Commit works during moving ahead

实现了每一个功能点 (Feature)要commit

Status
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	docs/

nothing added to commit but untracked files present (use "git add" to track)
```

Add, 把全部工作都加入作为一个feature 
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git add --all
```

__如果有些内容是属于另一个feature, 则不用--all命令选项, 而是逐个文件, 或逐个目录操作__


Commit, 简要说明这个Feature
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git commit -m "init beginner reqirement of git skill"
[master 8a5f997] init beginner reqirement of git skill
 3 files changed, 35 insertions(+)
 create mode 100644 docs/beginner-team-development.md
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\212\345\215\21011.59.45.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\21012.05.55.png"
```

Commit once again after another feature done
 

### Commit more in working day

For example, the feature modified
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   docs/beginner-team-development.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Update
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git add docs/beginner-team-development.md
```

Commit updation
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git commit -m "update beginner requirements: commit rules"
[master 994d29f] update beginner requirements: commit rules
 1 file changed, 50 insertions(+), 2 deletions(-)
```

### Push at least one time before working off

今天，你完成了一个Feature (test OK)， 并进行了另一个Feature
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   docs/beginner-team-development.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	docs/control-project-upstream.md

no changes added to commit (use "git add" and/or "git commit -a")
```

因此， 同上， 对2个features分别commit
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git add docs/beginner-team-development.md
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git commit -m "feature 1 ..."
[master 8c4c880] feature 1 ...
 1 file changed, 28 insertions(+), 2 deletions(-)
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git add docs/control-project-upstream.md
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git commit -m "begin feature 2..."
[master 37d7bc9] begin feature 2...
 1 file changed, 79 insertions(+)
 create mode 100644 docs/control-project-upstream.md
```

然后先把今天全部的工作push到remote. 一般全部工作commit在本地的master分支
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git branch
* master
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

Counting objects: 18, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (18/18), 349.06 KiB | 0 bytes/s, done.
Total 18 (delta 8), reused 0 (delta 0)
To http://demo:demo@172.17.4.59:10080/demo/ctf-java
   1adf3ff..37d7bc9  master -> master
```

通过检查最近n个commits (示例3个)，去checkout今天的实际工作量
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git log -3
commit 37d7bc9e0f143a26fe826b98888d0f2444f04a75
Author: tangfeixiong <tangfx128@gmail.com>
Date:   Fri Apr 20 13:32:17 2018 -0700

    begin feature 2...

commit 8c4c88065494e8675741ea9894b27079aaa06ced
Author: tangfeixiong <tangfx128@gmail.com>
Date:   Fri Apr 20 13:31:17 2018 -0700

    feature 1 ...

commit 994d29fa1da3e52e7609be45cac6d2b82acbbcb0
Author: tangfeixiong <tangfx128@gmail.com>
Date:   Fri Apr 20 12:50:11 2018 -0700

    update beginner requirements: commit rules
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git checkout -b patch 8c4c88065494e8675741ea9894b27079aaa06ced
M	docs/beginner-team-development.md
Switched to a new branch 'patch'
```

查看当前所在分支 (换成了patch)
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git branch
  master
* patch
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git log -1
commit 8c4c88065494e8675741ea9894b27079aaa06ced
Author: tangfeixiong <tangfx128@gmail.com>
Date:   Fri Apr 20 13:31:17 2018 -0700

    feature 1 ...
```

把新的patch分支push到remote
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git push http://demo:demo@172.17.4.59:10080/demo/ctf-java
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

Total 0 (delta 0), reused 0 (delta 0)
To http://demo:demo@172.17.4.59:10080/demo/ctf-java
 * [new branch]      patch -> patch
```

回到本地的master以备继续
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git checkout master
M	docs/beginner-team-development.md
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 4 commits.
  (use "git push" to publish your local commits)
```

## Pull Request

Go to upstream repository, e.g. __dev/ctf-java__
![屏幕快照 2018-04-20 下午2.01.57.png](屏幕快照%202018-04-20%20下午2.01.57.png)

Select branch to pull request, E.G. __patch__
![屏幕快照 2018-04-20 下午2.04.43.png](./屏幕快照%202018-04-20%20下午2.04.43.png)

如果上游(upstream)没有任何动作，那么这个请求一直留着
![屏幕快照 2018-04-20 下午2.13.26.png](./屏幕快照%202018-04-20%20下午2.13.26.png)

## Merge Upstream

一个Team, 每一个成员，无论是否负责合并， 都在自己的remote repository完成相同的操作

而项目仓库是用来归档的，不是属于个人的。

一般地， 第二天上班后， 首先要检查昨天的pull request有否被合并。

如果合并了， 你要pull上游的更新， 以获取其余成员的最近提交

每个人的远程仓库名默认是origin
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git remote -v
origin	http://172.17.4.59:10080/demo/ctf-java (fetch)
origin	http://172.17.4.59:10080/demo/ctf-java (push)
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ cat .git/config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = http://172.17.4.59:10080/demo/ctf-java
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

添加项目仓库为upstream
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git remote add upstream http://172.17.4.59:10080/dev/ctf-java
```

```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git remote -v
origin	http://172.17.4.59:10080/demo/ctf-java (fetch)
origin	http://172.17.4.59:10080/demo/ctf-java (push)
upstream	http://172.17.4.59:10080/dev/ctf-java (fetch)
upstream	http://172.17.4.59:10080/dev/ctf-java (push)
```

然后将upstream的master合并到本地的master
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git pull upstream master
From http://172.17.4.59:10080/dev/ctf-java
 * branch            master     -> FETCH_HEAD
Updating 1adf3ff..7bbfb02
Fast-forward
 docs/beginner-team-development.md                                                              | 347 +++++++++++++++++++++++++++++++++++++++++++++++
 docs/control-project-upstream.md                                                               |  90 ++++++++++++
 ...61\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\212\345\215\21011.59.45.png" | Bin 0 -> 259278 bytes
 ...61\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\21012.05.55.png" | Bin 0 -> 183910 bytes
 ...261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.01.57.png" | Bin 0 -> 171782 bytes
 ...261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.04.43.png" | Bin 0 -> 215085 bytes
 ...261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.13.26.png" | Bin 0 -> 284171 bytes
 ...261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.19.02.png" | Bin 0 -> 150362 bytes
 ...261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.25.54.png" | Bin 0 -> 300128 bytes
 9 files changed, 437 insertions(+)
 create mode 100644 docs/beginner-team-development.md
 create mode 100644 docs/control-project-upstream.md
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\212\345\215\21011.59.45.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\21012.05.55.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.01.57.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.04.43.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.13.26.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.19.02.png"
 create mode 100644 "docs/\345\261\217\345\271\225\345\277\253\347\205\247 2018-04-20 \344\270\213\345\215\2102.25.54.png"
```

如果觉得有必要, 可以让你个人的远程仓库也到最近的合并点: `git push`

否则继续你的工作

## Others

### Help 

For example
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git --help
```

Or
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git help --all
```

To a specified command, for example _push_
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git push --help
```
使用q键退出文档帮助工具

### Issue

1. RPC failed; result=22, HTTP code = 403

For example
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git push
Counting objects: 18, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (18/18), 349.06 KiB | 0 bytes/s, done.
Total 18 (delta 8), reused 0 (delta 0)
error: RPC failed; result=22, HTTP code = 403
fatal: The remote end hung up unexpectedly
fatal: The remote end hung up unexpectedly
Everything up-to-date
```

Gogs
```
fanhonglingdeMacBook-Pro:ctf-java fanhongling$ git push http://demo:demo@172.17.4.59:10080/demo/ctf-java
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

Counting objects: 18, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (18/18), 349.06 KiB | 0 bytes/s, done.
Total 18 (delta 8), reused 0 (delta 0)
To http://demo:demo@172.17.4.59:10080/demo/ctf-java
   1adf3ff..37d7bc9  master -> master
```