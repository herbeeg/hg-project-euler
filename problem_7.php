<?php

/**
 * Problem 7: Project Euler
 * Title: 10001st prime
 * Description: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 * What is the 10 001st prime number?
 * Author: Jonathan Herbst
 * Last Edited: 10/11/2015
 */

$count = 0;
$max = 10001;

$check = 1;
$prime_num = 0;

while( $count < $max ) {

	if( is_prime( $check ) ) {

		$count++;
		$prime_num = $check;
	}

	$check += 2;
}

function is_prime( $number ) {

	$index = 3;

	if( $number === 2 || $number === 3 ) {

		return true;
	}

	while ( $index < $number ) {

		if( $number % $index === 0 ) {

			return false;
		}

		$index += 2;
	}

	return true;
}

echo "The 10,001st prime number is " . $prime_num;

?>