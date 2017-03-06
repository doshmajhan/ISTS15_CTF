# Stuck in Traffic
Teams are given: state_secrets.pcap
1. Find the irc conversation: WireShark filter for IRC
2. Find the pdf file: WireShark search for hex value of PDF file to see start of FTP transfer -> follow stream -> raw -> save as "blah.pdf"
3. Extract the base64 encoded password from the ICMP messages: probably going to want to script that, convert, and use to unlock PDF file.
