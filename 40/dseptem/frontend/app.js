var myApp = angular.module("myApp", ["ngRoute", "ngResource", "myApp.services"]);

var services = angular.module("myApp.services", ["ngResource"])
services
.factory('Tweet', function($resource) {
    return $resource('http://localhost:5000/api/tweets/:id', {id: '@id'}, {
        get: { method: 'GET' },
        delete: { method: 'DELETE' }
    });
})
.factory('Tweets', function($resource) {
    return $resource('http://localhost:5000/api/tweets', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST', }
    });
})
.factory('Search', function($resource) {
    return $resource('http://localhost:5000/api/search', {q: '@q'}, {
        query: { method: 'GET', isArray: true}
    });
});

myApp.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'pages/main.html',
        controller: 'mainController'
    })
    .when('/tweets', {
        templateUrl: 'pages/tweets.html',
        controller: 'tweetListController'
    })
    .when('/tweets/:id', {
        templateUrl: 'pages/tweet_details.html',
        controller: 'tweetDetailsController'
    })
});

myApp.filter('filterStyles', function() {
  return function(input) {
    var output = new Array();
    for (i=0; i<input.length; i++) {
        if (input[i].checked == true) {
            output.push(input[i].name);
        }
    }
    return output;
  }
});

myApp.controller(
    'mainController',
    function ($scope, Search) {
        $scope.search = function() {
            q = $scope.searchString;
            if (q.length > 1) {
                $scope.results = Search.query({q: q});    
            }
        };
    }
);

myApp.controller(
    'tweetListController',
    function ($scope, Tweets, Tweet, $location, $timeout) {
        if ($location.search().hasOwnProperty('created')) {
            $scope.created = $location.search()['created'];
        }
        if ($location.search().hasOwnProperty('deleted')) {
            $scope.deleted = $location.search()['deleted'];
        }
        $scope.tweets = Tweets.query();
    }
);

myApp.controller(
    'tweetDetailsController', ['$scope', 'Tweet', '$routeParams',
    function ($scope, Tweet, $routeParams) {
        $scope.tweet = Tweet.get({id: $routeParams.id});
    }
]);

