// 상황에 따라 다른 값을 갖는 this

console.log("최상위 객체 this:", this);

document.addEventListener('DOMContentLoaded', function() {
  var data = {
    title: 'Java포켓 레퍼런스',
    price: 26800,
    show: function() {
      console.log("show 함수의 this :", this);
      console.log(this.title + ', ' + this.price + '원');
    }
  };
  console.log("document 이벤트 리스너의 this :", this);
  data.show(); // this가 data (호출한 객체)

  document.getElementById('btn').addEventListener(
      'click', data.show, false); // this가 #btn (이벤트 발생처)

  // document.getElementById('btn').addEventListener(
      // 'click', data.show.bind(data), false); // this를 data로 bind
}, false);
