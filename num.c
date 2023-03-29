int inverse_num(int nb, int siz) {
    return siz - nb;
}

#include <string.h>

char *ralong(char *text, int length) {
    int text_len = strlen(text);

    if (text_len < length) {
        char *padding = malloc((length - text_len + 1) * sizeof(char));
        memset(padding, ' ', length - text_len);
        padding[length - text_len] = '\0';
        strcat(padding, text);
        return padding;
    } else {
        return text;
    }
}


//gcc -shared -o libnum.so num.c
