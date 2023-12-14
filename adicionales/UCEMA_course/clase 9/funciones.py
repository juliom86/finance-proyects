# funciones

	# Editores de texto
		# Sublime
		# Atom
	# IDEs
		# VisualStudio Code
		# Spyder
		# Pycharm

def fecha(dia=None, mes=None, año=None, lang='es_ES', dias=0):
	"""Esta funcion te devuelve un diccionario con lo siguiente:
		- dias_faltantes: Es la cantidad de dias que faltan para la fecha dada
		- fecha_date: Es la fecha dada, en formato datetime.date
		- fecha_datetime: Es la fecha dada, en formato datetime.datetime
		- fecha_ISO
		- fecha_TXT: Formato lindo legible
		- fecha_timestamp


		Args:
		dia (Integer, optional): Es el dia dado, si no se pasa nada, se toma el dia actual
		mes (Integer, optional): Es el mes dado por el usuario, si no pone nada es el mes actual
		año (Integer, optional): Description
		lang (str, optional): Description
		dias= Es la cantidad de dias para la fecha necesaria (Ojo que si se pasa este dato no le damos bola al dia, mes y año)
	"""

	import datetime, locale
	locale.setlocale(locale.LC_ALL, lang)

	if dias==0:

		if not dia:
			dia = datetime.date.today().day
		if not mes:
			mes = datetime.date.today().month
		if not año:
			año = datetime.date.today().year

		fecha_date = datetime.date(año, mes, dia)
		fecha_datetime = datetime.datetime(año, mes, dia)
		dias_faltantes = (fecha_date - datetime.date.today()).days
		fecha_ISO = fecha_date.isoformat()
		fecha_timestamp = datetime.datetime.timestamp(fecha_datetime)
		fecha_TXT = f"{fecha_date.strftime('%A').title()} {dia} de {fecha_date.strftime('%B')} de {año}"

		r = {'dias_faltantes': dias_faltantes, 'fecha_date': fecha_date, 'fecha_datetime': fecha_datetime,'fecha_ISO': fecha_ISO,'fecha_timestamp': fecha_timestamp,'fecha_TXT': fecha_TXT}
	else:
		f = datetime.date.today() + datetime.timedelta(days=dias)
		dia, mes, año = f.day, f.month, f.year
		r = fecha(dia, mes, año)



	return r


