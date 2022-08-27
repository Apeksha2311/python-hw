<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
       


        

    <script src="myScript.js">

    </script>

    </head>
    

    <body ng-app="myModule">
        <div ng-controller="myController">
            <input type="checkbox" ng-module="hidesalary">Hide</input><br>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Gender</th>
                        <th>City</th>
                        <th ng-hide="hidesalary">Salary</th>
                    </tr>
                </thead>
                <tbody>
                    <tr ng-repeat="emp in employees">
                        <td>{{emp.name}}</td>
                        <td>{{emp.gender}}</td>
                        <td>{{emp.city}}</td>
                        <td ng-show="hidesalary">####</td>
                        <td ng-hide="hidesalary">{{emp.salary}}</td>
                    </tr>
                </tbody>
            </table>
           

        </div>


   
</body>

</html>
