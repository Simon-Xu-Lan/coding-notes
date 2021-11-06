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


# This
```js
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>This Example</title>
</head>
<body>

  <h1>Make sure to view the console to see the action!</h1>

  <script type="text/javascript">

    // EXAMPLE ONE:
    // --------------------------------------------------
    // What is "this" going to print?

    // Answer: "WINDOW"
    // Explanation: In this case "this" references the window (since it isn't inside of any object).
    console.log(this);


    // EXAMPLE TWO:
    // --------------------------------------------------
    // What is "this" going to print?

    // Answer: "WINDOW"
    // Explanation: Again, in this case 'this' references the window, since it isn't tied to any specific object.
    function myFunction() {
      console.log(this);
    }
    myFunction();

    // EXAMPLE THREE (IMPORTANT):
    // --------------------------------------------------
    // What is "someObj.say()" going to print?

    // Answer: "Red Hat"
    // Explanation: "someObj.say()" will print "this.name", which in this case references the "someObj" object.
    var someObj = {
      name: "Red Hat",
      say: function() {
        console.log(this.name);
      }
    };
    someObj.say();


    // EXAMPLE FOUR (BONUS, TRICKY!):
    // --------------------------------------------------
    // What is "myObj.yell()" going to print? Why?

    // Answer: "Object > name: 'Star Powerup'"
    // Explanation: Very tricky one!
    // In this case, one would think the output should be: "Object > name: 'Blue Shell".
    // However, in this case, the keyword: "this" changes meaning mid-way through the function call.
    // At first "this" refers to "myObj", but as we go inside the "changeName" function "this" means "Window".
    // The takeaway here is that one needs to be ultra careful of one's use of the keyword: "this".
    var myObj = {
      name: "",
      yell: function() {
        this.name = "Star Powerup";

        var changeName = function(newName) {
          this.name = newName;
          console.log("`this` refers to the window here, because this nested function loses the myObj scope. console.log(this):");
          console.log(this);
          console.log("so we're setting the name '" + newName + "' on the window. console.log(window.name):");
          console.log(window.name);
          console.log("`window` contains the global scope, so you can log the variable itself. console.log(name):");
          console.log(name);
        };
        changeName("Blue Shell");
        console.log("`this` here refers to myObj, so doesn't show our modifications to window");
        console.log(this);
      }
    };
    myObj.yell();


    // EXAMPLE FIVE (BONUS, TRICKY!):
    // --------------------------------------------------
    // What is "myObj.yell()" going to print? Why?

    // Answer: "Object > name: 'Blue Shell'"
    // Explanation: This example "solves" the issue from the previous bonus.
    // In order to maintain scope throughout the function we created a variable called: "thisObject".
    // This "thisObject" variable latches onto the original "myObj" instance of "this" to preserve state.
    // Now, we can use the object "thisObject" in our "changeName" function to set the new name.
    // Tricky indeed! Don't worry if you don't quite get it. This is more of a theoretical challenge.
    var myObj = {
      name: "",
      yell: function() {

        // Here we make use of the "thisObject" variable to hold the state of "this"
        var thisObject = this;

        this.name = "Star Powerup";
        var changeName = function(newName) {
          thisObject.name = newName;
        };
        changeName("Blue Shell");
        console.log(thisObject);
      }
    };
    myObj.yell();

  </script>
</body>
</html>

```



