<h1 align=center>Portfolio Project 4</h1>

<p align=center>Do you love music? Oldies? Pop music?..<br/>
Well, here you have the opportunity to hear and rate some of your favourite tracks of all time covered,<br>
(in some peoples opinion, ruined) <br>
by the worlds most unpopular genre of music.. METAL!</p>
<br>
<br>
<h1 align=center>Welcome to Metal-Re-Injection</h1>

## FINAL DESIGN
<br>
<img src="static/assets/img/readme_img/Amiresponsive.png">

#
[Here is a link to the final project](https://metal-re-injection.herokuapp.com/)
#

## User Experience

### User Stories

1. As a user, I would like to be able to …

    1.1 Register on the website using my username, email address and password;

    1.2 View all tracks added on the site;

    1.3 View details about all added tracks.

    1.4 View tracklist on the navbar.  

2. As a logged in user, I would like to be able to …

    2.1 Create a rating of my favourite tracks, including :
    + Track title,
    + Cover Artist,
    + Original artist,
    + Overall Rating,

    2.2 Create a new track, if my track is not added to the Database;

    2.3 Check my track review after added;

    2.4 Edit or delete my track ratings.
#
### 1. Strategy

  + **Project Goal**

   Create a platform that allows people (users) to rate music covers and share their thoughts in the form of 5 star ratings.

### 2. Scope

 * A simple, straightforward, intuitive UX experience;
 * An explicit content;
 * An easy navigation for the user through all of the features;
 * A site that is visually appealing on most devices.

## Functional Scope 

**Metal-Re-Injection Flowchart**

<details>
<summary>Flowchart</summary>
<br>

![MRI Flowchart](static/assets/img/readme_img/Metal-Re-Injection.png)
</details>


**Agile Methodology**

All functionality and development of this project were managed using **Trello** (https://trello.com/b/LcAoo35I/metal-re-injection-pp4)

* Credentials to this tool will be provided during submission.

<!-- ADD SPRINTS HERE -->
### 3. Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have a leisurely experience.
* Navbar is fixed on top to facilitate users to navigate through pages easily.
* A Small dropdown menu navigation is the same on all pages at small screen sizes to ensure easy navigation.
* Add, Edit/Update are straightforward forms to allow users to use the features without issues.


### 4. Skeleton

* Wireframes created with Balsamiq. <br>
* The project was developed from initial wireframes, and some modifications were made during the development process in response to user feedback.


<details>
<summary>Click to see wireframes:</summary>
<br>

[HomePage](wireframes/homepage.png) <br>
[Add track Page](wireframes/addtrackpage.png) <br>
[Rating Page](wireframes/ratetrack.png) <br>
[Register Page](wireframes/registration-page.png) <br>
[Login Page](wireframes/login-page.png) <br>
[HomePage mobile](wireframes/home-mobile.png) <br>
[Add track Page mobile](wireframes/addtrack-mobile.png) <br>
[Rating Page mobile](wireframes/ratetrack-mobile.png) <br>
[Register Page mobile](wireframes/registration-mobile.png) <br>
[Login Page mobile](wireframes/loginpage-mobile.png) <br>

</details>

#

### 5. Surface

* Colours

- The colour scheme was chosen based on the background image I wanted to use sitewide.
I used [Coolors](https://coolors.co/) to generate a colour palette based on the image.
<details>
<summary>Click to see Colours:</summary>
<br>

![Main colours](static/assets/img/readme_img/colorpalette.png)<br>
![Secondary colours](static/assets/img/readme_img/Colorpalette2.png)

</details>


* Font Selection
 
Two fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the entire site.

The chosen fonts were Varela Round, Segoe UI with Roboto and Lato as back up fonts for lists, forms, buttons and paragraphs.
#
## Existing Features

### **Navbar**

+ Fixed Navbar allow the user easy access to all pages.

1. Tracklist, Login and Signup buttons on the navbar are the only buttons present if the user is `not` logged in.

<img width="700" src="static/assets/img/readme_img/features/loggedoutnavbar.png">

2. Tracklist, Add a Track, My Tracks and Logout buttons are only present if the user has successfully logged in.

<img width="700" src="static/assets/img/readme_img/features/loggedinusernavbar.png">

3. Track list is available to view to all users (logged in or not), however, the tracks cannot be played until<br>
the user logs in, or signs up.

4. Collapsed navbar on smaller devices to wrap in all options and assure better navbar design.

  <img width="400" src="static/assets/img/readme_img/features/collapsed-navbar.png">

### **Track list page**

1. On this page, users can view all user added tracks ordered by latest date/time added, including pagination.

  <img width="700" src="static/assets/img/readme_img/features/tracklistpage.png">

* Each card contains Track title, Cover Artist, Original Artist, Author, Publication date and if the author owns the track, 
two buttons, `Edit` `Delete`.

* The entire card is a link to the Rate a track page.

### **Rate a Track page** 

* Here the User has the ability to listen to the track and give it a rating out of 5 stars.

<img width="700" src="static/assets/img/readme_img/features/rateatrackpage.png">

  1.1 If the user is the author, the same `Edit` `Delete` buttons will be present.

<img width="400" src="static/assets/img/readme_img/features/authoreditdelete.png">

   i. Edit Track (highlighted in green)
  
   ii. Delete Track (highlighted in red)

### **Track rating system**

1. Underneath the single song on the `Rate a Track` page, the user has the option to rate the current track out of 5 stars.

    i. The user can rate any song while logged in.
    ii. The user can change their rating while logged in.
    iii. The number of total ratings and average ratings are shown and match the stars accordingly.


  <img width="700"  src="static/assets/img/readme_img/features/ratings.png">

### **Update/Edit Track Page**

1. On this page, a logged user can change the information made by them. All fields are already populated, allowing the user to see which information they would like to change.
2. The `Go back` button will redirect the user to the Rate a Track page without any changes.

<img width="700" src="static/assets/img/readme_img/features/editatrackpage.png">

### **Delete a Track Page**

1. If the user clicks on delete a track, they will be redirected to Delete a Track page to confirm the deletion or cancel it.
2. The `Go back` button will redirect the user to the Rate a Track page without any changes.

<img width="700" src="static/assets/img/readme_img/features/deleteatrackpage.png">

### **Custom 404 Page not found**

* I have created a custom 404 error page to catch if the user inputs the wrong page number, or if a page or feature does not exist.
* I have included a button to redirect back to home.

<!-- IMAGE HERE -->

### **Custom 500 Internal server error**

* I have created a custom 500 error page to redirect to if there are any issues with the database including a button to redirect back to home.

<!-- IMAGE HERE -->
#
## Future Features

I would like to ...

1. Add a infinite smooth scroll carousel to list all tracks on the same page.
2. Add a search bar to find artists and or tracks.
3. Create an option for the user to add a song from another source, i.e. Youtube, Deezer.
4. Include a user profile page allowing users to edit, or delete their profile.
5. Include a comments section to be used with the rating system.

#
## Languages Used

<img width="200" height="150" src="static/assets/img/readme_img/languages/python3.png"><img width="200" height="150" src="static/assets/img/readme_img/languages/html5.png"><img width="200" height="150" src="static/assets/img/readme_img/languages/css3.png"><img width="200" height="150" src="static/assets/img/readme_img/languages/js.png">

## Frameworks, Libraries & Programs Used

+ Balsamiq: Balsamiq was used to create the wireframes during the design process.
+ Favicon Generator: Used to create favicon used on the website.
+ Grammarly: Used to correct any spell mistakes on readme and app text.
+ Git: Gitpod IDE was used for version control by utilizing the Gitpod terminal to commit and Push to GitHub.
+ GitHub: GitHub respository is used to store the project's code after being pushed from Gitpod.
+ Google Fonts: Google fonts are used to add fonts for aesthetic and UX purposes.
+ Django: Framework used to add structure to the platform.
+ AmIResponsive: Used to generate mockup image.


install django, gunicorn, psycopg2, cloudinary, bootstrap, summernote, allauth, star-ratings, whitenoise