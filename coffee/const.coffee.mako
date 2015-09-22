<%!
    from config import HOST, QINIU
    from model import const
    import json
%>

window.CONST = window.CONST or {}

CONST.HOST = '${HOST}'
CONST.ENUM = CONST.ENUM or {}
CONST.ENUM.BLOOD = ${const.BLOOD.to_dict()}
CONST.ENUM.DEGREE = ${const.DEGREE.to_dict()}
CONST.QINIU_HOST = '${QINIU.HOST}'
