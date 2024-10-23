from flask import Flask, request, jsonify

authData = {
   "id": "felipe.montero@uconn.edu",
   "token": "3c44fa6d9bc869945c373879aea756de8aba0937d581970b61bdc78f1100f2a7"
}

app = Flask(__name__)

@app.route("/")
def hello():
   return "You called \n"

@app.route("/login", methods=['POST'])
def login():
   # Log the incoming form data for debugging
   print("Received form data:", request.form)

   # Get 'id' and 'token' from request form data
   user_id = request.form.get('id')
   token = request.form.get('token')
   
   # Check if the provided 'id' and 'token' match authData
   if user_id == authData['id'] and token == authData['token']:
      return jsonify({"message": "Login successful"}), 200
   else:
      return jsonify({"message": "Login failed, invalid credentials"}), 401

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)
