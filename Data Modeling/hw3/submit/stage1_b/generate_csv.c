#include <stdio.h>
#include <stdlib.h>
#include <sys/times.h>
#include <string.h>
#include "record.h"


int checkRepeat(char (*arr)[64], char* key, int id){

    if(id==0){
        return 0;  
    }else{
        for(int i=0; i<id; i++){
            if(strcmp(arr[i], key)==0){
                //printf("arr=%s,id=%d\n", arr[i],id);  //print repeat element
                return i+1;
            }
        }
        return 0;
    } 
    
}

int splitData(char *arr, char *key, int start, char delimiter){
    memset(key,0,64);
    int n = strlen(arr);
    int index=0;

    for(int i=start; i<n; i++){
       
        if(arr[i] != delimiter){
            key[index] = arr[i];
            //printf("state[]= %c\n", state[index]);
            index++;
        }else{
            return 0;
        }
    }
    return 0;
}


int main(int argc, char **argv)
{
    int i;

    /* print usage if needed */
    if (argc != 3) {
        fprintf(stderr, "Usage: %s first_record_id last_record_id\n", argv[0]);
        exit(0);
    }
    
    /* first and last record ids */
    int first_record_id = atoi(argv[1]);
    int last_record_id = atoi(argv[2]);
    

    char filename[1024];
    FILE *fp = NULL;
    
    struct timeval time_start, time_end;
    
    /* start time */
    gettimeofday(&time_start, NULL);

    char cities[2000][64];
    char states[60][64];

    int user_i=0;
    int city_i=0;
    int state_i=0;
    int message_i=0;
        
    FILE *fMes=NULL;
    fMes = fopen("csv/message.csv", "w+");
    FILE *fUser=NULL;
    fUser = fopen("csv/user.csv", "w+");
   

    for (i = first_record_id; i <= last_record_id; i++) {
        /* open the corresponding file */  
        sprintf(filename, "record_%06d.dat", i);

        fp = fopen(filename,"rb");
    
        if (!fp) {
            fprintf(stderr, "Cannot open %s\n", filename);
            continue;
        }
        
        /* read the record from the file */
        record_t *rp = read_record(fp);
        
        /* =========== start of data processing code ================ */

        char firstName[64];
        char lastName[64];
        char *name = rp->name;
        splitData(name,firstName,0,' ');
        splitData(name,lastName,strlen(firstName)+1,' ');
        user_i++;   

        
        char city[64];
        char state[64];
        char *location = rp->location; 
        splitData(location,city,0,',');
        splitData(location,state,strlen(city)+1,',');

        int city_r_i = checkRepeat(cities, city, city_i);
        if(city_r_i>0){
            
        }else{
             strcpy(cities[city_i],city);
             city_i++;
             city_r_i=city_i;
        }
        int state_r_i=checkRepeat(states, state, state_i);
        if(state_r_i>0){
            
        }else{
             if(strlen(state)!=0){
                strcpy(states[state_i],state);
                state_i++;
                state_r_i=state_i;
             }   
        }
        

        fprintf(fUser, "%d,%s,%s,%d,%d\n", user_i,firstName,lastName,city_r_i,state_r_i);

        for (int j = 0; j < rp->message_num; j++) {           
            message_t *message = &(rp->messages[j]);
            char time[1024];
            sprintf(time,"%04d/%02d/%02d %02d:%02d", message->year, message->month, message->day, message->hour, message->minute);
            char text[1024];
            strcpy(text,message->text);
            message_i++;
            
            fprintf(fMes, "%d,%d,%s,%s\n", message_i,user_i,time,text);
            memset(time,0,1024);
            memset(text,0,1024);
        }      

        /* =========== end of data processing code ================ */    

        free_record(rp);
        fclose(fp);
        
    }    
    
    fclose(fMes);
    fclose(fUser);

    FILE *f=NULL;
    f = fopen("csv/city.csv", "w+");
    fprintf((f), "%d,%s\n",0,"" );
    for(int i=0; i<city_i; i++){
       
        fprintf(f, "%d,%s\n", (i+1), cities[i]);
    }
    fclose(f);

    f=NULL;
    f = fopen("csv/state.csv", "w+");
    fprintf((f), "%d,%s\n",0,"" );
    for(int i=0; i<state_i; i++){
       
        fprintf(f, "%d,%s\n", (i+1), states[i]);
    }
    fclose(f);

    /* end time */
    gettimeofday(&time_end, NULL);
    float totaltime = (time_end.tv_sec - time_start.tv_sec)
                    + (time_end.tv_usec - time_start.tv_usec) / 1000.0f;
                    
         
                    
    printf("\n\nProcess time %f ms\n", totaltime);
    
    return 0;
}
