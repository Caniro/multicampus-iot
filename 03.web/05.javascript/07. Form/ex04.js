// radio 값 취득

document.addEventListener('DOMContentLoaded', function() {
  const getRadioValue = function(name) {
    let result = '';

    document.getElementsByName(name).forEach(elem => {
      if (elem.checked) {
        result = elem.value;
        return ;
      }
    });

    return result ? result : '선택 안함';
  };

  document.getElementById('btn').addEventListener('click', function() {
    window.alert(getRadioValue('food'));
  }, false);
}, false);
