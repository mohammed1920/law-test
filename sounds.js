// موسيقى الخلفية
const bgMusic = new Audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');
bgMusic.loop = true;
bgMusic.volume = 0.3;

// تشغيل الموسيقى عند أول نقرة
document.addEventListener('click', () => {
    bgMusic.play().catch(() => {});
}, { once: true });

// دالة الصوت الصحيح
function playCorrect() {
    const sound = new Audio('https://www.myinstants.com/media/sounds/correct.mp3');
    sound.play();
}

// دالة الصوت الخاطئ
function playWrong() {
    const sound = new Audio('https://www.myinstants.com/media/sounds/wrong.mp3');
    sound.play();
}
