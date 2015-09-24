def_view(
    'OpsApp',
    'OpsCtrl',
    ($scope) ->
        o = {}
        o.msg = ''
        o.ops = CONST.ENUM.OPS_CATAGORY.MSG.toString()

        $scope.o = o

        $scope.submit =->
            $.ws.send(o.msg)
)
