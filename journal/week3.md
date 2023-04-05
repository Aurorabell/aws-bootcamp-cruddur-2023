# Week 3 — Decentralized Authentication
I completed the in-class tasks related to Amazon Cognito and the Flask Application. These tasks required a deep understanding of how to secure user authentication and sensitive data. I learned from Ashish Rajan's video tutorial that there are several security features and best practices to help ensure the security of the application and its users, such as using security protocols like OAuth2, OpenID Connect, and SAML. I am thrilled that I was able to successfully implement these settings.

The first task was to provision an Amazon Cognito User Pool via ClickOps. It involved creating a user pool, setting up a client, and configuring the necessary settings. The process was quite straightforward, and I was able to set up the user pool within a short time.

The next task was to install and configure the Amplify client-side library for Amazon Cognito. The Amplify library made it easy to interact with Amazon Cognito from the client-side.

After configuring the client-side library, the next task was to implement API calls to Amazon Cognito for custom login, signup, recovery, and forgot password pages. The implementation involved writing code that would interact with the user pool to authenticate users, sign them up, and enable password recovery. 

![Errors for password recovery](assets/week%203%20error.PNG)

Ah, the next task was all about playing hide and seek with the website elements! I had to write some code that would magically display or hide certain elements depending on whether the user was logged in or logged out. But let me tell you, my code was feeling mischievous that day! I ran into some silly errors on the recovery and forgot password pages, and my logging out code seemed to be enjoying a game of "now you see me, now you don't!" After a few failed attempts, I decided it was time for a little break to clear my head. Because sometimes, the best way to solve ridiculous errors is to step away and let your brain have a little rest.

![Errors after logging out](assets/week%203%20error%20after%20logout.PNG)

Finally, I implemented server-side verification of the JSON Web Token (JWT token) to serve authenticated API endpoints in Flask Application. This task involved verifying the JWT token that was generated when a user logged in and using it to protect certain endpoints in the Flask application.


