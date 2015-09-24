<%!
    from config import HOST, HOST_, QINIU
    from model import const
    import json
%>

window.CONST = window.CONST or {}

CONST.HOST = '${HOST}'
CONST.HOST_ = '${HOST_}'
CONST.ENUM = CONST.ENUM or {}
CONST.ENUM.OPS_CATAGORY = ${const.OPS_CATAGORY.to_dict()}
CONST.QINIU_HOST = '${QINIU.HOST}'
