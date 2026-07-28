#include <stdlib.h>
#include <limits.h>

typedef long long ll;

typedef struct {
    ll cost;
    int x, y, p;
} Node;

typedef struct {
    Node *a;
    int sz;
} Heap;

void swap(Node *a, Node *b){
    Node t=*a;
    *a=*b;
    *b=t;
}

void push(Heap *h, Node v){
    int i=h->sz++;
    h->a[i]=v;
    while(i){
        int p=(i-1)/2;
        if(h->a[p].cost<=h->a[i].cost) break;
        swap(&h->a[p],&h->a[i]);
        i=p;
    }
}

Node pop(Heap *h){
    Node ret=h->a[0];
    h->a[0]=h->a[--h->sz];
    int i=0;
    while(1){
        int l=2*i+1,r=2*i+2,s=i;
        if(l<h->sz && h->a[l].cost<h->a[s].cost) s=l;
        if(r<h->sz && h->a[r].cost<h->a[s].cost) s=r;
        if(s==i) break;
        swap(&h->a[s],&h->a[i]);
        i=s;
    }
    return ret;
}

long long minCost(int m, int n, int** penalty, int penaltySize, int* penaltyColSize) {

    int N=m*n;

    ll *dist=malloc(sizeof(ll)*N*2);

    for(int i=0;i<N*2;i++)
        dist[i]=LLONG_MAX;

    Heap h;
    h.a=malloc(sizeof(Node)*(N*10+10));
    h.sz=0;

    dist[0]=1;

    push(&h,(Node){1,0,0,0});

    int dx[4]={-1,1,0,0};
    int dy[4]={0,0,-1,1};

    while(h.sz){

        Node cur=pop(&h);

        int id=(cur.x*n+cur.y)*2+cur.p;

        if(cur.cost!=dist[id]) continue;

        if(cur.x==m-1 && cur.y==n-1){
            free(dist);
            free(h.a);
            return cur.cost;
        }

        int np=cur.p^1;

        /* wait */
        ll nc=cur.cost+penalty[cur.x][cur.y];
        int nid=(cur.x*n+cur.y)*2+np;

        if(nc<dist[nid]){
            dist[nid]=nc;
            push(&h,(Node){nc,cur.x,cur.y,np});
        }

        /* moves */
        for(int k=0;k<4;k++){

            int nx=cur.x+dx[k];
            int ny=cur.y+dy[k];

            if(nx<0||nx>=m||ny<0||ny>=n) continue;

            int ok=0;

            if(cur.p==0){ /* odd action */
                if((dx[k]==1&&dy[k]==0)||(dx[k]==0&&dy[k]==1))
                    ok=1;
            }else{ /* even action */
                if((dx[k]==-1&&dy[k]==0)||(dx[k]==0&&dy[k]==-1))
                    ok=1;
            }

            ll add=(ll)(nx+1)*(ny+1);

            if(!ok) add+=penalty[cur.x][cur.y];

            nc=cur.cost+add;

            nid=(nx*n+ny)*2+np;

            if(nc<dist[nid]){
                dist[nid]=nc;
                push(&h,(Node){nc,nx,ny,np});
            }
        }
    }

    free(dist);
    free(h.a);
    return -1;
}