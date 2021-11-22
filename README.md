# coding-notes

<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
<foreignObject width="100" height="100">
    <div xmlns="http://www.w3.org/1999/xhtml">
        <ul>
            <li>text</li>
        </ul>
        <!-- Other embed HTML element/text into SVG -->
    </div>
</foreignObject>
</svg>



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
