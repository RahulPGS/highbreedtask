# HighBreed Python and Django Task

Submitted by _**Rahul Pinjarla**_ , _S160142@rguktsklm.ac.in_

Two start the project open command prompt into the project directory.
The directory is the folder where the manage.py is located.

Then open any virtual env if you are an virtual env user.

Then install all the packages from the **requirements.txt**.

If you are pipenv user enter the following command to install all the packages.

`pipenv install`

Now, go to the [Chrome driver page](https://chromedriver.chromium.org/downloads) and download your chrome driver which supports the chrome version on your device.
Extract the zip file to get the exe file in it.

Set that chrome driver exe path to the CHROME_DRIVER_PATH variable in **settings.py** file

`CHROME_DRIVER_PATH = Your chromedriver.exe path here`

After that enter the following command which fires up the project in the localhost server with port 8000

`python manage.py runserver`

Now you can visit the project home page by entering the below url in the browser.

[http://localhost:8000](http://localhost:8000)

This task contains a Django project with two apps.

The home page will contain the link to both the app pages provided in the project.


#### App \#1

### App Searcher

You can visit the app searcher page by entering the below url in the browser after firing the localhost server.

[http://localhost:8000/appsearch](http://localhost:8000/appsearch)

This is a web app that fetches data from the Apple app store or Google play store.

The page provides a dropdown that allows users to select app store or playstore.

After selecting the store the required input fields for the app will appear and upon entering the details the user can hit get details of the app if the details are valid.

##### App store

For app store the input fields for the name and id of the app will appear.

Example:

for the app Spotify the app store url is 
 
 [https://apps.apple.com/us/app/spotify-discover-new-music/id324684580]()

the name will be **spotify-discover-new-music** and the id will be **324684580**
##### Play store
For play store the input field for package name of the app will appear.
 
 for the app Spotify the play store url is
 
 [https://play.google.com/store/apps/details?id=com.spotify.music]()
 
the package name will be **com.spotify.music**

Enter these details in the appeared input field(s) to get the app details.

#### App \#2

### Keyword finder

You can visit the keyword finder page by entering the below url in the browser after firing the localhost server.

[http://localhost:8000/findkeywords](http://localhost:8000/findkwywords)

This app takes a URL and fetch the keyword, description and og:description content and display them to the user.

A input field will be provided in the page where the user can enter the URL.

## Exception Handling:

If any error occur while fetching the details from the url in both the pages then a error message will appear on the page for 2 seconds stating where the error occurred.

## Validations:

#### Package name validation:

The package name for the play store app will be validated with the package name pattern, the accessing and fetching of the data from the URL will only start if the package name pass this validation.

#### URL validation:

The URL for the url field in the keyword finder app will be validated with the url pattern, the accessing and fetching of the meta tags from the URL will only start if the url pass this validation.


## Testing:

#### App searcher:
The testing of the app searcher app can be done by entering the below command in the command prompt after firing the localhost server

`python manage.py test appsearcher`

#### Keyword finder:
The testing of the keyword finder app can be done by entering the below command in the command prompt after firing the localhost server

`python manage.py test keywordfinder`

Hope you find this app exciting. **_Thank You_**.

_Rahul Pinjarla,_

_S160142@rguktsklm.ac.in,_

_9550711381._