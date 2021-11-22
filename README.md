# coding-notes

# test
<button name="button" onClick='(function() {document.getElementsByClassName("moreDetails").click()})();'>button</button>
<details class="moreDetails">


```sql
select *
FROM sdkf
WHERE lskdjf
```

</details>

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
<a href='#/' id='expAll' class='exp'>Expand All</a>

<details>Hello World
  <summary>summary</summary>lost</details>
<details>another
  <summary>good night moon</summary>find me</details>
