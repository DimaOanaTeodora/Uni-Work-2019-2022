#include <iostream>

using namespace std;

struct arbore
{
	int info;
	arbore* stang, * drept;
} *radacina;
void insert(int val)
{
	arbore* aux = radacina;
	arbore* last = aux;

	while (aux)
	{
		if (val < aux->info)
		{
			last = aux;
			aux = aux->stang;
		}
		else if (val > aux->info)
		{
			last = aux;
			aux = aux->drept;
		}
	}
	arbore* p = new arbore();
	p->info = val;
	if (radacina == 0)
	{
		radacina = p;
		return;
	}
	if (last->info < val)
	{
		last->drept = p;
	}
	else
	{
		last->stang = p;
	}
}

void searchValuesBetween(arbore* nod, int k1, int k2)
{
	if (nod == nullptr)
		return;

	if (nod->info > k1)
	{
		searchValuesBetween(nod->stang, k1, k2);
	}
	if (k1 <= nod->info && k2 >= nod->info)
	{
		cout << nod->info << " ";
	}

	if (nod->info < k2)
	{
		searchValuesBetween(nod->drept, k1, k2);
	}
}
void SRD(arbore* aux)
{
	if (aux)
	{
		SRD(aux->stang);
		cout << aux->info << " ";
		SRD(aux->drept);
	}
}

int main()
{
	int values[9] = { 6, 4, 9, 2, 1, 5, 3, 7, 8 };
	int k1, k2;
	for (int i = 0; i < 9; i++)
		insert(values[i]);
	// SRD(radacina);
	k1 = 3;
	k2 = 7;
	searchValuesBetween(radacina, k1, k2);
}