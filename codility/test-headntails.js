// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

/**
 * Jaziel Lopez
 * <juan.jaziel@gmail.com>
 *
 *  Write a function that given a zero-indexed array consisting of n integers
 *  representing the coins returns the minimuim number of coins that must be reversed.
 *
 *  Consecutive elements of array represent consecutive coins and contain only a 0 (heads) or a 1 (tails)
 *
 *  For example, given array [1,0,0,1,0,0]
 *  there are four coins showing heads
 *  there are two coins showing tails
 *
 *  The function should return 2 as after reversing two coins (in position 0 and 3) all the coins will be showing
 *  the same face (heads).
 **/

function solution(elements) {

    // write your code in JavaScript (Node.js 6.4.0)

    var

        i,

        value,

        counts = {

            '0' : 0,

            '1' : 0

        };

    if(!elements) {

        throw new Error('Expected array none provided');
    }


    if( elements.length === 0 || elements.length > 100) {

        throw new Error('Expected elements should within the range [1, 100]');
    }

    for(i in elements){

        value = elements[i];

        counts[value] ++;
    }

    return counts['0'] > counts['1'] ?

        counts['1'] : counts['0'];

}

console.log(solution([1,0,0,0,1,0,0]));
