# simple-api-shutterstock
Youtube Simple API series example for Shutter Stock
  
# Steps
 - Create an account with shutterstock.
 - Create (register) a new app with shutter shutterstock.
 - Copy your new app credentials (key, secret, and token)
 - Clone this repo  
`git clone git@github.com:tekksparrow-programs/simple-api-shutterstock.git
 - CD into the project dsirectory  
`cd simple-api-shutterstock`
 - Paste your app credentials into the `.env` file
 - Setup Environment 
```shell 
$ python3 -m venv venv
$ source venv/bin/activatess
$ pip3 install -r requirements.txt
```
 - If fetching your token, update the `redirect_url` variable to match what is registered with your application
 - If using provided token comment out OPTION 1 code
 - Fire up your run file  
`python3 simple-api-shutter.py`

# Video Tutorial
https://www.youtube.com/watch?v=qurxvE7lhX0

# Links
 - [developer landing page](https://www.shutterstock.com/api/pricing)
 - [api documentation](https://api-reference.shutterstock.com#overview)
 - [authentication docs](https://api-reference.shutterstock.com/#authentication)
 - [app registration](https://www.shutterstock.com/account/developers/apps)

