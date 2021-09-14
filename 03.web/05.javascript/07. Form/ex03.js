// 단일 체크 상자

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn').addEventListener('click', function() {
    let onoff = document.getElementById('onoff');

    if (onoff.checked) {
      console.log(onoff.value);
    } else {
      console.log('체크되지 않았어요');
    }
  }, false);
}, false);
