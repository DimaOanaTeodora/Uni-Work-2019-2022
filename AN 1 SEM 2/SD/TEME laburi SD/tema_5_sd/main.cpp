#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <queue>
using namespace std;

class directedGraph
{
    vector<list<int>> adiacenta;

public:
    directedGraph(){}
    void addNode(int x)
    {
        if (adiacenta.size()<=x)
            adiacenta.resize(x + 1, list<int>());

        adiacenta[x] = list<int>();
    }
    void addEdge(int s, int d)
    {
        adiacenta[s].push_back(d);
    }
    int hasEdge(int s, int t)
    {
        for (list<int>::iterator it = adiacenta[s].begin(); it != adiacenta[s].end(); ++it)
            if (*it == t)
                return 1;

        return 0;
    }

    void BFS(int start);
    void DFS(int start);
    int twoCycles();

};
void directedGraph:: BFS(int start)
{
    cout<<"Parcurgere BFS: "<<endl;

    queue<int> coada;
    coada.push(start);

    set<int> vizit;
    vizit.insert(start);

    int x;
    while (coada.size())
    {
        x = coada.front();
        coada.pop();
        cout << x << " ";
        for (int i : adiacenta[x])
            if (vizit.find(i) == vizit.end())
            {
                coada.push(i);
                vizit.insert(i);
            }

    }
    cout<<endl;
}
void directedGraph:: DFS(int start)
{
   cout<<"Parcurgere DFS:"<<endl;
    stack<int> stiva;
    stiva.push(start);
    vector<bool> vizit(adiacenta.size(), false);
    vizit[start] = true;
    int x;

    while (stiva.size())
    {
        x = stiva.top();
        cout << x << " ";
        stiva.pop();
        for (int i : adiacenta[x])
            if (!vizit[i])
            {
                stiva.push(i);
                vizit[i] = true;

            }

    }
    cout<<endl;
}

int directedGraph :: twoCycles() //numar cicluri
{
    int res = 0,i;
    for (i = 0; i < adiacenta.size(); i++)
        for (int j : adiacenta[i])
            if (hasEdge(j, i))
                res++;
    return res / 2;
}

int main()
{
    directedGraph g;
    //noduri 0, 1, 2, 3;=>4 noduri
    /*
     muchii:=> 5 muchii
     1-2
     2-1
     1-3
     3-1
     3-0
     start=1
     */
    int n,i,m,s,d,start;
    cout<<"Dati numarul de noduri:";
    cin>>n;
    for(i=0;i<n;i++)
        g.addNode(i);
    cout<<"Dati numarul de muchii:";
    cin>>m;
    cout<<"Dati muchiile: ";
    for(i=0;i<m;i++)
    {
        cin>>s;
        cin>>d;
        g.addEdge(s,d);
    }
    cout<<"Dati nodul de start: ";
    cin>>start;

    g.DFS(start);
    g.BFS(start);
    cout<<"Cate 2Cicluri sunt in graf? : ";
    cout << g.twoCycles();
}
