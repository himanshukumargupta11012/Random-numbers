void uniform(char*file,int len);
float mean(char*file);
float variance(char*file);
void gaussian(char*file,int len);
void triangular(char*file,int len);
void bernoulli(char*file,int len);
void gau_gau(char*file,char* file2,char*file3,int len);

void uniform(char*file,int len){
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
    srand(time(0));
    for(int i=0;i<len;i++){
        float m=0;
        for(int j=0;j<12;j++){
            m+=(double)rand()/RAND_MAX;
        }
        fprintf(fp,"%lf\n",m-6);
    
    }
    fclose(fp);
}
void rayleigh(char *file,char*file2,int len){
    FILE*fp=fopen(file,"w");
    FILE*fp2=fopen(file2,"r");
    char str[100];
    for(int i=0;i<len;i++){
        fprintf(fp,"%lf\n",-1*2*log(1-atof(fgets(str,sizeof(str),fp2))));
    }
    fclose(fp);
}
void triangular(char*file,int len){
    FILE*fp=fopen(file,"w");
    for(int i=0;i<len;i++){
        fprintf(fp,"%lf\n",(float)rand()/RAND_MAX+(float)rand()/RAND_MAX);
    }
    fclose(fp);
}
void bernoulli(char*file,int len){
    FILE*fp=fopen(file,"w");
    int m;
    for(int i=0;i<len;i++){
        float t=(float)rand()/RAND_MAX;
        
        if (t<.5) m= -1;
        if(t>=.5) m=1;
        fprintf(fp,"%d\n",m);
    }
    fclose(fp);
}

void ber_gau(char*file,char*file2,char*file3,int len){
    FILE*fp=fopen(file,"w");
    FILE*fp2=fopen(file2,"r");
    FILE*fp3=fopen(file3,"r");  
    char str[20],str2[20];
    int A=5;
    for(int i=0;i<len;i++){
        fprintf(fp,"%lf\n",A*atof(fgets(str,sizeof(str),fp2))+atof(fgets(str2,sizeof(str2),fp3)));
    }

    fclose(fp);
    fclose(fp2);
    fclose(fp3);
}

void gau_gau(char*file,char* file2,char*file3,int len){
    FILE*fp=fopen(file,"w");
    FILE*fp2=fopen(file2,"r");
    FILE*fp3=fopen(file3,"r");
    char str[20],str2[20];
    for(int i=0;i<len;i++){
        float X1=atof(fgets(str,sizeof(str),fp2));
        float X2=atof(fgets(str2,sizeof(str2),fp3));
        fprintf(fp,"%lf\n",X1*X1+X2*X2);
    }
    fclose(fp);
    fclose(fp2);
}