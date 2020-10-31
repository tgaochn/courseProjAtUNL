#include <stdio.h>
#include <stdlib.h>
#include <sys/times.h>
#include <limits.h>

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
    
    int count = 0;
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
        for (int j = 0; j < rp->message_num; j++) {           
            message_t *mes = &(rp->messages[j]);
            int hour = mes->hour;
            if(hour==8){
                count ++;
                //printf("id = %d\n",rp->id);
                j += rp->message_num;
            }
           
        }
        /* =========== end of data processing code ================ */    
    
        /* free memory */
        free_record(rp);
    
        /* close the file */
        fclose(fp);
    }    
        
    printf("The total number of user who sent messages between 8am-9am is %d",count);
    /* end time */
    gettimeofday(&time_end, NULL);
    
    float totaltime = (time_end.tv_sec - time_start.tv_sec)
                    + (time_end.tv_usec - time_start.tv_usec) / 1000.0f;
                    
         
                    
    printf("\n\nProcess time %f ms\n", totaltime);
    
    return 0;
}
