INSTALLATION

git clone https://github.cerner.com/patient-portal/portal-startup-app.git

cd portal-startup-app

git checkout NH054808

pip install -r requirements.txt

cd tweet_finder

python manage.py makemigrations

python manage.py migrate

python manage.py runserver