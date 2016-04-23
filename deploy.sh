cd /web/project/
source /web/project/.env/bin/activate
git pull
pip install -r requirements/staging.txt
python ./manage.py migrate
python ./manage.py collectstatic --noinput
# python ./manage.py test
touch /tmp/project.il-studio.ru
