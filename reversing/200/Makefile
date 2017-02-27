CC=gcc
CFLAGS=-Wall -Werror

clean:
	rm -f rev-200-testing rev-200-release rev-200-private

test: rev-200.c
	$(CC) $(CFLAGS) -g -o rev-200-testing rev-200.c

release: rev-200.c
	$(CC) $(CFLAGS) -O0 -o rev-200 rev-200.c
