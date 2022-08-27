var myapp = angular.module("myModule",[]);

myApp.controller("mycontroller",function($scope)
{ var employees =[
    {
        name:"alpha",gender:"Male",city:"london",salary:50000
    },
    {
        name:"Beta",gender:"Female",city:"Paris",salary:50000
    },
    {
        name:"alpha",gender:"Male",city:"london",salary:50000
    }
];
   $scope.employees=employees;







}
);
