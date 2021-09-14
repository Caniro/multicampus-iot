// 마우스 정보 취득

document.addEventListener('DOMContentLoaded', function() {
  let main = document.getElementById('main');

  main.addEventListener('mousemove', function(e) {
  msg = `screen (${e.screenX}, ${e.screenY}) <br />` +
        `page (${e.pageX}, ${e.pageY}) <br />` + 
        `client (${e.clientX}, ${e.clientY}) <br />` + 
        `offset (${e.offsetX}, ${e.offsetY}) <br />`;
  document.getElementById('desc').innerHTML = msg;
  }, false);
}, false);
