#include <stdio.h>

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover card.raw\n");
        return 1;
    }

    char* infile = argv[1];
    const int BLOCK_SIZE = 512;

    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    unsigned char buffer[BLOCK_SIZE];
    FILE* outptr = NULL;
    char image[7];
    int n = 0;

    while(fread(buffer, BLOCK_SIZE, 1, inptr) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            buffer[3] >= 0xe0 && buffer[3] <= 0xef)
        {
            if (n > 0)
            {
                fclose(outptr);
            }
            sprintf(image, "%03d.jpg", n);
            outptr = fopen(image, "w");
            if (outptr == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", image);
                return 3;
            }
            n++;
        }

        if (outptr != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outptr);
        }
    }

    fclose(outptr);
    fclose(inptr);

    return 0;
}
