// id 속성으로 선택
let current = new Date();

let currentDate = document.getElementById('currentDate');
currentDate.textContent = current.toLocaleDateString();

let currentTime = document.getElementById('currentTime');
currentTime.textContent = current.toLocaleTimeString();

document.getElementById('ignoreTag').textContent = 
  '<h3>태그는 이스케이프 처리</h3>';