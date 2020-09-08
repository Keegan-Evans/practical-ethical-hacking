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
