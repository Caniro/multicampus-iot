// select 값 설정

document.addEventListener('DOMContentLoaded', function() {
  const setListValue = function(name, value) {
    let opts = document.getElementById(name);

    for(let i = 0; i < opts.length; ++i) {
      let opt = opts.item(i);
      if (value.indexOf(opt.value) > -1) {
        opt.selected = true;
      }
    }
  };

  setListValue('food', ['만두', '불고기']);
}, false);
