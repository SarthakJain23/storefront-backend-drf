echo "BUILD STARTED...."
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py makemigrations
python3.9 manage.py migrate
gunicorn storefront.wsgi
echo "BUILD ENDED...."