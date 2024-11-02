echo "BUILD STARTED...."
sudo apt install python3-pip
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py makemigrations
python3.9 manage.py migrate
gunicorn storefront.wsgi
celery -A storefront worker -l info
echo "BUILD ENDED...."