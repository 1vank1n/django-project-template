# coding: utf-8
from fabric.api import env, cd, run, prefix

env.hosts = ['web@ip.ip.ip.ip']
env_prefix = prefix('source /web/.../.env/bin/activate')


def deploy():
    with cd('/web/...'):
        run('git pull')
        with env_prefix:
            # run('pip install -r req.txt')
            run('python ./manage.py migrate')
            run('python ./manage.py collectstatic --noinput')
    run('touch /tmp/...')
