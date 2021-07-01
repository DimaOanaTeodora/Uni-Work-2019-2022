#include <iostream>
using namespace std;

struct arbore
{
	int info;
	arbore* stang, * drept;
};
arbore *radacina;

void insert(int val)
{
	
	arbore* aux, * u, * nou;
	aux = radacina;
	u = aux;
	nou = new arbore();

	while (aux != NULL)
		if (val != aux->info)
		{
			u = aux;
			if (val < aux->info)
				aux = aux->stang;
			else 
				aux = aux->drept;
		
		}
	
	nou->info = val;
	if (radacina == NULL)
	{
		radacina = nou;
		return;
	}
	else
	
	{
		if (u->info < val)
			u->drept = nou;
		
		else
			u->stang = nou;
		
	}
	
		
}

void interval(arbore* nou, int k1, int k2)
{
	
	if (nou == nullptr)
		return;
	else
	{
		if (k1 < nou->info && k2 > nou->info)
			cout << nou->info << " ";

		if (nou->info > k1)
			interval(nou->stang, k1, k2);

		if (nou->info < k2)
			interval(nou->drept, k1, k2);
	}
	
	
}


int main()
{
	int v [8]= { 2, 3, 7, 6, 1, 5, 4, 9 }, k1, k2;
	int i, n=8;
	//k1 = 2;
	//k2 = 6;
	cout << "dati k1= ";
	cin >> k1;
	cout << "dati k2= ";
	cin >> k2;
	
	for (i = 0; i < n; i++)
		insert(v[i]);
	interval (radacina, k1, k2);
}