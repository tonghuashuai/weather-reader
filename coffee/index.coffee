$.ws.onopen = ->
    $.ws.onmessage = (evt)->
        data = $.parseJSON(evt.data)
        ops = parseInt(data.ops)
        msg = data.msg
        if ops == CONST.ENUM.OPS_CATAGORY.MSG
            $('#msg').html(msg)
            
        else if ops == CONST.ENUM.OPS_CATAGORY.OPS
            if msg == 'reload'
                location.reload()
            else if msg == 'refresh'
                console.log 'refresh data'

