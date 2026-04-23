import os
import re

def get_html_title(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
    except Exception:
        pass
    return file_path

def generate_index():
    main_file = "index.html"
    files = sorted([f for f in os.listdir('.') if f.startswith('ch') and f.endswith('.html')])
    
    with open(main_file, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html>\n<html dir="rtl" lang="ar">\n<head>\n')
        f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('<title>فهرس فصول الكتاب</title>\n')
        f.write('<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">\n')
        f.write('<style>\n')
        f.write('  body { font-family: "Cairo", sans-serif; background: #0f172a; color: white; padding: 20px; margin: 0; }\n')
        f.write('  .header { text-align: center; padding: 40px 0; }\n')
        f.write('  h1 { color: #38bdf8; font-size: 2.5rem; margin-bottom: 10px; text-shadow: 0 0 20px rgba(56, 189, 248, 0.3); }\n')
        f.write('  .container { max-width: 800px; margin: 0 auto; display: grid; grid-template-columns: 1fr; gap: 20px; padding-bottom: 50px; }\n')
        
        # تصميم الإطار لكل فصل
        f.write('  .chapter-card { \n')
        f.write('      background: #1e293b; border: 1px solid #334155; border-radius: 15px; \n')
        f.write('      padding: 20px; text-decoration: none; transition: all 0.3s ease; \n')
        f.write('      display: flex; justify-content: space-between; align-items: center; \n')
        f.write('      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); \n')
        f.write('  }\n')
        f.write('  .chapter-card:hover { \n')
        f.write('      transform: translateX(-10px); border-color: #38bdf8; \n')
        f.write('      background: #2d3748; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); \n')
        f.write('  }\n')
        f.write('  .chapter-title { color: #f8fafc; font-size: 1.2rem; font-weight: bold; }\n')
        f.write('  .chapter-icon { color: #38bdf8; font-size: 1.5rem; }\n')
        
        # تصميم زر التلكرام
        f.write('  .telegram-btn { \n')
        f.write('      display: flex; align-items: center; justify-content: center; gap: 10px; \n')
        f.write('      background: linear-gradient(135deg, #0088cc, #00aaff); color: white; \n')
        f.write('      padding: 15px; border-radius: 50px; text-decoration: none; font-weight: bold; \n')
        f.write('      margin-top: 30px; box-shadow: 0 10px 20px rgba(0, 136, 204, 0.3); \n')
        f.write('      transition: 0.3s; width: fit-content; margin-left: auto; margin-right: auto; \n')
        f.write('  }\n')
        f.write('  .telegram-btn:hover { transform: scale(1.05); box-shadow: 0 15px 25px rgba(0, 136, 204, 0.5); }\n')
        
        f.write('</style>\n</head>\n<body>\n')
        f.write('<div class="header"><h1>فهرس فصول الكتاب</h1><p style="color:#64748b;">نظام الأتمتة القانوني</p></div>\n')
        f.write('<div class="container">\n')
        
        # إنشاء البطاقات للفصول
        for file_name in files:
            arabic_title = get_html_title(file_name)
            f.write(f'  <a href="{file_name}" class="chapter-card">\n')
            f.write(f'    <span class="chapter-title">{arabic_title}</span>\n')
            f.write(f'    <span class="chapter-icon">📖</span>\n')
            f.write(f'  </a>\n')
            
        # إضافة زر التلكرام برابطك الجديد
        f.write('  <a href="https://t.me/M5M5P" class="telegram-btn">\n')
        f.write('    <span>انضم لقناتنا على تليجرام</span>\n')
        f.write('    <span>✈️</span>\n')
        f.write('  </a>\n')
        
        f.write('</div>\n</body>\n</html>')

if __name__ == "__main__":
    generate_index()
