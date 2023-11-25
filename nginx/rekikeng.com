server {
    listen 80;
    server_name rekikeng.com www.rekikeng.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /root/rekikeng/static/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
