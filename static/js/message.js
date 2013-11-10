angular.module('message-app',[]).config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    }
).controller("messageController", function($scope, $http){
  $scope.messages = [];
  function getMessage() {
    $http.get('/note/service/allnotes').success(function(data){
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
                });
                $scope.messages = data.results;
            });
  }
  getMessage()
  $scope.addMessage = function() {
      var note = {}
      note.author = $scope.author;
      note.content = $scope.newMessage;
      $http.post("/note/service/put", note).success(function(){
          getMessage();
      });

      $scope.newMessage = '';
      $scope.author = '';
    };
});