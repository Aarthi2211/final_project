{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "de0ffe97-ab60-4554-99c3-39795a32c3be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting locust\n",
      "  Downloading locust-2.32.5-py3-none-any.whl.metadata (10.0 kB)\n",
      "Collecting ConfigArgParse>=1.5.5 (from locust)\n",
      "  Downloading ConfigArgParse-1.7-py3-none-any.whl.metadata (23 kB)\n",
      "Collecting Flask-Cors>=3.0.10 (from locust)\n",
      "  Downloading Flask_Cors-5.0.0-py2.py3-none-any.whl.metadata (5.5 kB)\n",
      "Collecting Flask-Login>=0.6.3 (from locust)\n",
      "  Downloading Flask_Login-0.6.3-py3-none-any.whl.metadata (5.8 kB)\n",
      "Requirement already satisfied: Werkzeug>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (3.0.3)\n",
      "Requirement already satisfied: flask>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (3.0.3)\n",
      "Collecting geventhttpclient>=2.3.1 (from locust)\n",
      "  Downloading geventhttpclient-2.3.3-cp312-cp312-win_amd64.whl.metadata (10.0 kB)\n",
      "Requirement already satisfied: msgpack>=1.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (1.0.3)\n",
      "Collecting psutil>=5.9.1 (from locust)\n",
      "  Downloading psutil-6.1.1-cp37-abi3-win_amd64.whl.metadata (23 kB)\n",
      "Requirement already satisfied: pywin32 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (305.1)\n",
      "Requirement already satisfied: pyzmq>=25.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (25.1.2)\n",
      "Requirement already satisfied: requests>=2.32.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (2.32.3)\n",
      "Requirement already satisfied: setuptools>=70.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from locust) (75.1.0)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask>=2.0.0->locust) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask>=2.0.0->locust) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask>=2.0.0->locust) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask>=2.0.0->locust) (1.6.2)\n",
      "Collecting gevent (from geventhttpclient>=2.3.1->locust)\n",
      "  Downloading gevent-24.11.1-cp312-cp312-win_amd64.whl.metadata (13 kB)\n",
      "Requirement already satisfied: certifi in c:\\programdata\\anaconda3\\lib\\site-packages (from geventhttpclient>=2.3.1->locust) (2024.8.30)\n",
      "Requirement already satisfied: brotli in c:\\programdata\\anaconda3\\lib\\site-packages (from geventhttpclient>=2.3.1->locust) (1.0.9)\n",
      "Requirement already satisfied: urllib3 in c:\\programdata\\anaconda3\\lib\\site-packages (from geventhttpclient>=2.3.1->locust) (2.2.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.32.2->locust) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.32.2->locust) (3.7)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from Werkzeug>=2.0.0->locust) (2.1.3)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=8.1.3->flask>=2.0.0->locust) (0.4.6)\n",
      "Collecting zope.event (from gevent->geventhttpclient>=2.3.1->locust)\n",
      "  Downloading zope.event-5.0-py3-none-any.whl.metadata (4.4 kB)\n",
      "Requirement already satisfied: zope.interface in c:\\programdata\\anaconda3\\lib\\site-packages (from gevent->geventhttpclient>=2.3.1->locust) (5.4.0)\n",
      "Collecting greenlet>=3.1.1 (from gevent->geventhttpclient>=2.3.1->locust)\n",
      "  Downloading greenlet-3.1.1-cp312-cp312-win_amd64.whl.metadata (3.9 kB)\n",
      "Requirement already satisfied: cffi>=1.17.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from gevent->geventhttpclient>=2.3.1->locust) (1.17.1)\n",
      "Requirement already satisfied: pycparser in c:\\programdata\\anaconda3\\lib\\site-packages (from cffi>=1.17.1->gevent->geventhttpclient>=2.3.1->locust) (2.21)\n",
      "Downloading locust-2.32.5-py3-none-any.whl (1.2 MB)\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   ----------------- ---------------------- 0.5/1.2 MB 5.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.2/1.2 MB 5.1 MB/s eta 0:00:00\n",
      "Downloading ConfigArgParse-1.7-py3-none-any.whl (25 kB)\n",
      "Downloading Flask_Cors-5.0.0-py2.py3-none-any.whl (14 kB)\n",
      "Downloading Flask_Login-0.6.3-py3-none-any.whl (17 kB)\n",
      "Downloading geventhttpclient-2.3.3-cp312-cp312-win_amd64.whl (48 kB)\n",
      "Downloading psutil-6.1.1-cp37-abi3-win_amd64.whl (254 kB)\n",
      "Downloading gevent-24.11.1-cp312-cp312-win_amd64.whl (1.5 MB)\n",
      "   ---------------------------------------- 0.0/1.5 MB ? eta -:--:--\n",
      "   ---------------------------------- ----- 1.3/1.5 MB 6.1 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.5/1.5 MB 5.9 MB/s eta 0:00:00\n",
      "Downloading greenlet-3.1.1-cp312-cp312-win_amd64.whl (299 kB)\n",
      "Downloading zope.event-5.0-py3-none-any.whl (6.8 kB)\n",
      "Installing collected packages: zope.event, psutil, greenlet, ConfigArgParse, gevent, geventhttpclient, Flask-Login, Flask-Cors, locust\n",
      "Successfully installed ConfigArgParse-1.7 Flask-Cors-5.0.0 Flask-Login-0.6.3 gevent-24.11.1 geventhttpclient-2.3.3 greenlet-3.1.1 locust-2.32.5 psutil-6.1.1 zope.event-5.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  WARNING: The script locust.exe is installed in 'C:\\Users\\aarthidurgesh\\AppData\\Roaming\\Python\\Python312\\Scripts' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\n"
     ]
    }
   ],
   "source": [
    "pip install locust\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3310bc7f-df39-44e9-bde6-fc72d8107332",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'zope.event'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mlocust\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m HttpUser, TaskSet, task\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mclass\u001b[39;00m \u001b[38;5;21;01mUserBehavior\u001b[39;00m(TaskSet):\n\u001b[0;32m      4\u001b[0m     \u001b[38;5;129m@task\u001b[39m\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mpredict\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\locust\\__init__.py:16\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m os\u001b[38;5;241m.\u001b[39mgetenv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLOCUST_SKIP_MONKEY_PATCH\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m):\n\u001b[0;32m     14\u001b[0m     \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgevent\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m monkey, queue\n\u001b[1;32m---> 16\u001b[0m     monkey\u001b[38;5;241m.\u001b[39mpatch_all()\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m os\u001b[38;5;241m.\u001b[39mgetenv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mLOCUST_SKIP_URLLIB3_PATCH\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m):\n\u001b[0;32m     19\u001b[0m         \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01murllib3\u001b[39;00m\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\gevent\\monkey\\__init__.py:656\u001b[0m, in \u001b[0;36mpatch_all\u001b[1;34m(socket, dns, time, select, thread, os, ssl, subprocess, sys, aggressive, Event, builtins, signal, queue, contextvars, **kwargs)\u001b[0m\n\u001b[0;32m    653\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m k, v \u001b[38;5;129;01min\u001b[39;00m modules_to_patch\u001b[38;5;241m.\u001b[39mitems():\n\u001b[0;32m    654\u001b[0m     \u001b[38;5;28mlocals\u001b[39m()[k] \u001b[38;5;241m=\u001b[39m v\n\u001b[1;32m--> 656\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mgevent\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m events\n\u001b[0;32m    657\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    658\u001b[0m     _notify_patch(events\u001b[38;5;241m.\u001b[39mGeventWillPatchAllEvent(modules_to_patch, kwargs), _warnings)\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python312\\site-packages\\gevent\\events.py:75\u001b[0m\n\u001b[0;32m     72\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mzope\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01minterface\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Attribute\n\u001b[0;32m     73\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mzope\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01minterface\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m implementer\n\u001b[1;32m---> 75\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mzope\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mevent\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m subscribers\n\u001b[0;32m     76\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mzope\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mevent\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m notify\n\u001b[0;32m     80\u001b[0m \u001b[38;5;66;03m#: Applications may register for notification of events by appending a\u001b[39;00m\n\u001b[0;32m     81\u001b[0m \u001b[38;5;66;03m#: callable to the ``subscribers`` list.\u001b[39;00m\n\u001b[0;32m     82\u001b[0m \u001b[38;5;66;03m#:\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     89\u001b[0m \u001b[38;5;66;03m#: This is an alias for `zope.event.subscribers`; prefer to use\u001b[39;00m\n\u001b[0;32m     90\u001b[0m \u001b[38;5;66;03m#: that attribute directly.\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'zope.event'"
     ]
    }
   ],
   "source": [
    "from locust import HttpUser, TaskSet, task\n",
    "\n",
    "class UserBehavior(TaskSet):\n",
    "    @task\n",
    "    def predict(self):\n",
    "        headers = {'Authorization': 'Bearer your_jwt_token'}\n",
    "        self.client.post(\n",
    "            \"/predict\",\n",
    "            json={\"features\": [34, 1, 120, 80, 1.2, 0, 1]},\n",
    "            headers=headers\n",
    "        )\n",
    "\n",
    "class WebsiteUser(HttpUser):\n",
    "    tasks = [UserBehavior]\n",
    "    min_wait = 1000\n",
    "    max_wait = 3000\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "116a37c9-cbcc-4459-9c09-89e8fd642e56",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (530232053.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[3], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    locust -f locustfile.py --host=http://127.0.0.1:5000\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "locust -f locustfile.py --host=http://127.0.0.1:5000\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "deeedd11-5818-4083-8541-f12a979c3858",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6ecd955-b1cc-4907-ab08-9b3b21a63452",
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
