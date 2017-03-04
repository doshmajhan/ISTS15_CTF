#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

#define STDIN_FLUSH() scanf("%*[^\n]%*c");

typedef struct artist {
    char name[64];
    int age;
} artist_t;

typedef struct album {
    char title[64];
    int num_songs;
    artist_t* artist;
} album_t;

typedef struct song {
    char title[64];
    double length;
    album_t* album;
} song_t;


// Track all allocated objects for some reason
artist_t** artists = NULL;
album_t** albums = NULL;
song_t** songs = NULL;
unsigned int num_artists = 0;
unsigned int num_albums = 0;
unsigned int num_songs = 0;


void menu() {
    puts("1: Add new artist");
    puts("2: Add a new album");
    puts("3: Add a new song");
    puts("4: List all entered data");
    puts("0: Exit");
    printf("> ");
}


void add_artist() {
    char name[64];
    int age;
    artist_t* artist = malloc(sizeof(artist_t));

    printf("Enter name: ");
    scanf(" "); // Flush stored newline
    fgets(name, 64, stdin);
    printf("Enter age: ");
    scanf("%d", &age);
    
    artist->age = age;
    // Red herrings are fun
    strcpy(artist->name, name);

    // Add the artist to the artist list
    num_artists++;
    artists = realloc(artists, num_artists * sizeof(artist_t));
    assert(artists);
    artists[num_artists - 1] = artist;

    puts("Artist added!");
}


void add_album() {
    char title[64];
    int num_songs;
    album_t* album = malloc(sizeof(album_t));

    printf("Album title: ");
    scanf(" "); // Flush stored newline
    fgets(title, 64, stdin);
    printf("Number of songs: ");
    scanf("%d", &num_songs);
    
    // Select artist
    if(num_artists) {
        for(unsigned int i=0; i<num_artists; i++) {
            printf("%u: %s\n", i + 1, artists[i]->name);
        }
        unsigned int choice;
        // Pick the artist to reference
        do {
            printf("Artist number: ");
            scanf("%d", &choice);
        } while (choice == 0 || choice > num_artists + 1);
        album->artist = artists[choice - 1];
    } else {
        puts("How can you add an album if there is no artist to play it!?");
        puts("Add an artist and try again.");
        free(album);
        return;
    }

    // Add album to a list
    num_albums++;
    albums = realloc(albums, num_albums * sizeof(album_t));
    assert(albums);
    albums[num_albums - 1] = album; 

    puts("Album added.");
}


void add_song() {
    char title[64];
    int length;
    song_t* song = malloc(sizeof(song_t));

    printf("Song title: ");
    scanf(" "); // Flush stored newline
    fgets(title, 64, stdin);
    printf("Song length in seconds: ");
    scanf("%d", &length);
    
    // Select album
    if(num_artists) {
        for(unsigned int i=0; i<num_albums; i++) {
            printf("%u: %s\n", i, albums[i-1]->title);
        }
        unsigned int choice;
        // Pick the artist to reference
        do {
            printf("Album number: ");
            scanf("%d", &choice);
        } while (choice == 0 || choice > num_albums + 1);
        song->album = albums[choice - 1];
    } else {
        puts("We don't accept no stinking singles here!");
        puts("Come back when you have an album to add your song to!");
        free(song);
        return;
    }

    // Add song to a list
    num_songs++;
    assert(realloc(songs, num_songs * sizeof(song_t)));
    songs[num_songs - 1] = song; 

    puts("Album added.");

}


void list_all() {
    puts("-- Artists --");
    for(unsigned int i=0; i<num_artists; i++) {
        puts(artists[i]->name);
    }

    puts("\n-- Albums --");
    for(unsigned int i=0; i<num_albums; i++) {
        printf("%s by %s\n", albums[i]->title, albums[i]->artist->name);
    }

    puts("\n-- Songs --");
    for (unsigned int i=0; i<num_songs; i++) {
        printf("%s from %s\n", songs[i]->title, songs[i]->album->title);
    }
}


void challenge() {
    puts("Welcome to 'My New EP'");
    puts("The best music cataloging service!");

    int choice;
    while(1) {
        menu();
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                add_artist();
                break;
            case 2:
                add_album();
                break;
            case 3:
                add_song();
                break;
            case 4:
                list_all();
                break;
            case 0:
                printf(":( kbai\n");
                return;
        }
    }
}


int main() {
    challenge();
}
