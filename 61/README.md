## Code Challenge 61 - Build a URL Shortener

* Take the challenge [on our platform](https://codechalleng.es/challenges/61)

This urlshortner application is built using flask. This application uses simple light weight sqlite database which comes by default with flask. 

1. clone / create the project

2. Install from Pipfile: $ pipen install 

3. To run the application: $ python app.py (This will star the webserve locally in your laptop). 

4. you can enter any long url by passing it as a parameter in JSON at the follwing endpoint: http://localhost:5000/shortendurl/
   E.G: curl -H "Content-Type: application/json" -X GET -d '{"url":"https://www.quora.com/"}' http://localhost:5000/shortendurl/

   This long url is queried from the db, in case row exists, it will return the short url else, it return no rows. 

5. In case of a POST request: 
   E.G: curl -H "Content-Type: application/json" -X POST -d '{"url":"https://www.quora.com/"}' http://localhost:5000/shortendurl/

   New row is created in the db and the short url is returned for the long url 


 
