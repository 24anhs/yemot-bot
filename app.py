from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# פונקציה ליצירת מסד הנתונים (רצה אוטומטית כשהשרת עולה)
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # יצירת טבלה עם 3 עמודות: מזהה פנימי, טלפון, ותעודת זהות
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, phone TEXT, user_id TEXT)''')
    conn.commit()
    conn.close()

# הפעלת הפונקציה כדי לוודא שהטבלה מוכנה
init_db()

@app.route('/yemot', methods=['GET', 'POST'])
def yemot_api():
    caller_phone = request.values.get('ApiPhone')
    user_input = request.values.get('ID_Input')

    if not user_input:
        return "read=t-אנא הקש את תעודת הזהות שלך וסולם=ID_Input,no,9,9,7,Ok,True,True"
    else:
        # פתיחת חיבור למסד הנתונים ושמירת הנתונים
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (phone, user_id) VALUES (?, ?)", (caller_phone, user_input))
        conn.commit()
        conn.close()
        
        return f"id_list_message=t-שלום למספר טלפון {caller_phone}! תעודת הזהות שהקשת היא {user_input}! תודה ולהתראות&hangup"

# נתיב חדש ויעודי בשבילך כדי לראות את הנתונים!
@app.route('/show-data')
def show_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # שליפת כל הנתונים מהטבלה
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    
    # בניית דף HTML פשוט שמציג את הנתונים בטבלה
    html_content = "<h1 dir='rtl'>נתונים שנשמרו במערכת:</h1><table border='1' dir='rtl' style='font-size: 20px; text-align: center;'>"
    html_content += "<tr><th style='padding: 10px;'>מספר סידורי</th><th style='padding: 10px;'>טלפון</th><th style='padding: 10px;'>תעודת זהות</th></tr>"
    for row in rows:
        html_content += f"<tr><td style='padding: 10px;'>{row[0]}</td><td style='padding: 10px;'>{row[1]}</td><td style='padding: 10px;'>{row[2]}</td></tr>"
    html_content += "</table>"
    
    return html_content

if __name__ == '__main__':
    # הפעלת השרת
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
