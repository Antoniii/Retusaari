import kotlin.math.*

fun dfac(n: Int): Int {
    return if ((n == 0) or (n == 1))
        1
    else
        n * dfac(n-2) // fac(n-1)
}

//println(fac(10))

println(dfac(5))