import qrcode
from flask import Flask, render_template, request, redirect
import io
import base64
from PIL import Image
import re
app = Flask(__name__)

validEndings = ["@abcdicici", "@apl", "@yapl", "@rapl", "@abfspay", "@abfspay", "@bpunity", "@axisb", "@yescred", "@yescurie", "@yesfam", "@fifederal", "@fkaxis", "@freoicici", "@gwaxis", "@okaxis", "@okhdfcbank", "@okicici", "@oksbi", "@yesg", "@inhdfc", "@jupiteraxis", "@goaxb", "@kphdfc", "@ikwik", "@mvhdfc", "@naviaxis", "@niyoicici", "@oneyes", "@axb", "@paytm", "@ptyes", "@ptaxis", "@pthdfc", "@ptsbi", "@ybl", "@ibl", "@axl", "@yespop", "@rmrbl", "@pingpay", "@seyes", "@shriramhdfcbank", "@sliceaxis", "@superyes", "@tapicici", "@timecosmos", "@axisbank", "@yestp", "@idfcbank", "@waicici", "@icici", "@waaxis", "@wahdfcbank", "@wasbi"]

@app.errorhandler(404)
def not_found(error):
    return {
        "error": "Not Found",
        "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }

@app.route('/qr')
def qr():
    return render_template('qr.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_upi', methods=['POST'])
def generate_upi():
    vpa = request.form['vpa']
    amount = request.form['amount']

    amount = round(float(amount), 2)
    
    # Construct the UPI link
    upi_link = f"/qr/{vpa}&{amount}"
    
    return redirect(upi_link)

@app.route('/qr/<vpa_and_amount>')
def upi_redirect(vpa_and_amount):
    try:
        vpa, amount = vpa_and_amount.split('&')
        amount = round(float(amount), 2)

        if not re.fullmatch(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+', vpa):
            return {"error": "Invalid VPA. Only letters, numbers, and '@' is allowed."}, 400
        
        if vpa_and_amount.count('@') != 1:
            return {"error": "Invalid VPA"}, 400
        
        upi_link = f"upi://pay?pa={vpa}&am={amount}&cu=INR"

        qr = qrcode.make(upi_link)

        img = io.BytesIO()
        qr.save(img, format='PNG')
        img.seek(0) 

        qr_code_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
        
        return render_template('upiQR.html', vpa=vpa, amount=amount, qr_code=qr_code_base64)
    
    except Exception as e:
        return {"error": str(e)}, 400
    
@app.route('/upi/api/<vpa_and_amount>')
def upi_api(vpa_and_amount):
    try:
        vpa, amount = vpa_and_amount.split('&')
        amount = round(float(amount), 2)

        if not re.fullmatch(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+', vpa):
            return {"error": "Invalid VPA. Only letters, numbers, and '@' is allowed."}, 400
        
        if vpa_and_amount.count('@') != 1:
            return {"error": "Invalid VPA"}, 400
        
        upi_link = f"upi://pay?pa={vpa}&am={amount}&cu=INR"
        
        return {
            "vpa": vpa,
            "amount": amount,
            "upi_link": upi_link,
            "gpay_link": f'tez://upi/pay?pa={vpa}&am={amount}&cu=INR',
            "phonepe_link": f"phonepe://upi/pay?pa={vpa}&am={amount}&cu=INR"
        }
    except Exception as e:
        return {"error": str(e)}, 400
    
@app.route('/upi/api/validEndings')
def valid_endings():
    try:
        return {
            "validEndings": validEndings,
            "lastUpdated": "2025-02-10 17:11:21 UTC+5;30",
            "source": "https://www.npci.org.in/what-we-do/upi/3rd-party-apps"
        }
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
