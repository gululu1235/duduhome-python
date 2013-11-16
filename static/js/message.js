angular.module('message-app',['infinite-scroll']).config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    }
).controller("messageController", function($scope, $http){
  $scope.messages = [];
  var current_id = -1;
  var busy = false;
  function getMessage(id, refresh) {
    if (busy) return;
    busy = true;
    $http({method: 'GET', url: '/note/service/get_notes', params: {start_id: id}}).success(function(data){
                data.results.forEach(function (message){
                    if (message.author.substring(0,2) == 'da'){
                        message.style = 'dadu';
                    }
                    else if (message.author.substring(0, 4) == 'xiao') {
                        message.style = 'xiaodu';
                    }
                    else {
                        message.style = 'xiaodu';
                    }
                    message.icon = message.author
                    if (current_id < 0)
                        current_id = message.id;
                    else if (current_id > message.id) {
                        current_id = message.id
                    }

                });
                if (refresh) {
                    $scope.messages = data.results;
                }
                else {
                    $scope.messages = $scope.messages.concat(data.results);
                }
                busy = false;
            });
  }
  getMessage(-1, true);
  $scope.loadMoreMsg = function(){
      getMessage(current_id);
  }
  $scope.addMessage = function() {

      var note = {}
      note.author = $scope.author;
      note.content = $scope.newMessage;
      $http.post("/note/service/put", note).success(function(){
          getMessage(-1, true);
      });

      $scope.newMessage = '';
      $scope.author = '';
    };
});