/*
 Computer Science Education Week, 2018
 University of Dallas
 Learn Scala!
 Yeabkal Wubshit
 */
object Fibonacci {
  def main(args: Array[String]): Unit = {
  	// Prompt user to enter the desired amount of Fibonacci numbers to print.
  	println("Enter the amount of Fibonacci Numbers you want to print")

  	// Take user input for the amount of Fibonacci numbers to print.
  	val SizeOfFibonacciNumbers = scala.io.StdIn.readInt()

  	// Store the Fibonacci numbers in an array by calling the function
    // returning an array of Fibonacci sequence.
    val FibonacciNumbers = getFibonacciNumbers(SizeOfFibonacciNumbers)

    // Print the elements of the array containing the Fibonacci numbers.
    for (i <- 0 to SizeOfFibonacciNumbers-1) {
    	println(i + ": " + FibonacciNumbers(i))
    }
  }

  /*
  n - number of Fibonacci numbers to calculate
  returns an array containing 'n' Fibonacci numbers.
  */
  def getFibonacciNumbers(n: Int) : Array[Int] = {
  	// Define the 1st and 2nd Fibonacci numbers.
  	val Fib_1_2 = 1
  	// Array to 'n' store Fibonacci numbers.
  	var fibNos = new Array[Int] (n)
  	// Set the first Fibonacci number.
  	fibNos(0) = Fib_1_2
  	if(n > 1) { 
  		// Set the second Fibonacci number if the desired
  		// size is at least 2.
  		fibNos(1) = Fib_1_2
  	}
  	// Fill the array of Fibonacci numbers using the formula:
  	// fib(n) = fib(n-1) + fib(n-2)
  	for(i <- 2 to n-1) {
  		fibNos(i) = fibNos(i-1) + fibNos(i-2)
  	}
  	// Return the array of Fibonacci numbers
  	fibNos
  } 
}
