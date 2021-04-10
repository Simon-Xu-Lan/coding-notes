# d3-tips documentation

- https://github.com/Caged/d3-tip

# d3noob Website - Adding Axis Labels to D3.js Graph

- http://www.d3noob.org/2012/12/adding-axis-labels-to-d3js-graph.html

# Transition

## Take a few minutes to examine this [example using D3 transitions](https://bl.ocks.org/d3noob/899a0b2490318a96f9ebd40a5a84e4a7)

- There are three elements of animated transitions in D3:

  1. The selection.

  2. The transition method.

  3. Attributes.

- That is, in order to make a transition, we must first select element(s). We then use the `transition()` method to signal that a transition will take place, followed by specifying specific attributes of the transition, such as duration, movements, or color changes.

## See [example using D3 transitions](https://bl.ocks.org/d3noob/899a0b2490318a96f9ebd40a5a84e4a7)

The first transition involves changing the original position of the circles so that they are off screen, and then transitioning them down to their proper locations after the rest of the chart is created.

- The code for the second transition should be added to the `mouseout`, `click` and `mouseover`.

- See the [D3 Docs on Transitions](https://github.com/d3/d3/blob/master/API.md#transitions-d3-transition) for reference.
