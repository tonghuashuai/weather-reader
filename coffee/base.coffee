$.fn.extend(
    parallax: ->
        scroll_top = $(window).scrollTop()
        self = $(this)
        ratio = parseFloat(self.data('parallax-background-ratio'))
        self.css('background-position', "center #{scroll_top * ratio}px")
)

$('.to-top').click ->
    $("html,body").animate({scrollTop: $("#top").offset().top - 100}, 500)


$("#footer-sns #weixin").poshytip({
    className: 'tip-twitter',
    alignTo: 'target',
    alignX: 'center',
})


pathname = location.pathname
$("#navbar>ul>li").removeClass('active')
$("#navbar>ul>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')

window.def_view = (module, ctrl, fun)->
    app = angular.module(module, ["ngSanitize"]).controller ctrl, fun

    app.filter('deal_str', ->
        return $.deal_str
    )

    # angular js debug method
    window.V = ()->
        return angular.element($("[ng-controller=#{ctrl}]")).scope()


    return app


$(".nav>li").removeClass('active')
$(".nav>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')

$('.table-expandable>tbody>tr>td>a.open').click ->
    obj = $(this).parent('td').parent('tr').next()
    if obj.attr('class') and obj.attr('class').indexOf('collapse') >= 0
        if obj.css('display') == 'none'
            obj.slideDown()
        else
            obj.slideUp(0)



$.postJSON = (url, data, callback) ->
    $.ajax(
        url: url
        data: data
        type: 'post'
        success: (o)->
            if o.err
                $.alert_fail o.err.msg
            else
                callback o
        error: (o)->
            $.alert_fail()
    )

$.deal_str = (str)->
    r = new RegExp('>', 'g')
    str = str.replace(r, '&gt;')

    r = new RegExp('<', 'g')
    str = str.replace(r, '&lt;')
   
    str = str.replace(/\n/g, "</p><p>")

    return "<p>#{str}</p>"

$.alert_success = (msg='操作成功', callback)->
    dialog = BootstrapDialog.show({
        title: '提示',
        type: 'type-success',
        message: msg
        buttons: [{
            label: '关闭',
            action: (dialogItself)->
                dialogItself.close()
        }]
        onhidden: ->
            if callback
                callback()
    })
    
    setTimeout(->
        dialog.close()
    , 2000)


$.alert_fail = (msg='操作失败')->
    dialog = BootstrapDialog.show({
        title: '提示',
        type: 'type-danger',
        message: msg
        buttons: [{
            label: '关闭',
            action: (dialogItself)->
                dialogItself.close()
        }]
        onhidden: ->
            if callback
                callback()
    })

$.confirm = (callback, msg='确定？') ->
    BootstrapDialog.confirm(msg, (result)->
            if result
                if callback
                    callback()
    )


myElement = document.querySelector("header")

if myElement
    headroom  = new Headroom(myElement, {
                        tolerance: {
                          down : 10,
                          up : 20
                        },
                        offset : 30
                    })

    headroom.init()
