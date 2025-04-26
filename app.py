from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get('Body').strip().lower()
    response = MessagingResponse()
    msg = response.message()

    if incoming_msg in ["hi", "مرحبا", "السلام عليكم"]:
        msg.body("""👋 أهلاً وسهلاً بك في مركز العناية الطبي التخصصي.
يرجى اختيار الخدمة التي تريدها:
1️⃣ حجز موعد
2️⃣ الاستفسار عن العيادات
3️⃣ معرفة مواعيد الدوام
4️⃣ التحدث مع موظف

(اكتب الرقم فقط للمتابعة)""")
    elif incoming_msg == "1":
        msg.body("📅 لحجز موعد، الرجاء إرسال:\n- الاسم\n- رقم الهاتف\n- العيادة المطلوبة\n- التاريخ المرغوب")
    elif incoming_msg == "2":
        msg.body("🏥 العيادات المتوفرة:\n- الباطنية\n- الأطفال\n- الأسنان\n- الجلدية\n- النسائية\n- العظام")
    elif incoming_msg == "3":
        msg.body("🕒 الدوام من الأحد إلى الخميس، من الساعة 8:00 صباحاً حتى 4:00 مساءً.")
    elif incoming_msg == "4":
        msg.body("📞 سيتم تحويلك إلى موظف الاستقبال... الرجاء الانتظار.")
    else:
        msg.body("❓ لم أفهم رسالتك. اكتب 'مرحبا' للبدء من جديد.")

    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
