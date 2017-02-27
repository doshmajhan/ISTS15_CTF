# ISTS-15 (2017) - Reversing/Pwn

## 100 - A Strange Encoding
### Description
The author of this file stored the flag in some strange
pictographic encoding format that we cannot figure out. Can
you recover the data?

### The Challenge
The file stores the flag `flag{p1ct0gr4phs}` in memory. However,
they are stored as pictographs in a 2D array that gets printed without
newlines. Part of the challenge is getting the pictographic data, the
other part is assembling it into a valid flag.

It can be solved with a combination of static and dynamic analysis.
Getting the string arrays is easy enough, the file can be rewritten
in the program to give a simple way to capture the output. Reversing
the binary file, analyzing the system calls writing the data, or simply
applying trial and error, should lead to a column size of 20 characters.
Adding a newline every 20 characters should give a clear representation
of the flag.


## Competition Notes
Binary files appended with `testing` are for debugging purposes before
the competition. They are not the ones distributed to participants. They
are included in the repo for completeness sake.

Binaries with `release` appended are the binary files deemed distributable
for the purpose of the competition.

Binaries with `private` appended are competition binaries running server
applications that are based on the `release` version of the same file.
