План на выступление enterprise observability.

Буду акцентировать внимание на OpenSource-инструментах, которые можно развернуть на своих машинах. SAAS решения для РФ, не РФ рынка просто думаю упомянуть.

4 части:
I. Логи
II. Метрики
III. Трейсинг
IV. Собираем вместе, смотрим на Grafana

I. Логи
Покажу подходы с разными библиотеками. Мой фаворит по 12 factors это stdout и json.

Loki

Рассмотрим как это запускать на:
1/ виртуалке Unix, физическом сервере

logging -> own.
Synchronous.

Logstash: https://github.com/vklochan/python-logstash


vector
Важно для небольших виртуалок (Не Java)

Ansible, Puppet

systemd
https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
https://vector.dev/docs/reference/configuration/sources/journald/


2/ Docker compose/swarm

https://vector.dev/docs/setup/installation/platforms/docker/
https://www.fluentd.org/guides/recipes/docker-logging


3/ Kubernetes-окружении
Собираем vector, отправляем http

II. Метрики
* Prometheus
* OpenTelemetry

Рассмотрим как это запускать на:
1/ виртуалке Unix, физическом сервере
2/ Docker compose/swarm
3/ Kubernetes-окружении

III. Трейсинг
* Jaeger
* OpenTelemetry

Рассмотрим как это запускать на:
1/ виртуалке Unix, физическом сервере
2/ Docker compose/swarm
3/ Kubernetes-окружении

IV. Собираем вместе, смотрим на Grafana
1/ Метрики, графики
2/ Крутим алерты

Вот в последней части как-то пока очень базово не-enterprise получается. Мне кажется по времени много не влезет. Если подумать как поджать остальное, может быть можно было про шаблонизацию дашбордов для проектов, каналы оповещений и работу с инцидентами. Но тут надо думать, темы не маленькие.
