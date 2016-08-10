# sora
A bite-sized server monitoring framework

## Install and run the server agent

- Get dependencies for your platform

On Debian: `apt-get install build-essential`

On RedHat / CentOS: 
```
yum -y groupinstall 'Development Tools'
rpm -iUvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
yum -y update
yum -y install python-pip python-devel
```

- Get python dependencies
`pip install -r requirements.txt` 
(virtualenv recommended)

- Run the server agent
`./sora`
> Running on $IP:1337

## Usage

- Get a list of running processes on your server
`curl $IP:1337/ps`

> JSON output

```
"42": {
        "cmdline": "/bin/bash", 
        "environment": null, 
        "name": "bash", 
        "ppid": 1
    }
```

(note that the `sora` agent process will *not* be shown in the process list)
