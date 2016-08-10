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

> expected output (json)

```
"16726": {
        "cmdline": "/mnt/shared/sbin/dropbear -i -s -m -d /mnt/shared/etc/dropbear/dropbear_dss_host_key -r /mnt/shared/etc/dropbear/dropbear_rsa_host_key", 
        "environment": null, 
        "name": "dropbear", 
        "ppid": 1
    }
```
