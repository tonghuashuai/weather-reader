$.ws.onopen = ->
    $.ws.onmessage = (evt)->
        $('#msg').html(evt.data)
