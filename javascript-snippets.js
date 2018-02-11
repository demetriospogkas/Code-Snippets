// D3 - Get an HTML element's attributes
d3.select({element})
    .node()
    .attributes
    .{attribute}
    .value

// JS - Get the last element of an array
{array}[{array}.length - 1]

//JS - Slice an array
{array}
  .slice(1, ({array}.length)) // Slice array from second to last element

{array}
  .slice(0, ({array}.length - 1)) // Slice array from first to second to last element

{array}
  .slice(1, -1) // Slice array from second to second to last element