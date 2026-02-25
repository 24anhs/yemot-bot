from flask import Flask, request

app = Flask(__name__)

@app.route('/yemot', methods=['GET', 'POST'])
def yemot_api():
    # קבלת הנתונים שימות המשיח שלחו אלינו
    caller_phone = request.values.get('ApiPhone', 'לא מזוהה') # מספר הטלפון
    user_input = request.values.get('ID_Input')   # הקלט מהמשתמש

    # שלב א': אם עדיין אין קלט מהלקוח
    if not user_input:
        return "read=t-אנא הקש את תעודת הזהות שלך וסולם=ID_Input,no,9,9,7,Ok,True,True"
    
    # שלב ב': קיבלנו את הקלט
    else:
        # שמנו פסיקים במקום נקודות כדי שהרובוט של ימות המשיח לא יקרוס
        return f"id_list_message=t-שלום למספר טלפון, {caller_phone}, תעודת הזהות שהקשת היא, {user_input}, תודה ולהתראות&hangup"

if __name__ == '__main__':
    app.run(port=5000)
