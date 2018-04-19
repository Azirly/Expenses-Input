Start Time: 11:15 AM 4/19/2018

EXPENSES INPUT:
#### Problem:
Design a web application that takes in the date, value, and reason of an expense and puts it into a list.
This web application should then output a list of expenses, each with the date, 20% of the value of the expense, and reason for the expense

#### How to run: (Using Windows)
1. Open command prompt and go to the “Expense_Input” outer folder
2. Run ```python manage.py runserver``` on the server
3. Go to ```http://localhost:8000/userinput/```

#### Requirements
1. Front-End 
<br>    a. Django
2. Back-End (Solution is more back-end focused)
<br>    a. Django
<br>    b. MySQL
<br>    c. Data structure of the table
<br>        ```
        [date of expense | 20% of expense | reason for expense]
        ```
<br>    d. SQL Details       
        ```
        TABLE "userinput_expense" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date" datetime NOT NULL, "value" integer NOT NULL, "reason" varchar(500) NOT NULL);
         ```
#### Final Thoughts
1. 
2. If I had more time, would have ran the application on large-scale "dummy data".
        
