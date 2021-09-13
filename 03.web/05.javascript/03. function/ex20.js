// 스코프 체인 - 내부 함수
let x = 'Global';

function outerFunc() {
  let y = 'Local Outer';
  
  function innerFunc() {
    let z = 'Local Inner';
    console.log(z);
    console.log(y);
    console.log(x);
  }

  innerFunc();
};

outerFunc();
// innerFunc(); // 에러
