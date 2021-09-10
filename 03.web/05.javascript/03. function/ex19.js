// 고차 함수 (함수의 매개변수나 리턴값으로 함수를 전달)
function arrayWalk(data, f) {
  for (var key in data) {
    f(data[key], key, data);
  }
}

function showElement(value, key) {
  console.log(key + '： ' + value);
}

function showElement2(value, key) {
  console.log(`arr[${key}] = ${value}`);
}

function showElement3(value) {
  console.log(value);
}

function showElement4(value, key, arr) {
  console.log(`arr[${key}] = ${value}, [${arr}]`);
}

var ary = [1, 2, 4, 8, 16];
arrayWalk(ary, showElement);
arrayWalk(ary, showElement2);
arrayWalk(ary, showElement3);

// 이거 두개는 같다. forEach가 메서드로 정의되어 있음
arrayWalk(ary, showElement4);
ary.forEach(showElement4);
