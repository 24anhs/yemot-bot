from flask import Flask, request

app = Flask(__name__)

@app.route('/yemot', methods=['GET', 'POST'])
def yemot_api():
    # קבלת הנתונים שימות המשיח שלחו אלינו
    caller_phone = request.values.get('ApiPhone') # מספר הטלפון של המחייג
    user_input = request.values.get('ID_Input')   # משתנה שאנחנו נגדיר בשלב הבקשה

    # אם עדיין אין לנו קלט מהלקוח, נבקש ממנו להקיש נתונים
    if not user_input:
        # פקודת read: מבקשת מהלקוח להקיש נתונים. 
        # המבנה: read=קובץ_שמע=שם_משתנה_לחזרה,מספר_ספרות...
        # t-אנא... = השמעת טקסט (Text to Speech)
        return "read=t-אנא הקש את תעודת הזהות שלך וסולם=ID_Input,no,9,9,7,TeudatZehut"
    
    # אם כבר קיבלנו את הקלט מהלקוח
    else:
        # פקודת id_list_message: משמיעה הודעה
        # פקודת hangup: מנתקת את השיחה
        return f"id_list_message=t-שלום למספר טלפון {caller_phone}. תעודת הזהות שהקשת היא {user_input}. תודה ולהתראות&hangup"

if __name__ == '__main__':
    # הפעלת השרת על פורט 5000
    app.run(port=5000)

