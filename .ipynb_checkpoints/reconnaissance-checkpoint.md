We need a client to attack:

bugcrowd provides companies that are open to having bugs found. 

### Email address gathering with hunter.io

Allows you to search entire domains for email addresses. It also gives you
an idea of form the addresses take, this is handy, because if we find
someone on linked-in or facebook, but they don't list their email address,
we can take a guess at it. Often see break down by department, handy to
see who works where, and can give you information/names you can use if you
are performing social engineering. 

### Gathering Breach Credentials with Breach-Parse

Username enumeration through breached credentials.

[breach parse tool](github.com/hmaverickadams/breach-parse)

extract into `/opt`

in the /opt/breach-parse/BreachCompilation/data there are emails and
passwords grouped by the first letter of the email. 

To run:

``` bash

cd /opt/breach-parse/

./breach-parse.sh @target_domain output-file.txt

```


