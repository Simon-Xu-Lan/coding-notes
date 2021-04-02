// Sort the array in descending order
var numArray = [1, 2, 3];
numArray.sort(function compareFunction(firstNum, secondNum) {
  // resulting order is (3, 2, 1)
  return secondNum - firstNum;
});

// Returns [3, 2, 1]
console.log(numArray);

// Sort the array in ascending order
var numArray2 = [3, 2, 1];
numArray2.sort(function compareFunction(firstNum, secondNum) {
  // resulting order is (1, 2, 3)
  return firstNum - secondNum;
});

// Returns [1, 2, 3]
console.log(numArray2);

// Sort the array in ascending order, using an arrow function
var numArray3 = [3, 2, 1];
numArray3.sort((firstNum, secondNum) => firstNum - secondNum);
console.log(numArray3);

// Reverse the array
var numArray4 = [1, 2, 3];
var reversedArray = numArray4.reverse();
console.log(reversedArray);

// An unsorted array
numArray = [9.9, 6.1, 17.1, 22.7, 4.6, 8.7, 7.2];

// Sort the array in descending order and assign the results to a variable
numArray.sort((a, b) => b - a);

console.log(numArray);

// output:
result = [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 4.6];

// Sort the array in ascending order using an arrow function
numArray.sort((a, b) => a - b);
console.log(numArray);
// output:
result = [4.6, 6.1, 7.2, 8.7, 9.9, 17.1, 22.7];
