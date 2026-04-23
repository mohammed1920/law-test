// 1. تعريف جميع الأصوات
const sounds = {
    bg: new Audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'),
    correct: new Audio('https://actions.google.com/sounds/v1/cartoon/clink_clanking.ogg'),
    wrong: new Audio('https://actions.google.com/sounds/v1/cartoon/boing.ogg')
};

// 2. إعدادات الصوت
sounds.bg.loop = true;
sounds.bg.volume = 0.2;

// 3. دالة "الإيقاظ الشامل" (تفعيل كل المسارات الصوتية بنقرة واحدة)
function setupAudio() {
    // تشغيل الموسيقى
    sounds.bg.play().catch(() => {});
    
    // تشغيل أصوات التفاعل صامتة للحظة ثم إيقافها (لفتح قفل المتصفح)
    sounds.correct.muted = true;
    sounds.correct.play().then(() => {
        sounds.correct.pause();
        sounds.correct.muted = false;
        sounds.correct.currentTime = 0;
    }).catch(() => {});

    sounds.wrong.muted = true;
    sounds.wrong.play().then(() => {
        sounds.wrong.pause();
        sounds.wrong.muted = false;
        sounds.wrong.currentTime = 0;
    }).catch(() => {});
}

// تفعيل النظام عند أول لمسة
document.addEventListener('click', setupAudio, { once: true });
document.addEventListener('touchstart', setupAudio, { once: true });

// 4. الدوال التي تناديها ملفات الـ HTML
function playCorrect() {
    if (sounds.correct) {
        sounds.correct.currentTime = 0;
        sounds.correct.play().catch(e => console.log("خطأ صوت الصح"));
    }
}

function playWrong() {
    if (sounds.wrong) {
        sounds.wrong.currentTime = 0;
        sounds.wrong.play().catch(e => console.log("خطأ صوت الخطأ"));
    }
}
