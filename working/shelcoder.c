#include<stdio.h>
#include<string.h>
void argparse(int argc,char*argv[],char* inf_name,char* outf_name);
int main(int argc,char* argv[])
{
    char inf_name[256],outf_name[256];
    FILE *infile,*outfile;
    argparse(argc,argv,inf_name,outf_name);
    printf("input filename = %s\noutput filename= %s",inf_name,outf_name);

}
void argparse(int argc,char*argv[],char* inf_name,char* outf_name)
{

    int x,odone=0,indone=0;
    if (argc==1)
    {
        printf("usage: shellcoder -o [output filename] [input filename]\n");
    }
    else
    {
        for (x=1; x<argc; x++)
        {
            if(strstr("-o",argv[x])&&odone==0)
            {
                odone=1;
                strcpy(outf_name,argv[x+1]);
                x++;
            }
            else if (indone==0)
            {
                indone=1;
                strcpy(inf_name,argv[x]);
            }
            else
            {
                printf("dont know how to use %s\t\tCONSIDER RECHECKING THE COMMAND\n",argv[x]);
            }
        }
        if (odone==0)
        {
            strcpy(outf_name,inf_name);
        }
    }
}

