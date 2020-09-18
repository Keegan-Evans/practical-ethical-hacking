# Section 17: Attacking Active Directory - Initial Attack Vectors

## Introduction

We are working to get into the network in any way. We can make use of
features of Windows to gain access to additional users, computers, folders
etc. [Top Five Ways I Got Domain Admin Before
Lunch](https://medium.com/@adam.toscher/top-five-ways-i-got-domain-admin-on-your-internal-network-before-lunch-2018-edition-82259ab73aaa).
Some of these are being defended again, though they are generally still
really good to know about.

## LLMNR Poisoning Overview

What is Link Local Modal Name Resolution, basically DNS. It identifies
hosts, when DNS fails. The flaw is that it utilizes usernames and NTLMv2
hashes when appropriately prompted.

When the victim tries to find a resource, we respond back saying "send me
your has and then I can let you know where it is". This is a man in the
middle attack, where we are looking for any event where we can take over
in place of DNS.

`responder` is an `impacket` tool that you can use to respond to these
requests. Running this first thing in the morning or right after lunch.
Should be done even before `Nessus` or `nmap` scans, as these can generate
useful responses as well. There are several directions you can go, but the
first place to try is running the hash through `hashcat` to try to crack
the password, especially if it is a weak password.

## Capturing Hashes with Responder

```
responder -I eth0 -rdwv
```

This will show where it is listening, then with your server running and
another windows machine, try to navigate to your attack machine in the
file browser, which should then cause responder to capture the hash. This
can then be cracked offline using `hashcat`.

## Cracking the Hash with Hashcat


