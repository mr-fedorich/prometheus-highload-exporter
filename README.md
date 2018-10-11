# prometheus-highload-exporter
Exporter for prometheus. Monitoring of heavy processes that load memory and cpu. Toplist.

Displays the TOP of the heaviest requests that will load the server. Facilitates work in detecting problems on the server. Now you do not need to view large log files, just look at the graph and understand which process or daemon (with parameters) loads the system.

![Grafana Example Dashboard](https://github.com/mr-fedorich/prometheus-highload-exporter/raw/master/images/highload.png)

1. Put in to: /usr/local/sbin/highload-exporter.py
2. In the script edit the path parameter: path = "/var/lib/prometheus/node_exporter/textfile_collector/"
3. Add to cronjob

```sh
* * * * * /usr/local/sbin/highload-exporter.py top_cpu_cmd cpu
* * * * * /usr/local/sbin/highload-exporter.py top_mem_cmd mem
```
In the source file with metrics will be like

/var/lib/prometheus/node_exporter/textfile_collector/cpu.prom
/var/lib/prometheus/node_exporter/textfile_collector/mem.prom

```sh
top_cpu_cmd{metric="php",cmd="php /var/www/libraries/htdocs/app/bin/console brand"} 15.2
top_cpu_cmd{metric="php",cmd="php /var/www/libraries/htdocs/app/bin/console brand"} 12.3
top_cpu_cmd{metric="php-fpm:",cmd="php-fpm: pool www"} 3.7
top_cpu_cmd{metric="php-fpm:",cmd="php-fpm: pool www"} 3.1
top_cpu_cmd{metric="php-fpm:",cmd="php-fpm: pool www"} 2.3
top_cpu_cmd{metric="php-fpm:",cmd="php-fpm: pool www"} 1.7
top_cpu_cmd{metric="php-fpm:",cmd="php-fpm: pool www"} 1.7
top_cpu_cmd{metric="php-fpm:",cmd="php-fpm: pool www"} 1.6
```

4. Screw to grafana (query: top_mem_cmd{group='production'})
5. Enjoy
