cd /web/project/
source /web/project/.env/bin/activate
git pull
pip install -r requirements.txt
python ./manage.py migrate
python ./manage.py collectstatic --noinput
# python ./manage.py test
touch /tmp/project.il-studio.ru
