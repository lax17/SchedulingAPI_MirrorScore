# SchedulingAPI_MirrorScore

<b>Scheduling API:</b> This involves a single endpoint, which accepts Date-Time and a URL as a parameter.When the API is called, a task will be scheduled. A GET request (no parameters needed) should be sent on the URL specified (second parameter), when the current Date-Time matches the one specified in the Date-Time parameter (first parameter). "The GETrequest on the URL parameter will only return a status code, and no response body" task is invoked.

<b> Validation on parameter:<b>
 
<img width="850px" alt="validation_applied" src="https://user-images.githubusercontent.com/41922928/104103453-33bea100-52c8-11eb-9f63-4f2c7654fdf4.PNG">



<b>Scheduling Task is done Using Django Management Command and Cron</b>

      Using this method you dont have to install any libraries or packages.

<b>Creating a Django Management Command </b>

  The first thing we will be doing is create a custom django management command. To do this, just add a management/commands directory to the application. Django will register a   manage.py command for each Python module in that directory whose name doesn’t begin with an underscore. more info refer : https://django.cowhite.com/blog/scheduling-taks-in-django/
  
<b>Successful Request-Response </b>

<img width="850px" alt="scheduleapi" src="https://user-images.githubusercontent.com/41922928/104103650-41c0f180-52c9-11eb-805b-99074c76c0ee.PNG">

<hr/>

<b> PING API </b> 

    A separate ping endpoint must be created, to know that the server is alive. Whenever a GET request is sent to the '/ping' endpoint, the server must return a JSON "        {"status":"OK"}". 


  <b> When server is alive </b>

   <img width="850px" alt="okresponsse" src="https://user-images.githubusercontent.com/41922928/104103738-bb58df80-52c9-11eb-8488-0869a2796498.PNG">


  <b> When server is  not live </b>

   <img width="850px" alt="pingfailure" src="https://user-images.githubusercontent.com/41922928/104103768-d592bd80-52c9-11eb-920c-6005ecbf4b78.PNG">



<b> Instruction to run Project </b>

    step1: git clone https://github.com/lax17/SchedulingAPI_MirrorScore/

    step2: cd SchedulingAPI_MirrorScore/ScheduleTask/

    step3: python manage.py runserver








