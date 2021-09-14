// checkbox 값 취득 - name이 동일한 것들을 순회해서 검사

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn').addEventListener('click', function() {
    let result = [];
    let foods = document.getElementsByName('food');
  
    foods.forEach(food => {
      if (food.checked) {
        result.push(food.value);
      }
    });
    alert(result.toString());
  }, false);
}, false);
