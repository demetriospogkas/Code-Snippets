// JS - Get the last element of an array
{array}[{array}.length - 1]

//JS - Slice an array
{array}
  .slice(1, ({array}.length)) // Slice array from second to last element

{array}
  .slice(0, ({array}.length - 1)) // Slice array from first to second to last element

{array}
  .slice(1, -1) // Slice array from second to second to last element

// JS - Create a new array from elements/objects of another array
{array}.map(function(element, index){
  return element.{value}
})

// JS - Delay the execution of a function
setTimeout(function(){
  {function({element})}
},{miliseconds})

// JS - Repeatedly execute a function
setInterval(function(){
  {function({element})}
},{miliseconds})