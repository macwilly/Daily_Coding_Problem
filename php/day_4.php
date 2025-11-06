<?php
/*
--- Question ---
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/

/*
--- My Solution ---
- Uppon research 0 is not negative or positive so if all numbers are negative 1 will be next number.
*/

//$arr = [-1, -2, -10];
$arr = [45,49,13,34,41,4,17,30,44,19];
$lowestInArr      = null;
$lowestNotPresent = null;

// Regular sort array from lowest to highest.
sort($arr);

//get the lowest positive int
for ($i = 0; $i < count($arr); $i++) {
    while(is_null($lowestInArr)){
        if($arr[$i] < 0) {
            break;
        } else {
            $lowestInArr = $arr[$i];
        }
    }
}

//checking to see if $lowestInArr is still null meaning all ints were negative
// setting
if(is_null($lowestInArr)){
    $lowestInArr = 0;
    $lowestNotPresent = 1;
}

//find the lowest not in the array
while (is_null($lowestNotPresent)) {
    // Increment the lowest present by 1
    $upOne = $lowestInArr++;

    //check to see if its in the array
    if(!in_array($upOne, $arr)){
        $lowestNotPresent = $upOne;
    }
}

echo "Lowest not present " . $lowestNotPresent . "\n";