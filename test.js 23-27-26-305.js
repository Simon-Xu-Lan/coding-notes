function wordCount(myString) {
  // Placeholder object for tracking word frequency
  var wordFrequency = {};
  
  // Your solution goes here!
  var wordList = myString.split(" ");
  wordList.forEach(word => {
    if (word in wordFrequency) {
      wordFrequency[word]++
    } else {
      wordFrequency[word] = 1
    }
  })

  return wordFrequency
}

var strr = "to be or not to be that is the question"

var result = wordCount(strr)

console.log(result)