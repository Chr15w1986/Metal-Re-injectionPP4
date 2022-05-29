<h1 align=center>Testing</h1>


## **Automated tests**

### **Home app** 

The home app was tested using unittest.
Manual testing was conducted to test anything unittesting didn't cover to ensure no issues remain.

<p><img src="static/assets/img/readme_img/testing_img/homepageunittest.png"></p>

<br>

### **Tracks app** 

Spotify and add song functions on the tracks app were tested using unit tests.

  * Tracks Unittests Overall
<p><img src="static/assets/img/readme_img/testing_img/full-unittest.png"></p>


### **Coverage Test**

At the end of the development of this project (phase 1 - before submission day), used coverage tools to assert that automated tests covered all functions.

<p><img src="static/assets/img/readme_img/testing_img/coverage-report.png"></p>

#
## **Validation and accessibility**

### **Lighthouse report**
<details>
  <summary>Reports</summary>
  
  All pages of the app were tested using the lighthouse function built in to the Google Chrome browser on incognito mode.
  
  <img width="300" src="static/assets/img/readme_img/testing_img/home-page-loggedout.png">
  <img width="300" src="static/assets/img/readme_img/testing_img/home-page-loggedin.png">
  <img width="300" src="static/assets/img/readme_img/testing_img/signin-page.png">
  <img width="300" src="static/assets/img/readme_img/testing_img/tracklistpage.png">
  <img width="300" src="static/assets/img/readme_img/testing_img/ratetrack-page.png">
  <img width="300" src="static/assets/img/readme_img/testing_img/mytracks-page.png">
  <img width="300" src="static/assets/img/readme_img/testing_img/addtrack-page.png">
 
  
  The low score on `Rate a track` with 74 for accessibility, is due to the embedded spotify url.

</details>
  
### **WAVE Webaim Accessibility testing**
<details>
  <summary>Reports</summary>

  ### **Accessibility report**
  The WAVE tool was used to test all pages on the app.
  Some errors repeat over each page tested, these were due to the social links not having text as they are fontawesome links.
  As before a summary of results is shown as well as links to the individual results.  
    
    
  [link to home page WAVE result](https://wave.webaim.org/report#/https://metal-re-injection.herokuapp.com/)  
  [link to login page WAVE result](https://wave.webaim.org/report#/https://metal-re-injection.herokuapp.com/accounts/login/)  
  [link to signup page WAVE result](https://wave.webaim.org/report#/https://metal-re-injection.herokuapp.com/accounts/signup/)  
  [link to tracklist page WAVE result](https://wave.webaim.org/report#/https://metal-re-injection.herokuapp.com/tracks/song-list/)  
  [link to rate a track page WAVE result](https://wave.webaim.org/report#/https://metal-re-injection.herokuapp.com/tracks/single-song/48/)

  There were 2 parts of the site that were inaccesible and due to this I was unable to check them with the tool. 
  * These were:
    - Mytracks page, Internal server error. 
    - Rate a track page, User must be signed in, WAVE wouldn't allow me to sign in.
    
</details>

  ### **CSS Validation**
  <details>
  <summary>CSS Validator results</summary>
  Only the custom CSS file was tested (style.css)
  <img width="600" src="static/assets/img/readme_img/testing_img/CSSvalidator.png">
  
  </details>
  
 ### **HTML Validation**  
  <details>
  <summary>HTML Validator results</summary>
  All HTML was passed through the validator retreived from the source code within devtools on Chrome.

  [link to w3c validator result](https://validator.w3.org/nu/?showsource=yes&showoutline=yes&showimagereport=yes&doc=https%3A%2F%2Fmetal-re-injection.herokuapp.com%2F)
  
  </details>
  
 ### **Python Validation (PEP8)**
  <details>
  <summary>PEP8 Validator results</summary>

###  **Metal-Re-injection App**

<p float="left">
        <img src="static/assets/img/readme_img/testing_img/PEP8/MRIasgi.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/MRIsettings.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/MRIWsgi.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/MRI-Views.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/MRI-Urls.png" width="400" height="200"/>
</p>

All files for metal-re-injection passed through PEP8 without errors

###  **Home App**

<p float="left">
        <img src="static/assets/img/readme_img/testing_img/PEP8/HOMEviews.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/HOMEurls.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/HOMEtests.png" width="400" height="200"/>
</p>

All files for home app passed through PEP8 without errors

### **Tracks App**

<p float="left">
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSadmin.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSapps.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSforms.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSmodels.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSspotipytools.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSurls.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKSviews.png" width="400" height="200"/>
        <img src="static/assets/img/readme_img/testing_img/PEP8/TRACKStests.png" width="400" height="200"/>
</p>

All files for Tracks app passed through PEP8 except one, Tracks/tests.py.<br>
The errors related to line length, the tested urls in the file cannot be split onto the next line to conform with pylint and pep8,
I do not consider these errors to have any impact on the functionality of the file.

  </details>

#

## **Manual Testing**

### Manual Testing of User Input and Functions  
  I systematically tested all user inputs and functionality in the website to compare feedback/results against expected results.  
  Any unexpected output/outcomes were fixed.  
  [The results of this testing can be found here](https://docs.google.com/spreadsheets/d/1MXG4cFjO-vgku2RB4azp_uSs3hObE3Ms83dnKNmJe8w/edit?usp=sharing)

### Desktop
  
  Google Chrome: All aspects of the site work perfectly fine. Pages load quickly, all features are working and found no problems with CRUD, listening to the tracks, logging in or out, signing up, adding tracks etc.
  Mozilla Firefox: All aspects of the site work perfectly fine. Pages load quickly, all features are working and found no problems with CRUD, listening to the tracks, logging in or out, signing up, adding tracks etc.

  * Every button works and redirects to the next page quickly,<br>
  * Url's load correctly on the rate a track page.<br>
  * Sign up form sends an automated email from a gmail account to the user to verify the email address. This works as it should.
  

### Mobile

  Tested all aspects of the site via three devices, Apple Iphone 11, Samsung S20FE and Samsung S7 tablet. The site reacts well to different devices, responsiveness works well, including on apples browser Safari.


# **Unfixed bugs**

  Three errors remain in chrome dev tools on the live version of the site. These errors relate to cloudinary and sitewebmanifest.
  Although I have tried to research this issue, I have not found a cure, thus these errors remain. The functionality of the site is not affected.
