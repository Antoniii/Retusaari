//fun fizzBuzz(i: Int) = when {
//    i % 15 == 0 -> "FizzBuzz"
//    i % 3 == 0 -> "Fizz"
//    i % 5 == 0 -> "Buzz"
//    else -> "$i"
//}
//
//for (i in 1..27) {
//    print(fizzBuzz(i))
//    print(' ')
//}



var numbers: ArrayList<Int> = arrayListOf(2,5,1,8,7,3,4,6,10,9)

println(numbers)

var swap: Boolean = true

while (swap) {
    swap = false

    for (i in 0 until numbers.size-1) {
        if (numbers[i] > numbers[i+1]) {
            swap=true
            val temp: Int = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
        }
    }
}

println(numbers)