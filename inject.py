import marshal,zlib,base64
file = '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'

exec(marshal.loads(zlib.decompress(base64.b64decode(file.encode('utf-8')))))
