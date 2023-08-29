function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function changeTheme() {
    const randomInt = getRandomInt(1, 2);

    if (randomInt === 1) {
        document.body.className = 'light-side';
        document.getElementById('app').innerHTML = '<h1>SPA del Bootcamp AWS Cloud Engineer - Lado Luminoso</h1>';
    } else {
        document.body.className = 'dark-side';
        document.getElementById('app').innerHTML = '<h1>SPA del Bootcamp AWS Cloud Engineer - Lado Oscuro</h1>';
    }

    // Deshabilitar el botón después de hacer clic en él
    document.getElementById('changeThemeButton').disabled = true;
}
