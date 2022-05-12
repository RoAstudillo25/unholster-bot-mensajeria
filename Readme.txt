
Para crear un venv : python3 -m env (nombre del entorno virtual)

Para activar env.  : source env/bin/activate
		    python3 main.py
		    "introducir mensaje a traves de input"

Para desactivar.   :  deactivate

* Para ejecutar el bot a través de la terminal

curl -X POST -H 'Content-type: application/json' --data '{"text":Este es un mensaje enviado , World!"}' https://hooks.slack.com/services/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