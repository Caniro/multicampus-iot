// Array - filter

let data = [4, 9, 16, 25];
let odd_num = data.filter(function(value, index, array) {
  return (value % 2 === 1);
});
console.log(odd_num);

let even_num = data.filter(value => (value % 2 === 0));
console.log(even_num);
