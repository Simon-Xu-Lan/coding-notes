# Position

## Static Position:

- This is default value
- HTML elements are positioned static by default.
- Static positioned elements are not affected by the top, bottom, left, and right properties.
- An element with position: static;
  - is not positioned in any special way;
  - it is always positioned according to the normal flow of the page:

## Relative Position:

- sets boxes relative to its original location
- Setting the top, right, bottom, and left properties of a relatively-positioned element
  - will cause it to be adjusted away from its normal position.
  - Other content will not be adjusted to fit into any gap left by the element.

## Absolute Position:

- anchors element to the first element (overall box)
- The element is positionecd absolutely to its first positioned parenet
- An element with position: absolute; is positioned relative to the nearest positioned ancestor
- However; if an absolute positioned element has no positioned ancestors, it uses the document body, and moves along with page scrolling.

## Sticky Position:

- the element is positioned based on the user's scroll position.

## Fixed Position:

- the element is positioned related to the browser window.
- An element with position: fixed; is positioned relative to the viewport
  - which means it always stays in the same place even if the page is scrolled

## Overlapping Elements

- Z-Index:
  - let's us position elements on top of each other (the z-axis controls depth position)

## font

- https://www.udemy.com/course/100-days-of-code/learn/lecture/22372332#overview
- https://fonts.google.com

# CSS Link Order

- CSS styles are applied in the order they are linked in your HTML code.
  - https://www.udemy.com/course/100-days-of-code/learn/lecture/22372342#overview

# icon resources

- https://fontawesome.com
- https://www.udemy.com/course/100-days-of-code/learn/lecture/22372356#overview

# rotate image

```css
.title-img {
  width: 60%;
  transform: rotate(25deg);
}
```

# make text less obvious -- grayish it

```css
p {
  color: #8f8f8f;
}
```

# make image to be a circle

```css
img {
  border-radius: 100%;
}
```

# Bootstrap tool

- https://bootswatch.com/

# Bootstrap Carousel

- https://www.udemy.com/course/100-days-of-code/learn/lecture/22372386#overview

# Bootsnipp: Bootstrap components exmple

- https://bootsnipp.com/

# CSS Z-index and Stacking Order

- https://www.udemy.com/course/100-days-of-code/learn/lecture/22372394#overview

# CSS-Media Query Breakpoints

- make it responsive
- https://www.udemy.com/course/100-days-of-code/learn/lecture/22372402#overview

# Combine selector

https://www.udemy.com/course/100-days-of-code/learn/lecture/22372448#overview

1.  Multiple Selector

- selector1, selector2 { ... }

```css
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: 'Monstserrat-Bold';
}

h1,
p {
  color: red;
}
```

2. Hierarchical Selectors

- Selector1 selector2 {...}
- selector2 is a child of selector1

# Selector Priority

- https://www.udemy.com/course/100-days-of-code/learn/lecture/22372458#overview

- inline style > id > class > html tag
- below > top
- avoid inline style if possible
