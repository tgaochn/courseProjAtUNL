#include <stdio.h>
#include <stdlib.h>
#include <sys/times.h>
#include <string.h>
#include "record.h"


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
    
    char name[64];
    int max = 0;
    int id=0;

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
        int mes_num = 0;
        char *loc = rp->location;
        char * ret;
        ret = strstr(loc, "Nebraska");
        if(ret){
            for (int j = 0; j < rp->message_num; j++) {           
                message_t *mes = &(rp->messages[j]);
                int hour = mes->hour;
                if(hour==8){
                    mes_num++;
                }
               
            }
            if(mes_num>max){
                max = mes_num;
                strcpy(name,rp->name);
                id=rp->id;
            }
            
        }
        
        /* =========== end of data processing code ================ */    
    
        /* free memory */
        free_record(rp);
    
        /* close the file */
        fclose(fp);
    }    
        
    
    /* end time */
    gettimeofday(&time_end, NULL);
    printf("%s (id=%d) is the user who sent the most messages between 8am-9am in Nebraska. He sent %d messages",name,id,max);
    float totaltime = (time_end.tv_sec - time_start.tv_sec)
                    + (time_end.tv_usec - time_start.tv_usec) / 1000.0f;
                    
         
                    
    printf("\n\nProcess time %f ms\n", totaltime);
    
    return 0;
}
