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

in the `/opt/breach-parse/BreachCompilation/data` there are emails and
passwords grouped by the first letter of the email. 

To run:

``` 

cd /opt/breach-parse/

./breach-parse.sh @target_domain output-file.txt

```

Grabs grabs usernames and passwords from emails from the target domain,
outputs to 3 files
 
- output-file-master.txt 

- output-file-users.txt

- output-file-passwords.txt

Look for users that appear more than once, especially if they have similar
passwords, as they are likely good targets.

- *credential stuffing* : Trying known username and passwords. You can
  also try with variations of the known passwords. 

- *password spraying*: Taking known usernames and spraying likely
  passwords at them.

- *theharvester*: Check out Kali - Applications - 1. Information gathering
  for more tools.  Helps you find subdomains specify a domain and how deep
in you want to go and what you want to search on. Sometimes need api keys
(like on hunter)

> example at 1:50

`theHarvester -d tesla.com -l 500 -b google`[^1]

[^1]: New syntax with a capital "H" instead of "h".

Gives emails and subdomains(with ip addresses).

### Web Information Gathering

May be tasked with web penetration test or a website on an internal or
external penetration test.

1. Identify subdomains. Might run into something like
   dev.target-domain.com or testsite.target-domain.com or login forms or
some other vunerable domain. A good tool is *sublist3r*. Searches the
site: with `sublist3r -d target-domain`. A web tool is
[crt.sh](https://crt.sh), which allows you to specify the wild card that
you use, using "%" as the wild card. This allows you to use *certificate
fingerprinting*. sso-dev, dev, vpn, api-toolbox might all be good targets.
This gives several levels of sublevels. OWASP Amass is the modern tool,
but slow. 

2. Identify Website Technologies. [builtwith](wwww.builtwith.com). Enter
   the domain, and you can identify the technologies the website is using.
[wappalyzer](https://www.wappalyzer.com/) is a browser extension, it
doesn't provide as much information, but it fast. Theoretically not as
passive, as it does actually interact with the website. You can check the
technologies versions to look for vunerabilities/exploits using
enumeration. Built into Kali there is *whatweb*. Can give information
about the versions, not super powerful  but built in. 

3. *burpsuite*: A web proxy/can intercept traffic. To use in Firefox:
   &#9776; -> Preferences > Network Settings (at the bottom) -> Manual
Proxy 127.0.0.1/8080 and ***unicode check box*** "use this proxy server
for all protocols". Then enter (https://burp) in a new tab, accept the
certificate if need be. Then download the certificate, go to Firefox ->
Preferences -> Privacy & Security -> Certificates -> View Certificates ->
Import to add it. Then try loading a webpage, which will seem not to work
but if you go to Burp Suite -> Proxy tab you can see all of the traffic
that BS is capturing from Firefox, that is intercepting the request that
tesla is making out, you can see this clicking through using Forward. To
see summary, turn Intercept Off, then go to Target Tab. If you look at the
GET requests and more importantly the Response to see what the website is
doing. 

> Burp Suite Pro can be quite worth it for professionals. 

### Google Fu

[Google Search
Operators](https://ahrefs.com/blog/google-advanced-search-operators/)

to search on particular site: 

`site:site-to-be-searched.com`

if don't want to search main site you could do:

`site:site-to-be-searched.com -www`

This can be good way to find subdomains. Also find filetypes

`site:site-to-be-searched.com filetype:desired-filetype`

Before you ask a question, Google it.

### Social Media

Images are a good place to start, look for things like badge photos or
desks. Twitter is a good place for these things. Also, especially
"Members"
on LinkedIn, which lets you get names(which you might be able to use to
get email addresses) and email addresses. With a large enough set of
emails, it is almost guaranteed to have a simple password like "Fall2019".
You want email addresses and especially anything that has been part of
a credential breach. People are nearly always the weakest link. 










