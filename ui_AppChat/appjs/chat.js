angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        var thisCtrl = this;

        this.messageList = [];

        this.loadMessages = function(){
            // Get the messages from the server through the rest api
            // THis function will load all the messages in the DB

            var messageID = $routeParams.mID;
            var reqURL = "http://localhost:5000/messages";
            console.log(" reqURL"+ reqURL)
            $http.get(reqURL).then(
                function(response){
                    console.log(" data:" + JSON.stringify(response.data));

                },
                //error function
                function(response){
                var status = response.status;
                if(status == 0){
                alert("No hay conexion a internet");
                }
                else if(status == 404){
                alert("Su seccion expiro")
                }
                else{
                alert("Error del sistema")
                }
              }
            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});
            thisCtrl.newText = "";
        };

        this.loadMessages();
}]);
