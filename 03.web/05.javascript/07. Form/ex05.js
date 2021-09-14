// radio 값 설정 (프로퍼티 설정)

document.addEventListener('DOMContentLoaded', function() {
  const setRadioValue = function(name, value) {
    document.getElementsByName(name).forEach(elem => {
      if (elem.value === value) {
        elem.checked = true;
        return ;
      }
    });
  };

  setTimeout(() => {setRadioValue('food', '만두');}, 2000);
}, false);
