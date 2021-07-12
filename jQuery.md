# $, text(), append(), attr()
```js
    $("#empty-div").html("<h1>Hello friends!</h1>");

    // jQuery alternative to: var newDiv = document.createElement("div");
    var newDiv = $("<div>");

    // jQuery alternative to: newDiv.textContent = "A pleasure to meet you!";
    newDiv.text("A pleasure to meet you!");

    // jQuery alternative to: document.querySelector("#empty-div").appendChild(newDiv);
    $("#empty-div").append(newDiv);

    // If we need to apply some CSS, we can quickly do so, using the jQuery ".attr" method.
    newDiv.attr("class", "fancy");
```

# each()
```js
    //This line of jQuery selects the div with the matching id (#drink-options)
    var drinkDiv = $("#drink-options");

    // Here we loop through our array using the .each() method and append a new div with each iteration
    $.each(drinkList, function(i, drink) {
      drinkDiv.append("<div>" + drink + "</div>");
    });

```


# document.ready
- This "document.ready" code isn't necessary in this example... but is useful to become familiar with.
- "document.ready" makes sure that our JavaScript doesn't get run until the HTML document is finished loading.
# .$("#id|.class|element").on("action", function(){});
```js
// This "document.ready" code isn't necessary in this example... but is useful to become familiar with.
    // "document.ready" makes sure that our JavaScript doesn't get run until the HTML document is finished loading.
    $(document).ready(function() {

      // Here we use jQuery to select the header with "click-me" as its ID.
      // Notice I have the #click-me, click, and then the function
      // So $("#id|.class|element").on("action", function(){});
      // And so whenever it is clicked...
      $("#click-me").on("click", function() {
        alert("I've been clicked!");
      });

    });
```

# prepend
- the prepend() method inserts specified contend at the beginning of the selected element
```js
// Insert content at the beginning of all <p> elements:
$("button").click(function(){
  $("p").prepend("<b>Prepended text</b>");
});
```

# before
- The before() method inserts specified content in front of (before) the selected elements.
```js
// Insert content before each <p> element:
$("button").click(function(){
  $("p").before("<p>Hello world!</p>");
});
```

