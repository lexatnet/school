#include <stdio.h>

void f(char * str, char * out){
  // a -> b
  int i = 0;
  while (str[i] != '\0') {
    if (str[i] == 'a') {
      out[i] = 'b';
    } else {
      out[i] = str[i];
    }
    i++;
  }
  out[i] = '\0';
}

int main(){
  char str[100];
  char out[100];
  scanf("%s", str);
  printf("input = %s\n", str);
  f(str, out);
  printf("input = %s\noutput = %s\n", str, out);
}
