services mean: webservers, sql database, etc

### apache2

start with ifconfig, get ip address. Shows that it can't connect, start
a web server:

```
service apache2 start
```

If you want to actually host files on this, there is a fairly easy way:

```
python -m SimpleHTTPServer 8080
```

this wil go off line when the machine reboots, if you want to keep it open
you can use 

```
systemctl enable service
```

but you should only do it with postgresql
