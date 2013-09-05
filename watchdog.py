import urllib
import json
from subprocess import call
import logging

LOG_FILENAME = '/var/log/watchdog.log'
CONF_FILENAME = '/etc/watchdog.conf'
RUN_FILENAME = '/var/run/watchdog.run'
FORMAT = '%(asctime)-15s - %(message)s'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format=FORMAT,)

try: #se arquivo nao existe criar arquivo
	f = open(RUN_FILENAME, 'r')
	var = json.load(f)
except (IOError, ValueError):
	aux = '{"tentativas": 0}'
	var = json.loads(aux)
try:
	f = open(RUN_FILENAME, 'w+')
	fconf = open(CONF_FILENAME, 'r')
	
	#parsing dos arquivos json
	conf = json.load(fconf)
	max_tentativas = conf['max_tentativas']
	url = conf['url']
	tentativas = var['tentativas']

	#abre arquivo modo escrita
	f = open(RUN_FILENAME, 'w+')

	#checagem
	status_code = urllib.urlopen(url).getcode()
	if status_code != 200:
		if tentativas < max_tentativas:
			var['tentativas'] += 1
		else:
			logging.warning('Numero limite de tentativas atingido, reiniciando PHP5-FPM')
			var['tentativas'] = 0
			call(["service", "php5-fpm", "restart"])
	else:
		var['tentativas'] = 0
	# salva o arquivo
	json.dump(var,f)
except Exception:
	logging.exception('Erro ao executar Watchdog:')
	exit(1)