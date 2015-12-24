<?php

/**
 * Project Euler: Problem 11
 * Title: Largest product in a grid
 * Description: In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
 * 
 * The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
 * 
 * What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, 
 * or diagonally) in the 20×20 grid?
 * Author: Jonathan Herbst
 * Last Edited: 24/12/2015
 */

$product = 0;
$result = 0;
$grid = array();

// Grid content
$grid[0] = array( 08, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 08 );
$grid[1] = array( 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00 );
$grid[2] = array( 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65 );
$grid[3] = array( 52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91 );
$grid[4] = array( 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80 );
$grid[5] = array( 24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50 );
$grid[6] = array( 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70 );
$grid[7] = array( 67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 08, 40, 91, 66, 49, 94, 21 );
$grid[8] = array( 24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72 );
$grid[9] = array( 21, 36, 23, 09, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95 );
$grid[10] = array( 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 09, 53, 56, 92 );
$grid[11] = array( 16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57 );
$grid[12] = array( 86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58 );
$grid[13] = array( 19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40 );
$grid[14] = array( 04, 52, 08, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66 );
$grid[15] = array( 88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69 );
$grid[16] = array( 04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 08, 46, 29, 32, 40, 62, 76, 36 );
$grid[17] = array( 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16 );
$grid[18] = array( 20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54 );
$grid[19] = array( 01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48 );

/**
 * Check the current product calculation to see if it's larger than what we've already got
 * 
 * @param $new     int The new value to check
 * @param $current int The current largest product we've tracked
 *
 * @return int $new if larger, else the $current value
 */
function check_result( $new, $current ) {

	if( $new > $current ) {

		return $new;
	}

	return $current;
}

// Horizontal

// For each grid row (going down)
for( $hy = 0; $hy < 20; $hy++ ) {

	// For each item in the current row, with padding from the right (-4)
	for( $hx = 0; $hx < 17; $hx++ ) {

		// Check the current position's value and the three to the right
		$result = $grid[$hy][$hx] * $grid[$hy][$hx + 1] * $grid[$hy][$hx + 2] * $grid[$hy][$hx + 3];

		// Check the new value against the current one
		$product = check_result( $result, $product );
	}		
}

// Vertical

// For each grid column
for( $vx = 0; $vx < 20; $vx++ ) {

	// For each item in the column, with bottom padding included (-4)
	for( $vy = 0; $vy < 17; $vy++ ) {

		// Check the current position's value and the three tiles below
		$result = $grid[$vy][$vx] * $grid[$vy + 1][$vx] * $grid[$vy + 2][$vx] * $grid[$vy + 3][$vx];

		// Check the new value against the current one
		$product = check_result( $result, $product );
	}
}

// Diagonal (left-right)

// For each row going left to right
for( $drx = 0; $drx < 17; $drx++ ) {

	// For each column going top to bottom
	for( $dry = 0; $dry < 17; $dry++ ) {

		// Check the current position and three to the bottom right (ie [0,0], [1,1], [2,2], [3,3])
		$result = $grid[$drx][$dry] * $grid[$drx + 1][$dry + 1] * $grid[$drx + 2][$dry + 2] * $grid[$drx + 3][$dry + 3];

		// Check the new value against the current one
		$product = check_result( $result, $product );
	}
}

// Diagonal (right-left)

// For each row going right to left
for( $dlx = 19; $dlx > 2; $dlx-- ) {

	// For each column going top to bottom
	for( $dly = 0; $dly < 17; $dly++ ) {

		// Check the current position and three to the bottom left (ie [3,0], [2,1], [1,2], [0,3])
		$result = $grid[$dlx][$dly] * $grid[$dlx - 1][$dly + 1] * $grid[$dlx - 2][$dly + 2] * $grid[$dlx - 3][$dly + 3];

		// Check the new value against the current one
		$product = check_result( $result, $product );
	}
}

echo 'The greatest product of four adjacent numbers in the same direction in the 20x20 grid is ' . $product;

?>