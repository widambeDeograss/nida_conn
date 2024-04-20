from flask import Flask, jsonify, request
from nida import Nida

app = Flask(__name__)


# http://10.1.1.1:5000/login?nida_no=5267672672672

@app.route('/api/nida_info/', methods=['GET'])
def fetch_nida_info():
    nida_no = request.args.get('nida_no')
    user_detail = Nida.load_user(national_id=nida_no)

    return jsonify(user_detail)


if __name__ == '__main__':
    app.run()
