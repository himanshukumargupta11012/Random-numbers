void uniform(char*file,int len);
float mean(char*file);
float variance(char*file);
void gaussian(char*file,int len);
void triangular(char*file,char*file2,char*file3,int len);
void bernoulli(char*file,int len);
void logarithmic(char *file,char*file2,int len);
// void gau_gau(char*file,char* file2,char*file3,int len);
void gau_gau(char*file,int para,int len);


void uniform(char*file,int len){
FILE*fp;
fp=fopen(file,"w");
// srand(time(0));
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

void gaussian2(char*file,int len){
    FILE*fp=fopen(file,"w");
    char str[30];
    srand(time(0));
    for(int i=0;i<len;i++){
        float m=0;
        for(int j=0;j<80;j++){
            m+=(double)rand()/RAND_MAX;
        }
        fprintf(fp,"%lf\n",m-40);
    
    }
    fclose(fp);
}

void logarithmic(char *file,char*file2,int len){
    FILE*fp=fopen(file,"w");
    FILE*fp2=fopen(file2,"r");
    char str[100];
    for(int i=0;i<len;i++){
        fprintf(fp,"%lf\n",-1*2*log(1-atof(fgets(str,sizeof(str),fp2))));
    }
    fclose(fp);
}
// void triangular(char*file,char*file2,char*file3,int len){
//     FILE*fp=fopen(file,"w");
//     FILE*fp2=fopen(file2,"r");
//     FILE*fp3=fopen(file3,"r");
//     char str[20],str2[20];
//     for(int i=0;i<len;i++){
//         fprintf(fp,"%lf\n",atof(fgets(str,sizeof(str),fp2))+atof(fgets(str2,sizeof(str2),fp3)));
//     }
//     fclose(fp);
//     fclose(fp2);
//     fclose(fp);


// }
void triangular(char*file,char*file2,char*file3,int len){
    uniform(file2,len);
    uniform(file3,len);

    FILE*fp=fopen(file,"w");
    FILE*fp2=fopen(file2,"r");
    FILE*fp3=fopen(file3,"r");
    char str[20],str2[20];
    for(int i=0;i<len;i++){
        fprintf(fp,"%lf\n",atof(fgets(str,sizeof(str),fp2))+atof(fgets(str2,sizeof(str2),fp3)));
    }
    fclose(fp);
    fclose(fp2);
    fclose(fp);

}
void bernoulli(char*file,int len){
    FILE*fp=fopen(file,"w");
    int m;
    for(int i=0;i<len;i++){
        double t=(double)rand()/RAND_MAX;
        
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
        fprintf(fp,"%lf\n",A*atoi(fgets(str,sizeof(str),fp2))+atof(fgets(str2,sizeof(str2),fp3)));
    }

    fclose(fp);
    fclose(fp2);
    fclose(fp3);
}

double gen_gau(){
    double m=0;
    for(int k=0;k<12;k++){
        m+=(double)rand()/RAND_MAX;
    }
    return m-6;
}

void chi_2(char*file,int para,int len){
    FILE*fp=fopen(file,"w");

    for(int i=0;i<len;i++){
        float l=0;
        for(int j=0;j<para;j++){
            double t=gen_gau();
            l+=pow(t,2);
        }
        fprintf(fp,"%lf\n",l);

    }
    fclose(fp);
}

// void rayleish(char*file,char*file2,int len,float sig){
//     FILE*fp=fopen(file,'w');
//     FILE*fp2=fopen(file2,'r');
//     char str[20];
//     for(int i=0;i<len;i++){
//         fprintf(fp,"%lf\n",sig*sqrt(-2*log(atof(fgets(str,sizeof(str),fp2)))));
//     }
// }