@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Generate JWT
    access_token = create_access_token(identity={'username': user.username, 'email': user.email})
    return jsonify({"token": access_token}), 200

