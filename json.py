{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "882e179f-d085-4146-9e2e-fc5d1e916c61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting flask-jwt-extended\n",
      "  Downloading Flask_JWT_Extended-4.7.1-py2.py3-none-any.whl.metadata (3.8 kB)\n",
      "Requirement already satisfied: Werkzeug>=0.14 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask-jwt-extended) (3.0.3)\n",
      "Requirement already satisfied: Flask<4.0,>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask-jwt-extended) (3.0.3)\n",
      "Requirement already satisfied: PyJWT<3.0,>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask-jwt-extended) (2.8.0)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask<4.0,>=2.0->flask-jwt-extended) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask<4.0,>=2.0->flask-jwt-extended) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask<4.0,>=2.0->flask-jwt-extended) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask<4.0,>=2.0->flask-jwt-extended) (1.6.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from Werkzeug>=0.14->flask-jwt-extended) (2.1.3)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=8.1.3->Flask<4.0,>=2.0->flask-jwt-extended) (0.4.6)\n",
      "Downloading Flask_JWT_Extended-4.7.1-py2.py3-none-any.whl (22 kB)\n",
      "Installing collected packages: flask-jwt-extended\n",
      "Successfully installed flask-jwt-extended-4.7.1\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask-jwt-extended\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8fa992db-b6a9-4131-b5a2-002094872295",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'flask_jwt_extended'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mflask_jwt_extended\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m JWTManager, jwt_required, create_access_token\n\u001b[0;32m      3\u001b[0m app\u001b[38;5;241m.\u001b[39mconfig[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mJWT_SECRET_KEY\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124myour-secret-key\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m      4\u001b[0m jwt \u001b[38;5;241m=\u001b[39m JWTManager(app)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'flask_jwt_extended'"
     ]
    }
   ],
   "source": [
    "from flask_jwt_extended import JWTManager, jwt_required, create_access_token\n",
    "\n",
    "app.config['JWT_SECRET_KEY'] = 'your-secret-key'\n",
    "jwt = JWTManager(app)\n",
    "\n",
    "@app.route('/login', methods=['POST'])\n",
    "def login():\n",
    "    username = request.json.get('username')\n",
    "    password = request.json.get('password')\n",
    "    # Replace this with real authentication logic\n",
    "    if username == 'admin' and password == 'password':\n",
    "        access_token = create_access_token(identity={'username': username})\n",
    "        return jsonify(access_token=access_token)\n",
    "    else:\n",
    "        return jsonify({'msg': 'Bad username or password'}), 401\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "@jwt_required()\n",
    "def predict():\n",
    "    try:\n",
    "        # Load model and scaler\n",
    "        model = joblib.load('models/random_forest_model.pkl')\n",
    "        scaler = joblib.load('models/scaler.pkl')\n",
    "\n",
    "        # Get input data\n",
    "        data = request.get_json()\n",
    "        input_features = np.array(data['features']).reshape(1, -1)\n",
    "\n",
    "        # Preprocess and predict\n",
    "        input_features = scaler.transform(input_features)\n",
    "        prediction = model.predict(input_features)\n",
    "        probability = model.predict_proba(input_features).tolist()\n",
    "\n",
    "        return jsonify({'prediction': int(prediction[0]), 'probability': probability})\n",
    "\n",
    "    except Exception as e:\n",
    "        return jsonify({'error': str(e)})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4c7a7c3-f113-4934-9c8b-82e3e5bcc248",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
