# Pulling data from LinkedIn

You must create a known entity (application) that will communicate with the API. Start by reading [OAuth 2.0 for linkedin](https://developer.linkedin.com/docs/oauth2)

[Create an application](https://www.linkedin.com/secure/developer?newapp=)

I just used my name for the application name:

<img src="figures/linkedin-app-settings.png" width=280>


```bash
$ pip install python-linkedin
```

Here are some important notes from the LinkedIn documentation:
 
> To request an authorization code, you must direct the user's browser to LinkedIn's OAuth 2.0 authorization endpoint.

> When the user completes the authorization process, the browser is redirected to the URL provided in the redirect_uri query parameter.
> 
> Attached to the redirect_uri will be two important URL arguments that you need to read from the request: code, state (*we will ignore the state*)
> 
> The code is a value that you will exchange with LinkedIn for an actual OAuth 2.0 access token in the next step of the authentcation process.
> 
> Before you accept the authorization code, your application should ensure that the value returned in the state parameter matches the state value from your original authorization code request. This ensures that you are dealing with the real original user and not a malicious script that has somehow slipped into the middle of your authentication flow.  If the state values do not match, you are likely the victim of a CSRF attack and you should throw an HTTP 401 error code in response.