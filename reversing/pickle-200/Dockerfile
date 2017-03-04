FROM ubuntu:latest
COPY pwn-200.py /opt/challenge/
COPY flag.txt /opt/challenge/

RUN apt-get update -y
RUN apt-get install -y python3
RUN adduser challenge
RUN chown -R challenge:challenge /opt/challenge
RUN chown root:root /opt/challenge/pwn-200.py
RUN chown root:root /opt/challenge/flag.txt
RUN chmod 644 /opt/challenge/pwn-200.py
RUN chmod 644 /opt/challenge/flag.txt

USER challenge
WORKDIR /opt/challenge

CMD "python3 pwn-200.py;"
