#include <stdio.h>
#include <math.h>
#include <string.h>

void f(char * str){
  // a -> b
  int i = 0;
  while (str[i] != '\0') {
    if (str[i] == 'a') {
      str[i] = 'b';
    }
    i++;
  }
}


int main(){
  char str[100];
  scanf("%s", str);
  printf("input = %s\n", str);
  f(str);
  printf("output = %s\n", str);
}
