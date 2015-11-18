<?php

/**
 * Project Euler: Problem 3
 * Title: Largest prime factor
 * Description: The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143?
 * Author: Jonathan Herbst
 * Last Edited: 11/11/2015
 */

function largest_prime( $number ) {

	$index = 3;

	while( $index * $index < $number ) {

		// If it's a factor
		if( $number % $index === 0 ) {

			$number = $number / $index;
		}

		else {

			// Iterate by 2 since the answer can't be even
			$index += 2;
		}
	}

	// The number that is left over will be the largest prime
	return $number;
}

$original = 600851475143;

echo "The largest prime factor of the number " . $original . " is " . largest_prime( $original );

?>