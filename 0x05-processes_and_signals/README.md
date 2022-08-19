### Project Title: Processes and signals
## Resources
# Read or watch:

- Linux PID
- Linux process
- Linux signal
man or help:

- ps
- pgrep
- pkill
- kill
- exit
- trap
# Learning Objectives
*At the end of this project, I am expected to be able to explain to anyone, without the help of Google:*

# General
- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored.

# What is a Process?
A process can be thought of as an instance of a program in execution. We called this an ‘instance of a program’, because if the same program is run lets say 10 times then there will be 10 corresponding processes.

Moving ahead, each process has its own unique process ID through which it is identified in the system. Besides it own ID, a parent’s process ID is also associated with a process.

# What is a signal? 
Signals are software interrupts.

A robust program need to handle signals. This is because signals are a way to deliver asynchronous events to the application.

A user hitting ctrl+c, a process sending a signal to kill another process etc are all such cases where a process needs to do signal handling.

# Linux Signals
In Linux, every signal has a name that begins with characters SIG. For example :

- A SIGINT signal that is generated when a user presses ctrl+c. This is the way to terminate programs from terminal.
- A SIGALRM  is generated when the timer set by alarm function goes off.
- A SIGABRT signal is generated when a process calls the abort function.
etc
