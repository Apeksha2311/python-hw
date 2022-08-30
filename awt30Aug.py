<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
        <script src="scripts/myScript.js"></script>

    </head>
    <body ng-app="md">
        <div ng-controller="ctrl">
            {{8-67}}
            <ul>
                <li ng-repeat="country in countries" ng-init="parentIndex=$index">
                    {{country.name}}

                    <ul>
                        <li ng-repeat="city in country.cities">
                            {{city.name}}-parentIndex={{parentIndex}},Index={{$index}}
                        </li>
                    </ul>
                </li>
            </ul>





        </div>
       
        
    </body>
</html>
