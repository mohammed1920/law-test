// إنشاء كائنات الصوت
const audioCtx = {
    correct: new Audio('https://www.soundjay.com/buttons/sounds/button-37.mp3'),
    wrong: new Audio('https://www.soundjay.com/buttons/sounds/button-10.mp3')
};

// ضبط الإعدادات لضمان الجاهزية
Object.values(audioCtx).forEach(sound => {
    sound.preload = 'auto';
    sound.load();
});

function playCorrect() {
    // نطلب من المتصفح تشغيل الصوت ونصفر الوقت لضمان التكرار السريع
    audioCtx.correct.pause();
    audioCtx.correct.currentTime = 0;
    audioCtx.correct.play().catch(err => console.log("تفاعل مع الصفحة أولاً لتفعيل الصوت"));
}

function playWrong() {
    audioCtx.wrong.pause();
    audioCtx.wrong.currentTime = 0;
    audioCtx.wrong.play().catch(err => console.log("تفاعل مع الصفحة أولاً لتفعيل الصوت"));
}
