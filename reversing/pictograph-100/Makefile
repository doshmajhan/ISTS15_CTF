CC=gcc
CFLAGS=-Wall -Werror

clean:
	rm -f rev-100-testing rev-100-release rev-100-private rev-100

test: rev-100.c
	$(CC) $(CFLAGS) -g -o rev-100-testing rev-100.c

release: rev-100.c
	$(CC) $(CFLAGS) -O0 -o rev-100 rev-100.c
	
