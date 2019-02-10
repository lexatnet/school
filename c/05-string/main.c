#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
  char str[10];
  char sub_str[3];
  int x;
  scanf("%s", str);
  scanf("%d", &x);
  printf("out = %c\n", str[3]);
  printf("len = %ld\n", strlen(str));
  printf("size = %ld\n", sizeof(str));
  for(int i = 0; i < 2; i++) {
    printf("i = %d str[x+i] = %c\n", i, str[x+i]);
    sub_str[i] = str[x+i];
  }
  sub_str[2] = '\0';
  printf("sub_str = %s\n", sub_str);
}
