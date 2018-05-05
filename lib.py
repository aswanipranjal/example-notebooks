from functools import partial

from json import dump, JSONDecoder


def parse_json(fileobj, decoder=JSONDecoder(), buffersize=2048):
    """
    A function to parse the JSON file and return JSON objects in the file
    """
    buffer = ''
    for chunk in iter(partial(fileobj.read, buffersize), ''):
        buffer += chunk
        while buffer:
            try:
                result, index = decoder.raw_decode(buffer.strip("\n\t"))
                yield result
                buffer = buffer[index:]
                
            except ValueError:
                # Not enough data to encode, read more data
                break