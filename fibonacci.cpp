#include <iostream>
#include <fstream>

void writeNumbersToFile(int numbers[], int numOfNums, char *fileName) {
  std::ofstream myfile;
  myfile.open (fileName);
  for(int i = 0; i < numOfNums; i++){
    myfile << numbers[i];
    myfile << "\n";
  }
  myfile.close();
}

int *fibonacciSequence(int numOfNums){
  int *sequence = (int*) malloc(numOfNums * sizeof(int));
  if(numOfNums == 0){
    return sequence;
  }
  sequence[0] = 1;
  if(numOfNums == 1){
    return sequence;
  }
  sequence[1] = 1;
  for(int i = 2; i < numOfNums; i++){
    sequence[i] = sequence[i - 1] + sequence[i - 2];
  }
  return sequence;
}

int fibonacci(int index) {
  int previous = 1;
  int current = 1;
   // since previous and current take up indicies 1 and 2,
   // we start at index 2
  int i = 2;
  while(i < index){
    int temp = current;
    current = current + previous;
    previous = temp;
    i++;
  }
  return current;
}

int main2() {
  std::cout << "Enter your fibonacci index:\n";
  int index;
  std::cin >> index;
  int fibonacciNumber = fibonacci(index);
  std::cout << fibonacciNumber;
  return 0;
}

int main() {
  std::cout << "Enter your fibonacci index:\n";
  int index;
  std::cin >> index;
  char fileName[] = "fibonacciNumbers.txt";
  int *sequence = fibonacciSequence(index);
  writeNumbersToFile(sequence, index, fileName);
  free(sequence);
  std::cout << index;
  std::cout << " fibonacci numbers have been written to ";
  std::cout << fileName;
  return 0;
}
