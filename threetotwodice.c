#include <stdio.h>

int tri(int n) { return n*(n+1)/2; }
int tet(int n) { return n*(n+1)*(n+2)/6; }
void sort2(int *x, int *y)
{
  int tmp;
  if ((*x) > (*y)) { tmp = *x; *x = *y; *y = tmp; }
}
void sort3(int *x, int *y, int *z)
{
  sort2(x, y);
  sort2(y, z);
  sort2(x, y);
}
int num(int i, int j, int k)
{
  sort3(&i, &j, &k);
  if ((i == j) && (j == k)) { return 0; }
  if (j == k) { j = i; }
  return tet(5-i) + tri(5-j) + 5-k + 2;
}
void topair(int i, int j, int k, int* a, int* b)
{
  int m;
  m = num(i, j, k);
  *a = m/6 + 1;
  *b = m%6 + 1;
}

int main()
{
  int i, j, k, a, b;
  int c[6][6];

  for(a=0; a<=5; a++) {
    for(b=0; b<=5; b++) {
      c[a][b] = 0;
    }
  }
  for(i=1; i<=6; i++) {
      for(j=1; j<=6; j++) {
          for(k=1; k<=6; k++) {
            topair(i, j, k, &a, &b);
            c[a-1][b-1]++;
          }
      }
  }
  for(a=0; a<=5; a++) {
    for(b=0; b<=5; b++) {
      printf("%d ", c[a][b]);
    }
    printf("\n");
  }
}
