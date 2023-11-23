server {
    listen 80;
    server_name rekikeng.com www.rekikeng.com;

    location / {
        include proxy_params;
        proxy_pass  http://127.0.0.1:4200;
    }
}
