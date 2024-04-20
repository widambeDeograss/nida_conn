import requests
from flask import Flask, jsonify, request
from  addict import Dict
app = Flask(__name__)


BASE_URL = "https://ors.brela.go.tz/um/load/load_nida/{}"

header = {
            "Content-Type": "application/json",
            "Content-Length": "0",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
        }


def load_user_information(self, national_id: str):
    try:
        user_information = requests.post(
            self.BASE_URL.format(national_id), headers=self.get_headers()
        ).json()

        if user_information["obj"].get("result"):
            user_data = user_information["obj"].get("result")
            return user_data
        if user_information["obj"].get("error"):
            return None
    except (requests.ConnectionError, requests.ConnectTimeout):
        raise ConnectionError(
            "Can't load user information probably connection issues"
        )


def load_user(self, national_id: str, json: bool = False):
    try:
        user_data = self.load_user_information(national_id)
        if not json:
            user_data = self.preprocess_user_data(user_data)
            return user_data
        return user_data
    except Exception as bug:
        print(bug)
        return None


# http://10.1.1.1:5000/login?nida_no=5267672672672


@app.route('/api/nida_info/', methods=['GET'])
def fetch_nida_info():
    nida_no = request.args.get('nida_no')
    user_detail = load_user(national_id=nida_no)

    return jsonify(user_detail)


if __name__ == '__main__':
    app.run()
