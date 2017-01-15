#include <conio.h>
#include <stdio.h>
#include <string.h>


typedef struct telefon
{
  char producator[25],model[25],retea[25],culoare[25];//,*categorie
  //nu am nici o idee ce inseamna categorie, deci o comentez pentru moment
  int pret;
  int greutate;
  int bucati;
  struct telefon *urm;
} lista;

lista *adaug(lista *prim,char producator[25],char model[25],char retea[25],char culoare[25],int pret, int greutate,int bucati)
{
    lista *q,*p;
    p = (lista*)malloc(sizeof(lista));
    /*p->producator=(char*)malloc(strlen(producator) + 1);
    p->model=(char*)malloc(strlen(model) + 1);
    p->retea=(char*)malloc(strlen(retea) + 1);
    p->culoare=(char*)malloc(strlen(culoare) + 1);*/
    strcpy(p->producator,producator);
    strcpy(p->model,model);
    strcpy(p->retea,retea);
    strcpy(p->culoare,culoare);
    p->pret=pret;
    p->greutate=greutate;
    p->bucati=bucati;
    p->urm=NULL;

    if(prim==NULL)
    {
        return p;
    }
    else
    {

    }

}
void adauga(lista *prim)
{
    char producator[25],model[25],retea[25],culoare[25];int pret;int greutate;int bucati;
            fflush(stdin);
            sscanf("%s",&producator);
            sscanf("%s",&model);
            sscanf("%s",&retea);
            sscanf("%s",&culoare);
            scanf("%d",&pret);
            scanf("%d",&greutate);
            scanf("%d",&bucati);
            adaug(prim,producator,model,retea,culoare,pret,greutate,bucati);

}
void citire(FILE *fp,lista *prim)
{
     char producator[25],model[25],retea[25],culoare[25];
    int pret;
    int greutate;
    int bucati;
    fseek(fp,0,SEEK_END);
    if(ftell(fp)==0)
        printf("%s","fisierul este gol");
    else
    {
        do
        {   fflush(stdin);
           printf("da");
            fscanf(fp,"%s",&producator);

            fscanf(fp,"%s",&model);
            fscanf(fp,"%s",&retea);
            fscanf(fp,"%s",&culoare);
            fscanf(fp,"%d",&pret);
            fscanf(fp,"%d",&greutate);
            fscanf(fp,"%d",&bucati);
            fflush(stdin);
            adaug(prim,producator,model,retea,culoare,pret,greutate,bucati);

        }
        while(!feof(fp));
    }

}




int main()
{   //deschide
   FILE *fp;
   lista *prim=NULL;
    fp = fopen( "stoc.txt" , "r+" );
    do{
    int selector;
    printf("%s","alegeti ce doriti sa faceti\n");
    printf("%s","1. daca doriti sa cititi\n");
    printf("%s","2.daca doriti sa adaugati\n");
    printf("%s","3. altceva\n");
    printf("%s","4. nedeterminat\n");
    printf("%s","5.another\n");
    printf("%s","6. ultima varianta\n");
    scanf("%d",&selector);
    printf("%d",selector);
    switch(selector)
    {
     case 0: goto end;

     case 1:
         citire(fp,prim);
            break;
     case 2:
         adauga(prim);
            break;
     case 3:
            break;
     case 4:
            break;

     case 5:
            break;

     case 6:
            break;

    default: printf("%s","reintroduceti valoarea");

    }
    } while(1);
    end:


        ;
}
