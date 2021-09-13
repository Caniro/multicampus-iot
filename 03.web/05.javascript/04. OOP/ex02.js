// this

let data = 'Global data';
let obj1 = { data: 'obj1 data' };
let obj2 = { data: 'obj2 data' };

function hoge() {
  console.log('this : ', this);
  console.log(this.data);
}

hoge();

// .call() : 호출 함수의 this 값을 매개변수로 설정
hoge.call(null); // this = top level 객체
hoge.call(obj1); // this = obj1
hoge.call(obj2);
