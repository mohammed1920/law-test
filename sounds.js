// ملف المحرك الصوتي الموحد لجميع الفصول
const audioCtx = {
    correct: new Audio('https://www.soundjay.com/buttons/sounds/button-37.mp3'),
    wrong: new Audio('https://www.soundjay.com/buttons/sounds/button-10.mp3')
};

// دالة استدعاء الصوت
function playCorrect() {
    audioCtx.correct.currentTime = 0;
    audioCtx.correct.play().catch(e => console.log("الصوت مفعل بعد أول نقرة"));
}

function playWrong() {
    audioCtx.wrong.currentTime = 0;
    audioCtx.wrong.play().catch(e => console.log("الصوت مفعل بعد أول نقرة"));
}

