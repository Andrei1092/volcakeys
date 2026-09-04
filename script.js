async function fetchWeather() {
    const tempEl = document.getElementById('temperature');
    const conditionEl = document.getElementById('condition');
    const humidityEl = document.getElementById('humidity');
    const windEl = document.getElementById('wind');
    const feelsLikeEl = document.getElementById('feels-like');
    const dateEl = document.getElementById('date');

    // Установка текущей даты
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    dateEl.innerText = new Date().toLocaleDateString('ru-RU', options);

    try {
        // Координаты Тюмени: 57.1522, 65.5272
        const response = await fetch('https://api.open-meteo.com/v1/forecast?latitude=57.1522&longitude=65.5272&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m');
        const data = await response.json();
        
        const current = data.current;
        tempEl.innerText = Math.round(current.temperature_2m);
        humidityEl.innerText = current.relative_humidity_2m + '%';
        windEl.innerText = current.wind_speed_10m + ' м/с';
        feelsLikeEl.innerText = Math.round(current.apparent_temperature) + '°C';
        
        conditionEl.innerText = getWeatherDescription(current.weather_code);
    } catch (error) {
        conditionEl.innerText = 'Ошибка загрузки данных';
        console.error(error);
    }
}

function getWeatherDescription(code) {
    const weatherCodes = {
        0: 'Ясно',
        1: 'Преимущественно ясно',
        2: 'Переменная облачность',
        3: 'Пасмурно',
        45: 'Туман',
        48: 'Иней',
        51: 'Лёгкая морось',
        53: 'Морось',
        55: 'Плотная морось',
        61: 'Небольшой дождь',
        63: 'Дождь',
        65: 'Сильный дождь',
        71: 'Небольшой снег',
        73: 'Снег',
        75: 'Сильный снег',
        95: 'Гроза'
    };
    return weatherCodes[code] || 'Облачно';
}

fetchWeather();
