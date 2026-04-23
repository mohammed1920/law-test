import os
import re

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
        # تنسيق الخلفية والجسم
        f.write('  body { font-family: "Cairo", sans-serif; background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%); color: white; padding: 20px; margin: 0; min-height: 100vh; }\n')
        f.write('  .header { text-align: center; padding: 40px 0; }\n')
        f.write('  h1 { color: #38bdf8; font-size: 2.2rem; margin-bottom: 10px; text-shadow: 0 0 20px rgba(56, 189, 248, 0.3); }\n')
        f.write('  .container { max-width: 700px; margin: 0 auto; display: flex; flex-direction: column; gap: 15px; padding-bottom: 60px; }\n')
        
        # تنسيق بطاقة الفصل (الإطار)
        f.write('  .chapter-card { \n')
        f.write('      background: rgba(30, 41, 59, 0.6); backdrop-filter: blur(10px); \n')
        f.write('      border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 16px; \n')
        f.write('      padding: 22px; text-decoration: none; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); \n')
        f.write('      display: flex; justify-content: space-between; align-items: center; \n')
        f.write('      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); \n')
        f.write('  }\n')
        
        # تأثير عند تمرير الماوس أو اللمس
        f.write('  .chapter-card:hover { \n')
        f.write('      transform: scale(1.03) translateX(-5px); border-color: #38bdf8; \n')
        f.write('      background: rgba(56, 189, 248, 0.1); box-shadow: 0 10px 25px rgba(56, 189, 248, 0.2); \n')
        f.write('  }\n')
        
        f.write('  .chapter-title { color: #f8fafc; font-size: 1.15rem; font-weight: bold; }\n')
        f.write('  .chapter-icon { background: #334155; width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 0.9rem; }\n')
        
        # تنسيق زر التليجرام الاحترافي
        f.write('  .telegram-btn { \n')
        f.write('      display: flex; align-items: center; justify-content: center; gap: 12px; \n')
        f.write('      background: linear-gradient(135deg, #0088cc, #00aaff); color: white; \n')
        f.write('      padding: 18px 35px; border-radius: 50px; text-decoration: none; font-weight: bold; \n')
        f.write('      margin-top: 40px; box-shadow: 0 10px 25px rgba(0, 136, 204, 0.4); \n')
        f.write('      transition: 0.3s; width: fit-content; align-self: center; \n')
        f.write('  }\n')
        f.write('  .telegram-btn:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0, 136, 204, 0.6); }\n')
        f.write('  .footer { text-align: center; margin-top: 40px; font-size: 0.8rem; color: #64748b; letter-spacing: 1px; }\n')
        
        f.write('</style>\n</head>\n<body>\n')
        f.write('<div class="header"><h1>فهرس فصول الكتاب</h1><p style="color:#94a3b8;">تحديث تلقائي ذكي</p></div>\n')
        f.write('<div class="container">\n')
        
        # توليد البطاقات
        for index, file_name in enumerate(files, start=1):
            arabic_title = get_html_title(file_name)
            f.write(f'  <a href="{file_name}" class="chapter-card">\n')
            f.write(f'    <span class="chapter-title">{arabic_title}</span>\n')
            f.write(f'    <span class="chapter-icon">{index}</span>\n') # يظهر رقم الفصل بدائرة
            f.write(f'  </a>\n')
            
        # زر التليجرام برابط قناتك
        f.write('  <a href="https://t.me/M5M5P" class="telegram-btn">\n')
        f.write('    <span>انضم لقناة التليجرام</span>\n')
        f.write('    <span>✈️</span>\n')
        f.write('  </a>\n')
        
        f.write('  <div class="footer">تم البرمجة والتطوير بواسطة الأتمتة الذكية</div>\n')
        f.write('</div>\n</body>\n</html>')

if __name__ == "__main__":
    generate_index()
