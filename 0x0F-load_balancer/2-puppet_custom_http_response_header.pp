# Add new header with puppet

exec { 'add X-Served-By header':
    command => 'sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME always;\n" /etc/nginx/sites-available/default;
                sudo service nginx restart',
    provider => 'shell',
}
