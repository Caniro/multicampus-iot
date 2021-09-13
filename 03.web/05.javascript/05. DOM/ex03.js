// name 속성으로 선택
let current = new Date();
let time = document.getElementsByName('time');

time[0].value = current.toLocaleTimeString();
