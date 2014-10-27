var scrooge = angular.module('scrooge.controllers', ['scrooge.services']);

scrooge.controller('MainMenuCtrl', ['$scope', '$location', 'MainMenu', function ($scope, $location, MainMenu) {
    $scope.stats.subMenus = MainMenu.items.get();
    $scope.stats.subMenus.$promise.then(function (subMenus) {
        subMenus.forEach(function (element) {
            if (element.name == $scope.stats.currentSubMenu) {
                $scope.stats.currentSubMenu = element
            }
        })
    })
    $scope.setActive = function(obj) {
        $scope.stats.currentSubMenu = obj
        if ($scope.stats.inArray($scope.stats.currentLeftMenu, $scope.stats.currentSubMenu.leftMenu) == false) {
            $scope.stats.currentLeftMenu = $scope.stats.getFirstExistMenu()
        }
    }
}]);
