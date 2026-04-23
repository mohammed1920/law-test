// 1. إعداد الموسيقى الخلفية
const bgMusic = new Audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');
bgMusic.loop = true;
bgMusic.volume = 0.2; // صوت هادئ

// 2. إعداد أصوات الإجابات (باستخدام روابط مباشرة وسريعة جداً)
const correctSound = new Audio('https://actions.google.com/sounds/v1/cartoon/clink_clanking.ogg');
const wrongSound = new Audio('https://actions.google.com/sounds/v1/cartoon/boing.ogg');

// 3. محرك الإيقاظ (Unlock) عند أول لمسة
document.addEventListener('click', function() {
    if (bgMusic.paused) {
        bgMusic.play().catch(e => console.log("المتصفح ينتظر نقرة"));
    }
    // تحميل مسبق للأصوات لضمان السرعة
    correctSound.load();
    wrongSound.load();
}, { once: true });

// 4. الدوال التي تستدعيها ملفات HTML (يجب أن تكون بهذه الأسماء بالضبط)
function playCorrect() {
    correctSound.currentTime = 0; // إعادة الصوت للبداية لكي يعمل مع كل نقرة سريعة
    correctSound.play().catch(e => console.log("خطأ في تشغيل صوت الصح"));
}

function playWrong() {
    wrongSound.currentTime = 0; // إعادة الصوت للبداية
    wrongSound.play().catch(e => console.log("خطأ في تشغيل صوت الخطأ"));
}
