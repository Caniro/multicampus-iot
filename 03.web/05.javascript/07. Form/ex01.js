// input의 값(value) 취득

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn').addEventListener('click', function() {
    let name = document.getElementById('name');
    console.log(name.value);
    name.value = '정시온';
  }, false);
}, false);
