// المحرك الصوتي المطور: موسيقى + تفاعل
const audioManager = {
    bgMusic: new Audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'), // موسيقى هادئة
    correct: new Audio('https://actions.google.com/sounds/v1/cartoon/clink_clanking.ogg'),
    wrong: new Audio('https://actions.google.com/sounds/v1/cartoon/boing.ogg'),
    isInitialized: false
};

// إعدادات الموسيقى الخلفية
audioManager.bgMusic.loop = true; // تكرار مستمر
audioManager.bgMusic.volume = 0.2; // خفض الصوت ليكون هادئاً ولا يغطي على تفكير الطالب

function initAllSounds() {
    if (audioManager.isInitialized) return;
    
    // تشغيل الموسيقى الخلفية
    audioManager.bgMusic.play().catch(e => console.log("بانتظار التفاعل لبدء الموسيقى"));
    
    // تجهيز أصوات التفاعل
    audioManager.correct.load();
    audioManager.wrong.load();
    
    audioManager.isInitialized = true;
    console.log("تم تفعيل الموسيقى والنظام الصوتي");
}

// تشغيل عند أول نقرة في أي مكان
document.addEventListener('click', initAllSounds, { once: true });
document.addEventListener('touchstart', initAllSounds, { once: true });

function playCorrect() {
    audioManager.correct.currentTime = 0;
    audioManager.correct.play();
}

function playWrong() {
    audioManager.wrong.currentTime = 0;
    audioManager.wrong.play();
}
