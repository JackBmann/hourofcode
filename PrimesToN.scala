object PrimesToN {
  def main(args: Array[String]): Unit = {
    val n = scala.io.StdIn.readInt()
    val primesToN = getPrimesToN(n)
    for (i <- 0 to primesToN.length - 1) {
      println(primesToN(i))
    }
  }

  def getPrimesToN(n: Int) : List[Int] = {
    (2 to n).toList.filter(s=>(2 to scala.math.sqrt(s).toInt).toList.forall(g=>s%g!=0))
  } 
}



