#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define STATE_SIZE 8
#define GET_BIT(s,n) ((s >> n) & 0x1)

// These two macros are for debugging purposes.
// http://stackoverflow.com/a/3208376
#define B_PATTERN "%c%c%c%c%c%c%c%c"
#define B2B(byte)  \
      (byte & 0x80 ? '1' : '0'), \
  (byte & 0x40 ? '1' : '0'), \
  (byte & 0x20 ? '1' : '0'), \
  (byte & 0x10 ? '1' : '0'), \
  (byte & 0x08 ? '1' : '0'), \
  (byte & 0x04 ? '1' : '0'), \
  (byte & 0x02 ? '1' : '0'), \
  (byte & 0x01 ? '1' : '0') 

// The integer type to handle the cipher
typedef uint8_t c_size;

// Gets a byte of output from the PRNG
uint8_t getbyte(c_size state, c_size feedback) {
    uint8_t retval = 0;
    for (int i=0; i<8; i++) {
        uint8_t  out_bit = state & 1;
        retval <<= 1;
        retval |= out_bit;
        state >>= 1;
        feedback ^= state;
        if (feedback & 1) state |= 0b10000000;
    }
    return retval;
}

int main() {
    c_size state = 0b10101001;
    c_size feedback = 0; 

    printf("Enter text to encrypt: ");
    char* ptext = 0;
    uint8_t ctext[strlen(ptext) + 1];
    for (unsigned long i=0; i<strlen(ptext); i++) {
        uint8_t b = getbyte(state, feedback);
        ctext[i] = (uint8_t)(b ^ ptext[i]);
        ctext[i] = (uint8_t)(b ^ ctext[i]);
    }
    ctext[strlen(ptext)] = '\0';

    printf("ctext: ");
    for (unsigned long i=0; i<strlen(ptext); i++) {
        printf("%x", ctext[i]);
    }
    printf("\nptext: ");
    for (unsigned long i=0; i<strlen(ptext); i++) {
        printf("%x", ptext[i]);
    }
    printf("\n");

    /* Debug statement to show the internal state
    printf("state: "B_PATTERN\
            "\tp: "B_PATTERN\
            "\tfeedback: "B_PATTERN\
            "\tout_bit: %u\n",\
            B2B(state), B2B(p), B2B(feedback), out_bit);
    */
    
    return 0;
}
