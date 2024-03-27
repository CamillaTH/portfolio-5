# ZAMASHOP B2C online store

![alt text](static/images/zamashop-logo.png)
 Zamashop is a b2c store that offers clothing and homewhere like beddings, necklases etc.

## Deployment

* site is live at : https://protfolio-5-a19d9a5d5d8d.herokuapp.com/
* To enter admin panel go to -> https://protfolio-5-a19d9a5d5d8d.herokuapp.com//admin



### clone repository locally (HTTPS)

* Navigate to the repository (https://github.com/CamillaTH/portfolio-5)
* Click on the button "code".
* Choose "HTTPS" and copy the URL.
* Choose a local directory where want to clone the repository.
* Open terminal at the location you want the repository and write "git clone https://github.com/CamillaTH/portfolio-4.git" and press enter.

![alt text](static/images/readme/readme-clone.png)

### Run Website locally

To run server locally from terminal write :
 * python3 manage.py runserver
 * open in browser (click yes)
 
#### Activate local database
To use the local databse in settings.py line : 104-115 uncomment below "# local Database" 
* DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

And comment out 
#production DB
* DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }
 
 and comment ut SECRET_KEY = os.environ.get('SECRET_KEY') in settings.py
## Agile

Agile development was used during development of this site project board can be found :
* https://github.com/users/CamillaTH/projects/6/views/1

![alt text](static/images/readme/readme-agile.png)


## Frameworks

* This application is using the python frameWork Django v3.2.21
* Db is a postgresSql hosted on elephantsql.com.
* Site is deployed at heroku.com.
* jQuery is used as JS framwork.
* Boostrap is used as HTML/css framwork.
* Stripe as payment provider



## Features 


### Exsiting Features
 
* User can create an account.
* Users can sign in and sign out.
* Users search products
* users can filter products
* Users can sort products
* users can add products to cart
* Users can add products with different sizes(if they have)
* Users can view cart
* Users can when in checkout make an order (payment sucess to stripe but currently bug to land on order confirmation page)
 
 __ADMIN PANEL__

![alt text](static/images/readme/django-admin.png)

 
 __HOMEPAGE__

Homepage where you can search for products and choose categories
![alt text](static/images/readme/luna_readme_homepage.png)

__PRODUCTFEED PAGE__

Products feed page where you land if you pick an category or search for products. Shows product cards and shows information about every product. On this page users can also sort products on different criteras

![alt text](static/images/readme/readme-productFeed.png)

__PRODUCTDETAIL PAGE__

On the product detailpage users can see more details about products and add products to cart, users should also be able to add reviews about products and make comments /rateings but its under construction only BE is done for that.

![alt text](static/images/readme/readme-productDetail.png)

__CART PAGE__

Cart where user can view their products and add more or remove(currently a bug wiht removeing products) if user choose same products of different sizes the products are aranged on their own with its sizes.

![alt text](static/images/readme/readme-cart.png)

__CHECKOUT PAGE__

checkout page where user can se a sum of thier prouducts and total price and see the delivery fee. Here the user can fill delivery info submit an order (currently not 100% finished) and pay with card using stripe

Product summary

![alt text](static/images/readme/readme-checkout.png)

Cart payment

![alt text](static/images/readme/readme-checkout2.png)

__MOBILE MENU__

For smaller screen the site have a sliding overlaying menu so everyting in the header can fit

![alt text](static/images/readme/readme-mobilemenu.png)

__SITE MESSAGES__

The Admins have the feature to dynamically change the site messages for the customer without deploying/change the code. That is possible using the custom model sitemessages from the admin panel. At the moment there are 2 places where the admin can change the site messages "header" and "cart" 

Admin configured site message for the header.
![alt text](static/images/readme/readme-header-message-admin.png)


Configured site message message shown on site header
![alt text](static/images/readme/readme-header-message-site.png)


Admin configured site message for the cart.
![alt text](static/images/readme/readme-cart-message-admin.png)

Configured site message shown on cart page
![alt text](static/images/readme/readme-cart--message-site.png)

__WISHLIST__

Logged in user have the opertunity to add and remove products to their wishlist

User clicks button and product is added to wishlist (if user clicks link below it redirects it to account page so user can view its wishlist)
![alt text](static/images/readme/readme-wishlist-addtowishlist.png)

If user is not logged in show text you need to be logged in to add to wishlist (user clicks link and redirects to create account page)
![alt text](static/images/readme/readme-wishlist-logintoaddtowishlist.png)

If product is already added to wishlist show message to user
![alt text](static/images/readme/readme-wishlist-productalready-added.png)

Account view where user can view its wishlist and remove products from the wishlist
![alt text](static/images/readme/readme-wishlist-accountwishlist.png)


### Marketing strategies
Zamashop facebook page
![alt text](static/images/readme/readme-zamashopFacebookpage.png)

#### Social Media Marketing:
Use platforms like Instagram, Facebook, Pinterest, and Twitter to showcase your clothing products.
Run targeted ads to reach specific demographics based on age, location, interests, and online behavior.
Collaborate with influencers and fashion bloggers for sponsored posts and reviews.

#### Content Marketing:
Start a fashion blog on your website, providing style tips, fashion trends, and outfit ideas.
Create engaging and shareable content, such as videos, infographics, and articles related to fashion.
  
#### Email Marketing: 
Build an email list by offering discounts or exclusive content in exchange for subscribers.
Send personalized and targeted emails with new arrivals, promotions, and special offers. Send emails using mailchimp. Mailchimp is integreated to the django app when a user inserts its email and click the button the email will be added to the mailchimp audience list.

Campaign template

 ![alt text](static/images/readme/mailchimpimage.png)

user subscribes to newsletter

 ![alt text](static/images/readme/readme-subscribe-to-newsletter.png)

Email address is immediately added to zamashops audience list

 ![alt text](static/images/readme/readme-audience-mailchimp.png)


Employee chooses an campaign and send out emails to the emails in the audience list

 ![alt text](static/images/readme/readme-mailchimp-campaigndashboard.png)


Confirmation that the campaign have been emailed out.

![alt text](static/images/readme/readme-mailchimp-campaign-sent-confirmation.png)


### SEO
Robots.txt is added and allowed to crawl trough whole site

## Testing
 
 * To run python test in terminal write: "python manage.py test"
 
### Python test results
![alt text](static/images/readme/readme-pythonTest.png)

### Lighthouse score 
![alt text](static/images/readme/readme-lighthouse.png)

lighthouse score can definitely be imporoved. 

### Responsvie testing 
    Of some reason it does not work with Heroku apps and responsive checker (i tested different ones just got a blank screen...)


### Validator Testing

 HTML:
   No errors were found when code was injected into the official (https://validator.w3.org/)
* CSS:
   No errors were found when code was injected into the official https://jigsaw.w3.org/css-validator
* JS validation: Javascript validation using https://jshint.com (alot of missing semicolons where detected and fixed)
* JS format: Fixed formating of Js code using https://beautifier.io


### Known Bugs

Bugs that are confimred and not fixed:

* custom 404 page does not render it instead throws 500 page and that page is custom.


### Overal thoughts 
Im not super happy with the design but i had to focus on the functions first handed to have time to finish the project on time.
But the overall design and contrasts of the colors can be imporved ALOT!
 

## Credits 

Inspiration taken from code insitutes rock papper scissors game made by code insitute.

* For blinking effect this guide was used
https://www.w3docs.com/snippets/css/how-to-create-a-blinking-effect-with-css3-animations.html
* For to convert an png image to favicon (.ico format) 
https://cloudconvert.com/ico-converter tool was used.
* to create the logo i used adobe https://www.adobe.com/express/create/logo
* To make images transparent https://www.remove.bg/ tool was used
* for icons i use fontawsome https://fontawesome.com/icons

