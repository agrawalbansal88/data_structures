#include <stdio.h>
#include <string.h>

int compare(const char *c1, const char *c2)
{
    int index = 0;
    while(c1[index] != '\0' && c2[index] != '\0')
    {
        if(c1[index] != c2[index])
        {
            break;
        }
        index++;
    }
    return c1[index]-c2[index];
}   

//Following solution assumes that characters are represented using ASCII representation, i.e., codes for ‘a’, ‘b’, ‘c’, … ‘z’ are 97, 98, 99, … 122 respectively. And codes for ‘A’, “B”, ‘C’, … ‘Z’ are 65, 66, … 95 respectively.
int ignore_case_compare(const char *c1, const char *c2)
{
    int index = 0;
    while(c1[index] != '\0' && c2[index] != '\0')
    {
        if((c1[index] != c2[index]) && ((c1[index]^32) != c2[index]))
        {
            break;
        }
        index++;
    }
    return c1[index]-c2[index];
}
int main()
{
    printf("Ankur\n");
    //compare("PAPA", "MAMMA");
    char *str1 = "PApA";
    char *str2 = "PAPA";
    printf("%d\n", compare(str1,str2));
    printf("%d\n", ignore_case_compare(str1,str2));
    int retval = strcmp(str1,str2);
    printf("%d\n", retval);

}
