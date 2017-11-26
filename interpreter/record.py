import interpreter.tools
import base64

def file(audio_data):
	filename = "./interpreter/data/" + interpreter.tools.randwavefile()
	with open(filename, "wb") as fh:
		fh.write(base64.decodebytes(audio_data))
	return filename