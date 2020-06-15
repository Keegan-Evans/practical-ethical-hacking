# Common Network Commands

```
ifconfig
```

It shows your network interfaces and associated information with them. 

For wireless networking devices:

```
iwconfig
```

Another common command:

```
ping ip_address_trying_to_communicate_with
```

Will run forever unless you stop it with <kbd> Ctrl </kbd> + <kbd>
c </kbd>

```
arp -a
```

Shows ip address it talks to and the MAC address associated with it. A way
of associating ip addresses with MAC addresses

```
netstat -ano
```

Shows what connections are open and which are talking. 
