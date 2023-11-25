from fabric import task

hosts = [dict(user='root', host='159.65.196.39')]


@task(hosts=hosts)
def execute(c):
    c.run('/etc/')


@task(hosts=hosts)
def setup_nginx(c):
    """
    Setup Nginx for serving the website.
    """
    c.run('chown -R root:www-data /root/rekikeng/static')
    c.run('sudo chmod -R 755 /root/rekikeng')
    c.run('sudo chmod -R 755 /root/rekikeng/static')
    c.run("apt-get -y install nginx")
    c.put("./nginx/rekikeng.com", "/etc/nginx/sites-available/")
    c.run("ln -sf /etc/nginx/sites-available/rekikeng.com /etc/nginx/sites-enabled")
    check = c.run("nginx -t")
    if check.ok:
        c.run("systemctl restart nginx")
        c.run("ufw allow 'Nginx Full'")


@task(hosts=hosts)
def nginx_logs(c):
    c.run('tail -F /var/log/nginx/error.log')


@task(hosts=hosts)
def reload_service(c):
    c.run('systemctl daemon-reload')
    c.run('systemctl restart rekikeng')


@task(hosts=hosts)
def setup_ssl(c):
    """
    Setup SSL certificate using Let's Encrypt.
    """
    c.run("snap install core && snap refresh core")
    c.run("snap install --classic certbot", pty=True)
    c.run("ln -sf /snap/bin/certbot /usr/bin/certbot")
    c.run("certbot --nginx -d rekikeng.com -d www.rekikeng.com", pty=True)
    c.run("systemctl status snap.certbot.renew.service")


@task(hosts=hosts)
def createsuperuser(c):
    """
    Create a superuser account using Django management command.
    """
    with c.cd('rekikeng'):
        with c.prefix('source venv/bin/activate'):
            c.run('./manage.py createsuperuser', pty=True)