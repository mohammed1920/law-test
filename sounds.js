// ملف sounds.js المحدث
const correctSound = new Audio('https://actions.google.com/sounds/v1/cartoon/clink_clanking.ogg');
const wrongSound = new Audio('https://actions.google.com/sounds/v1/cartoon/boing.ogg');

function playCorrect() {
    correctSound.currentTime = 0;
    correctSound.play().catch(e => console.log("تفاعل مع الصفحة أولاً"));
}

function playWrong() {
    wrongSound.currentTime = 0;
    wrongSound.play().catch(e => console.log("تفاعل مع الصفحة أولاً"));
}
