// 날씨 받아오기 - async, await

function showWeather(w) {
  const main = w.main;
  const url_img = `http://api.openweathermap.org/img/w/${w.weather[0].icon}.png`;
  const template = `
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

const getWeather = async () => {
  const url = 'http://api.openweathermap.org/data/2.5/weather';
  const city = 'Seoul';
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

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('btn').onclick = getWeather;
}, false);
