void uniform(int len,char*file);
float mean(char*file);
float variance(char*file);
void gaussian(char*file,int len);
void triangular(char*file,int len);
void uniform(int len,char*file){
FILE*fp;
fp=fopen(file,"w");
for(int i=0;i<len;i++){

fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);

}
fclose(fp);
}

float mean(char*file){
    FILE*fp;
    fp=fopen(file,"r");
    if(fp==NULL){
        printf("unable to open");
    }
    float m=0;
    int n=0;
    char line[20];
    while(fgets(line,sizeof(line),fp)){
        m+=atof(line);
        n+=1;}
fclose(fp);
        return m/n;
}

float variance(char*file){
    FILE*fp;
    fp=fopen(file,"r");
    if(fp==NULL){
        printf("unable to open");
    }
    float m=0;
    int n=0;
    char line[20];
    while(fgets(line,sizeof(line),fp)){
        m+=atof(line)*atof(line);
        n+=1;}
fclose(fp);
        return m/n-mean(file)*mean(file);
}


void gaussian(char*file,int len){
    FILE*fp=fopen(file,"w");
    char str[30];
    for(int i=0;i<len;i++){
        float m=0;
        for(int j=0;j<12;j++){
            m+=(double)rand()/RAND_MAX;
        }
        fprintf(fp,"%lf\n",m-6);
    
    }
}

// void triangular(char*file,int len){
//     FILE*fp=fopen(file,"w");
//     for(int i=0;i<len;i++){
//         fprintf(fp,"%lf",rand()/RAND_MAX+rand()/RAND_MAX);
//     }
// }
