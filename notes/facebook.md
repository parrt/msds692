# Pulling data from Facebook

[Code to pull whitehouse feed](https://github.com/parrt/msan692/blob/master/notes/code/facebook/feed.py). Requires app ID and secret from your app on your dashboard.

1. [Register/configure an App overview](https://developers.facebook.com/docs/apps/register)
2. [Create developer account](https://developers.facebook.com/async/onboarding/dialog/)
3. [Create new Facebook App](https://developers.facebook.com/apps/async/create/platform-setup/dialog/)<br>
  <img src=figures/fb-add-app.png width=250><br>
  Click "Basic Setup"<br>
  <img src=figures/fb-create-id.png width=350><br>
  It will ask you to verify your account using phone or credit card. Note that I had to drop my mobile phone from the account and re-added in order for Facebook to allow me to create the application ID.
4. You need to make sure that you have specified where Facebook should go during OAuth:<br>
<img src=figures/fb-oauth-settings.png width=400>

**Save the application ID you get, and in a safe place.** You will need it to communicate with Facebook's API.

Once you're set up, you should see a dashboard like this:
 
<img src=figures/fb-dashboard.png width=400>

Notice that under products it says "Facebook login" but you can add lots of other products, depending on what you'd like to do. In our case we simply want to try logging in as a particular person.

Make sure you enable the app:

<img src=figures/fb-enable-desktop-app.png width=600>

and set up security on same page:

<img src=figures/fb-security.png width=400>

[FaceBook Login Flow](https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow)

```
https://www.facebook.com/dialog/oauth?
  client_id={app-id}
  &redirect_uri={redirect-uri}
```

browser will attempt to log the user in and then FB response after login does a redirect back to our site:

```
http://localhost:8000/?code=XXX
```

with a code that you need to use for communication with the API.

NOW, you need to exchange that code for an access token using your app secret.

```
https://graph.facebook.com/v2.3/oauth/access_token?
    client_id={app-id}
   &redirect_uri={redirect-uri}
   &client_secret={app-secret}
   &code={code-parameter}
```

Note that the `app-id` and `app-secret` should be kept private. Do not embed them in any HTML, JavaScript, or anything that could become public (such as in a webpage you post). I specify them on the commandline when I start up my application so as not to embed them anywhere.

The `code-parameter` is what you got back from login above.

[securing your FB requests](https://developers.facebook.com/docs/graph-api/securing-requests/)