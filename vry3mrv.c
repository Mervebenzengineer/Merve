#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct AgacElemani {
    int veri;
    struct AgacElemani *solKisim;
    struct AgacElemani *sagKisim;
} AgacElemani;

AgacElemani* yeniEleman(int sayi) {
    AgacElemani* gecici = (AgacElemani*)malloc(sizeof(AgacElemani));
    gecici->veri = sayi;
    gecici->solKisim = NULL;
    gecici->sagKisim = NULL;
    return gecici;
}

AgacElemani* agacUyesiEkle(AgacElemani* kok, int sayi) {
    if (kok == NULL)
        return yeniEleman(sayi);
    if (sayi < kok->veri)
        kok->solKisim = agacUyesiEkle(kok->solKisim, sayi);
    else
        kok->sagKisim = agacUyesiEkle(kok->sagKisim, sayi);
    return kok;
}

void agaciYazdir(AgacElemani* kok) {
    if (kok != NULL) {
        agaciYazdir(kok->solKisim);
        printf("%d ", kok->veri);
        agaciYazdir(kok->sagKisim);
    }
}

void istatistikTopla(AgacElemani* kok, int* toplam, int* adet, int* cift, int* tek) {
    if (kok == NULL) return;
    *toplam += kok->veri;
    (*adet)++;
    if (kok->veri % 2 == 0) (*cift)++;
    else (*tek)++;
    istatistikTopla(kok->solKisim, toplam, adet, cift, tek);
    istatistikTopla(kok->sagKisim, toplam, adet, cift, tek);
}

int yaprakSayisi(AgacElemani* kok) {
    if (kok == NULL) return 0;
    if (kok->solKisim == NULL && kok->sagKisim == NULL)
        return 1;
    return yaprakSayisi(kok->solKisim) + yaprakSayisi(kok->sagKisim);
}

int main() {
    srand(time(NULL));
    AgacElemani* basDugum = NULL;
    int i, rastgeleDeger;
    
    printf("Ekleme islemi basliyor...\n");
    for (i = 0; i < 40; i++) {
        rastgeleDeger = 1 + rand() % 20;
        basDugum = agacUyesiEkle(basDugum, rastgeleDeger);
        printf("%d ", rastgeleDeger);
    }

    printf("\n\nAgac (Inorder Dolasma): ");
    agaciYazdir(basDugum);

    int toplam = 0, adet = 0, cift = 0, tek = 0;
    istatistikTopla(basDugum, &toplam, &adet, &cift, &tek);
    double ortalama = (double)toplam / adet;

    int yaprak = yaprakSayisi(basDugum);

    printf("\n\nToplam dugum sayisi: %d", adet);
    printf("\nAritmetik ortalama: %.2f", ortalama);
    printf("\nCift sayi adedi: %d", cift);
    printf("\nTek sayi adedi: %d", tek);
    printf("\nYaprak dugum sayisi: %d\n", yaprak);

    return 0;
}
