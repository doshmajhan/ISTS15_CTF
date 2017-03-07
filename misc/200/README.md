# Banner Karaoke
User connects from an IP within their Corp network (scored services), and the challenge script determines the IPs of some of their scored services based on their team number within their IP. The script then connects to these services and checks their service banner against a string of song lyrics, modeling a karaoke prompt. The user must modify each of their service banners to the correct song lyrics to get the flag.

Services and lyrics:
  * FTP -- `NEVER GONNA GIVE YOU UP`
  * SSH -- `NEVER GONNA LET YOU DOWN`
  * POP3 -- `NEVER GONNA RUN AROUND`
  * QOTD -- `AND DESERT YOU`
  
Flag: `flag{R1CK_45TLY_4EVR}`
