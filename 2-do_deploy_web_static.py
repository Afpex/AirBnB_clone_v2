#!/usr/bin/python3
"""Deploy the web static"""
from fabric.api import run, put, env
import os


env.hosts = ['34.207.190.92', '54.236.45.84']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """function to deploy the code"""
    fil = os.path.basename(archive_path)
    folder = fil.replace(".tgz", "")
    path = "/data/web_static/releases/{}/".format(folder)
    yes = False
    if os.path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            run("mkdir -p {}".format(path))
            run("tar -xzf /tmp/{} -C {}".format(fil, path))
            run("rm -rf /tmp/{}".format(fil))
            run("mv {}web_static/* {}".format(path, path))
            run("rm -rf {}web_static".format(path))
            run("rm -rf /data/web_static/current")
            run("ln -sf {} /data/web_static/current".format(path))
            print('Ran SUccesfully')
            yes = True
        except Exception as e:
            print(e)
            yes = False
    else:
        return (False)
    return (yes)
