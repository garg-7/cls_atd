# cls_atd
Photographic Classroom Attendance System made for 4th semester B.Tech Project under the guidance of Prof. Anand Mishra


## Getting Started
* Navigate to the cloned repository.
```
cd cls_atd
```
### Backend Setup

* Download the LightCNN-29 v2 model of [LightCNN](https://github.com/AlfredXiangWu/LightCNN) and place it in `src/api/LightCNN`

* Set up and activate a virtual environment
```
sudo apt-get install -y python3-venv
python3 -m venv env
source env/bin/activate
```
* Use pip to install other dependencies from `requirements.txt` 
```
pip install -r requirements.txt
```

* Navigate to `src` folder
```
cd src
```
* Make database Migrations 
```
python manage.py makemrations
python manage.py migrate
```
* Run the backend server 
```
python manage.py runserver --nothreading --noreload
```
The backend must now be running on `localhost:8000`

### Frontend Setup

Note: `npm` must be installed in the computer

* In a new terminal window navigate to `frontend` folder
```
cd frontend
```

* Install dependencies from `package.json`
```
npm install
```

* Run development server 
```
npm run serve 
```

The frontend of the application must now be running at `localhost:8080`
