// 1. تعريف الأصوات (استخدمت لك روابط موثوقة جداً من جوجل)
const bgMusic = new Audio('https://actions.google.com/sounds/v1/weather/rain_on_roof.ogg'); // موسيقى مطر هادئة جداً
const correctSound = new Audio('https://actions.google.com/sounds/v1/cartoon/clink_clanking.ogg');
const wrongSound = new Audio('https://actions.google.com/sounds/v1/cartoon/boing.ogg');

// إعدادات الموسيقى
bgMusic.loop = true;
bgMusic.volume = 0.1; 

// 2. دالة "الإيقاظ" الإجبارية
function startAudioSystem() {
    // تشغيل الكل صامت لفتح القفل
    [bgMusic, correctSound, wrongSound].forEach(s => {
        s.play().then(() => {
            if (s !== bgMusic) { s.pause(); s.currentTime = 0; }
        }).catch(e => console.log("بانتظار اللمسة الأولى"));
    });
}

// تفعيل عند أول لمسة للشاشة
document.addEventListener('click', startAudioSystem, { once: true });
document.addEventListener('touchstart', startAudioSystem, { once: true });

// 3. الدوال التي تطلبها ملفات الـ HTML
window.playCorrect = function() {
    correctSound.currentTime = 0;
    correctSound.play();
};

window.playWrong = function() {
    wrongSound.currentTime = 0;
    wrongSound.play();
};
