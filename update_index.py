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
    # البحث عن ملفات html التي تبدأ بـ ch
    files = sorted([f for f in os.listdir('.') if f.startswith('ch') and f.endswith('.html')])
    
    with open(main_file, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html>\n<html dir="rtl" lang="ar">\n<head>\n')
        f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write('<title>فهرس الكتاب</title>\n')
        f.write('<style>body{font-family:"Cairo", sans-serif; background:#0f172a; color:white; padding:20px; text-align:center;} ')
        f.write('a{display:block; background:#1e293b; color:#38bdf8; margin:10px auto; padding:15px; border-radius:10px; text-decoration:none; max-width:400px; border:1px solid #334155; transition:0.3s;} ')
        f.write('a:hover{background:#334155; transform: scale(1.02);}</style>\n</head>\n<body>\n')
        f.write('<h1>فهرس فصول الكتاب</h1>\n<p>تحديث تلقائي</p>\n<hr style="border:0.5px solid #334155; max-width:400px;">\n<br>\n')
        
        for file_name in files:
            arabic_title = get_html_title(file_name)
            f.write(f'<a href="{file_name}">{arabic_title}</a>\n')
            
        f.write('\n</body>\n</html>')

if __name__ == "__main__":
    generate_index()
