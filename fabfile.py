from fabric.api import *
from fabric.contrib.files import upload_template

env.hosts = ['54.191.70.60']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/r_blog_analytics.pem'
env.shell = "/bin/bash -l -i -c"
env.use_ssh_config = True
env.project_name = "rocketu_blog_analytics"

from fabric.colors import *
from fabric.decorators import task
from fabric.operations import local


def restart_app():
    sudo("service supervisor restart")
    sudo("service nginx restart")


@task
def deploy():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/ru_blog_analytics"):
            run("git pull origin master")
            run("pip install -r requirements.txt")
            run("python manage.py migrate")
            run("python manage.py collectstatic --noinput")
    restart_app()


@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))


@task
def setup_nginx(project_name, server_name):
    """
    $ fab setup_nginx:rocketu_blog_analytics,54.191.70.60
    :param project_name:
    :param server_name:
    :return:
    """
    upload_template("./deploy/nginx.conf",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)
    restart_app()


@task
def setup_gunicorn(project_name, proc_name):
    """
    project name and proc name should be the same,
    but are not in my example
    $ fab setup_gunicorn:ru_blog_analytics,rocketu_blog_analytics
    :param project_name:
    :param proc_name:
    :return:
    """
    upload_template("./deploy/gunicorn.conf.py",
                    "{}/gunicorn.conf.py".format(project_name),
                    {'proc_name': proc_name},
                    )
    restart_app()

@task
def setup_supervisor(project_name, server_name):
    """

    Need to finish
    https://students.rocketu.com/week8/2_pm/#/9

    :param project_name:
    :param server_name:
    :return:
    """
    upload_template("./deploy/supervisor.conf",
                    "/etc/supervisor/conf.d/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)
    restart_app()


# @task
# def ubuntu_hello():
#     run("lsb_release -a")

@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))



@task
def hello():
    print("I'm alive!")


@task
def goodbye():
    print(green("I'm alive!"))

@task
def create_file(file_name):
    local("touch ~/Desktop/{}.txt".format(file_name))

@task
def create_dir(pathname, dir_name):
    local("mkdir ~/{}/{}".format(pathname, dir_name))
