import logging
logger = logging.getLogger(__name__)


def str_encode(value='', encoding=None, errors='strict'):
    logger.debug("Encode str {} with and errors {}".format(value, encoding, errors))
    return str(value, encoding, errors)


def str_decode(value='', encoding=None, errors='strict'):
    if isinstance(value, str):
        return bytes(value, encoding, errors).decode('utf-8')
    elif isinstance(value, bytes):
        # 解决 windows-874 解码, cp874 = windows-874 别名
        _encoding = 'cp874' if encoding == 'windows-874' else encoding
        # return value.decode(encoding or 'utf-8', errors=errors)
        # 解决 viscii 编码异常
        _encoding = 'utf-8' if _encoding == 'viscii' else _encoding
        return value.decode(_encoding or 'utf-8', errors=errors)
    else:
        raise TypeError("Cannot decode '{}' object".format(value.__class__))
