distupgrade
===========

Python script that simplifies the apt-get update / review / apt-get dist-upgrade process

Why?
----
I use a Debian system with [pinning](http://jaqque.sbih.org/kplug/apt-pinning.html).
Usually, I the following to upgrade my system:

```
$ apt-get update
$ apt-get dist-upgrade -s
$ # painfull review to see what package gets pulled from where (testing, sid, experimental)
$ apt-get dist-upgrade
```

`dist-upgrade.py` simplifies the whole process. It runs `apt-get update`, then lists then
number of updates per repository and interactively ask to install them. Usually, this is
enough and I hit enter to install the updates. `dist-upgrade.py` allows to review the list
of upgrades in a pager (yeah), and then asks again to install the updates.

A typical session
-----------------
```
dist-upgrade.py -u

[lots of text]
Get:168 http://ftp.at.debian.org experimental/main 2014-07-10-1457.04.pdiff [1,657 B]
Fetched 1,560 kB in 16s (94.7 kB/s)
Reading package lists... Done

Debian:testing: 83
Install upgrades? [Y/n/l] l
Debian:testing:
 Inst autoconf [2.69-6] (2.69-7 Debian:testing [all])
 Inst cups-filters [1.0.54-3] (1.0.54-3+b1 Debian:testing [amd64])
 [lots of text, but scrollable in a pager]
 Inst uno-libs3 [4.2.5-1] (4.2.5-1+b1 Debian:testing [amd64]) [ure:amd64 ]
 Inst ure [4.2.5-1] (4.2.5-1+b1 Debian:testing [amd64]) []
 Inst vim-youcompleteme [0+20140207+git18be5c2-1+b1] (0+20140207+git18be5c2-1+b2 Debian:testing [amd64])
(END) q
Install upgrades? [Y/n/l] <enter>
[lots of text]
Setting up vim-youcompleteme (0+20140207+git18be5c2-1+b2) ...
Processing triggers for libc-bin (2.19-4) ...
Processing triggers for menu (2.1.47) ...
```

The whole procedure took 3 keystrokes: `l,q,<enter>`

Synopsis
--------
```
usage: dist-upgrade.py [-h] [-u] [-f]

List dist-upgrades by repo and interactively confirm that upgrades should by
applied

optional arguments:
  -h, --help    show this help message and exit
  -u, --update  Execute apt-get update first
  -f, --force   Force dist-upgrade without printing upgrades
```
