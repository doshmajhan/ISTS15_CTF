# Bleeding Heart
Exploit Heartbleed using a [simple PoC script](https://gist.github.com/sh1n0b1/10100394) to pull the flag from memory. There's a script running on the challenge box (`sendflag.sh`) to continually put the flag back in memory, as the flag is usually overwritten in memory after every HTTP request sent to the server.

Set up using Ubuntu 12.04 following [this guide](https://warroom.securestate.com/building-a-vulnerable-box-heartbleed/).
