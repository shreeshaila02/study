#include<stdio.h>
#include<stdlib.h>
struct day
{
    char*name;
    int date;
    char*activity;
}
calendar[3];
void creat()
{
    for(int i=0;i<3;i++){
        calendar[i].name=malloc(20*sizeof(char));
        calendar[i].activity=malloc(100*sizeof(char));

    }
}
void read()
{
    for(int i=0;i<3;i++){
        printf("enter the name of the day:");
        scanf("%19s,calendar[i].name");
        printf("enter the date:");
        scanf("%d,&calendar[i].date");
        printf("enter the activity:");
        scanf("%99[^\n],calendar[i].activity");
        
    }
}
void display() {
    printf("\nDay\t\tDate\tActivity\n");
    printf("---------------------------------------\n");
    for (int i = 0; i < 3; i++) {
        printf("%-10s\t%d\t%s\n", calendar[i].name, calendar[i].date, calendar[i].activity);
    }
}

int main()
{
    printf("creating the calendar entries....\n");
    creat();
    printf("reading the calendar entries...\n");
    read();
    printf("\ndisplay the calendar entries...\n");
    display();
    for(int i=0;i<7;i++){
        free(calendar[i].name);
        free(calendar[i].activity);
    }
    return 0;
}
