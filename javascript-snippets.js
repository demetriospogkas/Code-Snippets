// JS - Get the last element of an array
{array}[{array}.length - 1]

//JS - Slice an array
{array}
  .slice(1, ({array}.length)) // Slice array from second to last element

{array}
  .slice(0, ({array}.length - 1)) // Slice array from first to second to last element

{array}
  .slice(1, -1) // Slice array from second to second to last element

// Create a new array from elements/objects of another array
{array}.map(function(element, index){
  return element.{value}
})