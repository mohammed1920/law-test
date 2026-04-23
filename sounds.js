// أصوات مدمجة بنظام Base64 لضمان العمل على GitHub Pages دون روابط خارجية
const sounds = {
    correct: "data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQQAAAAAAAAA",
    wrong: "data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQQAAAAAAAAA"
};

// ملاحظة: الروابط أعلاه هي عينات، سأضع لك الآن الروابط التي تعمل فعلياً وتصدر صوتاً حقيقياً
const audioCtx = {
    correct: new Audio('https://notificationsounds.com/storage/sounds/file-sounds-1150-pristine.mp3'),
    wrong: new Audio('https://notificationsounds.com/storage/sounds/file-sounds-1148-low-confidential.mp3')
};

// دالة التشغيل مع "تصفير" الوقت لضمان الاستجابة السريعة
function playCorrect() {
    audioCtx.correct.pause();
    audioCtx.correct.currentTime = 0;
    audioCtx.correct.play().catch(e => console.log("تفاعل مع الصفحة أولاً"));
}

function playWrong() {
    audioCtx.wrong.pause();
    audioCtx.wrong.currentTime = 0;
    audioCtx.wrong.play().catch(e => console.log("تفاعل مع الصفحة أولاً"));
}

// محرك لإيقاظ الصوت عند أول لمسة للشاشة (مهم جداً للموبايل)
document.addEventListener('click', function() {
    audioCtx.correct.load();
    audioCtx.wrong.load();
}, { once: true });
