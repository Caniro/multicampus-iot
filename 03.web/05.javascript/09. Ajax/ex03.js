// 날씨 받아오기 - async, await

function showWeather(w) {
  const main = w.main;
  const url_img = `http://api.openweathermap.org/img/w/${w.weather[0].icon}.png`;
  const template = `
    <h3>${w.name}</h3>
    <p>
      <img src="${url_img}" />
      ${w.weather[0].description}
    </p>
    <p>기온 : ${main.temp}</p>
    <p>습도 : ${main.humidity}</p>
    <p>풍속 : ${w.wind.speed} m/s, 풍향 : ${w.wind.deg}°</p>
  `;
  
  const weather = document.getElementById('weather');
  weather.innerHTML = template;
}

const getWeather = async (city) => {
  const url = 'http://api.openweathermap.org/data/2.5/weather';
  const lang = 'kr';
  const units = "metric";
  const params = { q: city, appid: weather_key, lang, units };

  try {
    const res = await axios.get(url, { params });
    showWeather(res.data);
  } catch(e) {
    console.log(e);
  }
};

const getCityWeather = e => {
  console.log(e.target);
  const city = e.target.dataset.name;
  getWeather(city);
};

document.addEventListener('DOMContentLoaded', function() {
  // 이 코드는 비효율적. DOM이 많아지면 브라우저가 느려질 수 있음
  // let cities = document.getElementsByClassName('city');
  // for (let i = 0; i < cities.length; ++i) {
  //   cities[i].onclick = getWeather;
  // }
  document.getElementById('cities').onclick = getCityWeather; // 이벤트 위임(delegation)
}, false);
