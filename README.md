# coding-notes

<h1>The onclick Event</h1>

<p>The onclick event is used to trigger a function when an element is clicked on.</p>

<p>Click the button to trigger a function that will output "Hello World" in a p element with id="demo".</p>

<button onclick="myFunction()">Click me</button>

<p id="demo"></p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}
</script>



=======================

<script src="http://code.jquery.com/jquery-1.4.2.min.js"></script>
<script>
...do stuff...
</script>



<script>
// Reference the toggle link
var xa = document.getElementById('expAll');

// Register link on click event
xa.addEventListener('click', function(e) {

  /* Toggle the two classes that represent "state"
  || determined when link is clicked
  */
  e.target.classList.toggle('exp');
  e.target.classList.toggle('col');

  // Collect all <details> into a NodeList
  var details = document.querySelectorAll('details');

  /* Convert NodeList into an array then iterate
  || throught it...
  */
  Array.from(details).forEach(function(obj, idx) {

    /* If the link has the class .exp...
    || make each <detail>'s open attribute true
    */
    if (e.target.classList.contains('exp')) {
      obj.open = true;
      // Otherwise make it false
    } else {
      obj.open = false;
    }

  });

}, false);
  
</script>
  
<a href='#/' id='expAll' class='exp'>Expand All</a>

<details>Hello World
  <summary>summary</summary>lost</details>
<details>another
  <summary>good night moon</summary>find me</details>
