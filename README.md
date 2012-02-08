### Introduction

This is a simple script which scans the given subnets for running counter strike servers, and prints the list found.

### Usage:

Tweak/Edit the following stuff, and run the script:

* Value passed to socket.setdefaulttimeout
* subnetList
* fileName

### Python modules used:

netaddr

### Important:

You might need to increase the threshold level for network devices if the number of IPs is too large.

I had to use the following values:

/etc/sysctl.conf

```
net.ipv4.neigh.default.gc_thresh1 = 4096
net.ipv4.neigh.default.gc_thresh2 = 8192
net.ipv4.neigh.default.gc_thresh3 = 16384
```

### Resources:

Python Sockets: http://docs.python.org/library/socket.html

CS Server Commands: https://developer.valvesoftware.com/wiki/Server_Queries
