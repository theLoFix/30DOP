# Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this issue. Once you have written to the log file, reraise the original exception.

def log_exception(exception, fn, **kwargs):
	values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
	
	with open("log.txt", "a") as log_file:
		log_file.write(f"Exception: {exception}, Function: {fn}, Values: {values}\n")
		

def itemgetter(collection, identifier):
	try:
		return collection[identifier]
	except (IndexError, KeyError, TypeError) as ex:
		log_exception(ex, "itemgetter", collection=collection, identifier=identifier)
		raise
