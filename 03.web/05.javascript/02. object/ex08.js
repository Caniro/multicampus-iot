// Array - map

let data = [1, 2, 3, 4, 5];
let result = data.map(function (value, index, array) {
  return value * value;
});
console.log(result);

let result2 = data.map(value => value * value);
console.log(result2);
