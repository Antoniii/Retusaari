//fun max(a: Int, b: Int): Int {
//    return if (a > b) a else b
//}
//
//println(max(1, 20))

fun fib(n: Int): Int {
    return if ((n == 0) or (n == 1))
        1
    else
        fib(n-2) + fib(n-1)
}

println(fib(34))