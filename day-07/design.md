# Day 07 – Thinking Before Coding (DevOps Mindset)

## Background (Day 01 & Day 02)
On Day-01 and Day-02, I mainly worked on understanding Python basic syntax.
I learned things like:
- variables
- conditions
- functions
- basic scripts
- simple API usage

At that stage, the focus was more on *how Python works*, not on building production-ready tools.

---

## Script Selected
Log Analyzer Script (Day 06 – CLI based)

---

## What problem am I solving?
In real systems, applications generate large log files.
Manually checking logs line by line is time-consuming and error-prone.

As a DevOps engineer, I need a simple tool that can quickly tell me:
- how many INFO messages are there
- how many WARNING messages are there
- how many ERROR messages are there

This script helps me understand the system health without manually reading logs.

---

## What input does my script need?
The script takes input from the user through command line:

- Log file path (required)
- Output file path (optional)
- Log level filter like INFO, WARNING, or ERROR (optional)

Example:
- app.log
- --level ERROR

---

## What output should my script give?
The script should:
- Show log summary in the terminal
- Save the same summary in an output file

Example output:
- INFO: 10
- WARNING: 2
- ERROR: 3

This makes it easy to quickly identify problems.

---

## What are the main steps involved?
1. User provides log file path using CLI
2. Script reads the log file safely
3. Script checks each line for log levels
4. Script counts INFO, WARNING, and ERROR messages
5. If a level filter is provided, only that level is shown
6. Summary is printed in terminal
7. Summary is written to an output file

