// 1초 간격으로 날짜, 시간 출력

document.addEventListener('DOMContentLoaded', function() {
  const date = new Date().toLocaleDateString();
  document.getElementById('date').innerHTML = '날짜 : ' + date;

  const clock = document.getElementById('time');
  setInterval(() => {
    const time = new Date().toLocaleTimeString();
    clock.innerHTML = '시간 : ' + time;
  }, 1000);
}, false);
