// checkboux 값 설정

document.addEventListener('DOMContentLoaded', function() {
  const setCheckValue = function(name, value_list) { // 체크하려는 값들을 배열로 받음
    document.getElementsByName(name).forEach(elem => {
      if (value_list.indexOf(elem.value) > -1) {
        elem.checked = true;
      }
    })
  };

  setTimeout(() => {setCheckValue('food', ['만두', '불고기']);}, 2000);
}, false);
