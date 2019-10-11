FlaskMongoDB Application using PyMongo
---
+ A student registration form created in Flask framework.
+ student can register by entering all the details like name, rollno, emailid, standard, and password. All the details stored in mongodb.
+ Post login into the student account, it welcomes to the students workspace.

---
To run the Application:

+ create a python virtualenvironment by using : virtualenv <nameofthevenv>

+ Activate the virtualenv : source ./bin/activate

+ Initialize the Git project named "FlaskMongoAssignment"

+ Requirements for this application (tried on ubuntu 18.04):
            - Python 2.7.15+
            - Flask 1.1.1
            - Werkzeug 0.16.0
            - Virtualenv 15.1.0
            - pymongo==3.8.0
            - pip 9.0.1
            - mongo v4.0.10
            


+ Install the dependencies required to execute this application on your local system:
     
     pip install <dependencyname> 


+ Check the status of the mongod server: service mongod status

+ Start the mongo server : service mongod start

+ At local system the mongo server : mongo "mongodb+srv://sheetalkcluster-xtvj5.mongodb.net/test"  --username SheetalK01
     need to enter password: <ur passowrd>

+ Execute the following flask project:

    flask run


---
note : Also created a mongodb on https://cloud.mongodb.com . The snapshot is also attached with the same. The database created named "school" with the "students" collection which stores the registered student details.
 
