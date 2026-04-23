import os
import re

# دالة لجلب العنوان من الملف
def get_html_title(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # البحث عن العنوان المكتوب داخل وسم title
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
    except Exception:
        pass
    return file_path

# دالة توليد الفهرس
def generate_index():
    main_file = "index.html"
    # جلب ملفات الفصول وترتيبها أبجدياً
    files = sorted([f for f in os.listdir('.') if f.startswith('ch') and f.endswith('.html')])
    
    with open(main_file, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html>\n<html dir="rtl" lang="ar">\n<head>\n')
        f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('<title>فهرس فصول الكتاب</title>\n')
        f.write('<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">\n')
        f.write('<style>\n')
        
        # 1. الخلفية سوداء ملكية مريحة للعين
        f.write('  body { font-family: "Cairo", sans-serif; background: #080808; color: #f8fafc; padding: 20px; margin: 0; min-height: 100vh; }\n')
        f.write('  .header { text-align: center; padding: 30px 0; }\n')
        
        # 2. العنوان الرئيسي ذهبي متألق (خط أصغر)
        f.write('  h1 { color: #d4af37; font-size: 1.8rem; margin-bottom: 8px; text-shadow: 0 0 15px rgba(212, 175, 55, 0.4); }\n')
        f.write('  .container { max-width: 650px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding-bottom: 60px; }\n')
        
        # 3. تنسيق بطاقة الفصل (الإطار) - أسود مع حافة ذهبية ناعمة
        f.write('  .chapter-card { \n')
        f.write('      background: rgba(20, 20, 20, 0.8); \n')
        f.write('      border: 1px solid rgba(212, 175, 55, 0.1); border-radius: 14px; \n')
        f.write('      padding: 16px 20px; text-decoration: none; transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); \n')
        f.write('      display: flex; align-items: center; gap: 15px; \n')
        f.write('      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3); \n')
        f.write('  }\n')
        
        # تأثير عند تمرير الماوس أو اللمس (يبرز الذهبي)
        f.write('  .chapter-card:hover { \n')
        f.write('      transform: scale(1.02) translateX(-5px); border-color: #d4af37; \n')
        f.write('      background: rgba(212, 175, 55, 0.05); box-shadow: 0 8px 20px rgba(212, 175, 55, 0.2); \n')
        f.write('  }\n')
        
        # 4. عنوان الفصل - خط أصغر وأوضح
        f.write('  .chapter-title { color: #f8fafc; font-size: 1.05rem; font-weight: bold; flex-grow: 1; }\n')
        
        # 5. الأرقام داخل الدوائر على اليمين - واضحة جداً وخلفية ذهبية
        f.write('  .chapter-icon { background: #d4af37; color: #080808; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 0.85rem; font-weight: 700; order: -1; }\n')
        
        # 6. زر التليجرام - ذهبي ملكي
        f.write('  .telegram-btn { \n')
        f.write('      display: flex; align-items: center; justify-content: center; gap: 10px; \n')
        f.write('      background: linear-gradient(135deg, #a67c00, #d4af37); color: #080808; \n')
        f.write('      padding: 16px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; \n')
        f.write('      margin-top: 35px; box-shadow: 0 10px 25px rgba(212, 175, 55, 0.3); \n')
        f.write('      transition: 0.3s; width: fit-content; align-self: center; font-size: 1rem; \n')
        f.write('  }\n')
        f.write('  .telegram-btn:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(212, 175, 55, 0.5); }\n')
        f.write('  .footer { text-align: center; margin-top: 40px; font-size: 0.8rem; color: #64748b; letter-spacing: 1px; }\n')
        
        f.write('</style>\n</head>\n<body>\n')
        f.write('<div class="header"><h1>فهرس فصول الكتاب</h1><p style="color:#64748b; font-size:0.9rem;">تحديث تلقائي ذكي</p></div>\n')
        f.write('<div class="container">\n')
        
        # توليد البطاقات
        for index, file_name in enumerate(files, start=1):
            arabic_title = get_html_title(file_name)
            f.write(f'  <a href="{file_name}" class="chapter-card">\n')
            f.write(f'    <span class="chapter-icon">{index}</span>\n') # الرقم على اليمين
            f.write(f'    <span class="chapter-title">{arabic_title}</span>\n')
            f.write(f'  </a>\n')
            
        # زر التليجرام
        f.write('  <a href="https://t.me/M5M5P" class="telegram-btn">\n')
        f.write('    <span>انضم لقناة التليجرام</span>\n')
        f.write('    <span>✈️</span>\n')
        f.write('  </a>\n')
        
        f.write('  <div class="footer">تم التطوير بواسطة فاعل خير </div>\n')
        f.write('</div>\n</body>\n</html>')

if __name__ == "__main__":
    generate_index()
