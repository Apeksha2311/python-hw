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









candidates.html
{% block body%}
 <div class="container">

    <!-- img -->
    <div class="container text-center">
      <img src="{{data.profile_image.url}}" alt="" height="150px">

    </div>
    <div class="py-2 border-bottom">
      <span>First Name:</span> <span>{{data.fname}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>Last Name:</span> <span>{{data.lname}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>Email Id:</span> <span>{{data.email}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>Contact:</span> <span>{{data.contact}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>Gender:</span> <span>{{data.gender}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>City:</span> <span>{{data.city}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>Date of birth:</span> <span>{{data.dob}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>State:</span> <span>{{data.state}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>Pin_no:</span> <span>{{data.pin}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>language:</span> <span>{{data.lang}}</span> 
    </div>

    <div class="py-2 border-bottom">
      <span>language Skills:</span> <span>{{data.lang_skills}}</span> 
    </div>
    <div class="py-2 border-bottom">
      <span>Prefered Location:</span> <span>{{data.prefered_loc}}</span> 
    </div>
    <div class="py-2 border-bottom">
      <span>Qualification</span> <span>{{data.qual}}</span> 
    </div>
    <div class="py-2 border-bottom">
      <span>projects</span> <span>{{data.projects}}</span> 
    </div>

    
 </div>

 {% endblock body%}
    
    
    
    
base.html
<body style="background-image: linear-gradient( 109.6deg, rgba(156,252,248,1) 11.2%, rgba(110,123,251,1) 91.1% );
    color:#333;
    font-size:1.5rem;
    ">
