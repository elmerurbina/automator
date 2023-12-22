from flask import Flask, request, jsonify, flash, render_template, url_for, redirect
from backend import schedule_message

app = Flask(__name__)
app.debug = True

@app.route('/automator', methods=['GET', 'POST'])
def index():
    return render_template('message_automator.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.form
    #print(data)

    phone = request.form.get('phone_number')
    message = request.form.get('message')
    hour = int(request.form.get('hour'))
    minute = int(request.form.get('minute'))
    file_path = request.form.get('file_path')




    if schedule_message(phone, message, hour, minute, file_path):
        return jsonify({'status': 'success', 'message': 'message scheduled successfully'})

   # return redirect(url_for('success_page'))
    else:
        flash("Message scheduled successfully")
        return redirect(url_for('success_page'))

@app.route('/success', methods=['GET'])
def success_page():
        return render_template('success.html')

  #  return jsonify({'status': 'error', 'message': 'invalid scheduling time'})




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
