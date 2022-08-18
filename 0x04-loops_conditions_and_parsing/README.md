## Poject Title: Loops, conditions and parsing
## Resources
# Read or watch:

- Loops sample
- Variable assignment and arithmetic
- Comparison operators
- File test operators
- Make your scripts portable
# man or help:

- env
- cut
- for
- while
- until
- if
# Learning Objectives
*At the end of this project, I am expected to be able to explain to anyone, without the help of Google:*

# General
- How to create SSH keys
- What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
- How to use while, until and for loops
- How to use if, else, elif and case condition statements
- How to use the cut command
- What are files and other comparison operators, and how to use them

# Loops
Loops allow us to take a series of commands and keep re-running them until a particular situation is reached. They are useful for automating repetitive tasks.

# Types of Loop statement
- For Loop statement:
For loop is a type of looping statement to execute a set of commands for a certain number of times.
- Syntax


for NAME [in LIST ]; do COMMANDS; done

- while Loop statement:
The while construct allows for repetitive execution of a list of commands, as long as the command controlling the while loop executes successfully (exit status of zero).
- Syntax

while CONTROL-COMMAND; do CONSEQUENT-COMMANDS; done

- Until Loop statement:
Until looping statement is similar to the while loop statement. The difference between two is, it will execute the body of the loop until the conditional statement becomes true whereas while loop executes commands if the condition is true.
- Syntax

until TEST-COMMAND; do CONSEQUENT-COMMANDS; done
