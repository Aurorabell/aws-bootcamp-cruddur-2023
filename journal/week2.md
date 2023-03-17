# Week 2 — Distributed Tracing
During the week, I followed the LiveStream class the topic tackled how to improve the observability and error logging for the backend Flask application and React frontend app. We had to instrument the backend with Open Telemetry and Honeycomb.io, AWS X-Ray, CloudWatch and Rollbar for error logging. 

For the backend Flask application (Honeycomb.io as the provider), I had to install the required dependencies and update the code to include the Open Telemetry API. Once the instrumentation was complete, I ran queries to explore traces within Honeycomb.io dashboard. Next,I had to configure and provision the X-Ray daemon within docker-compose and send data back to the X-Ray API. I was then able to observe X-Ray traces within the AWS Console. On the next task, I installed WatchTower and wrote a custom logger to send application log data to a CloudWatch Log group. Finally, I configured Rollbar and triggered an error to observe it in the Rollbar dashboard. This allowed me to quickly identify and fix errors in the application.

Throughout the week, I encountered various errors and issues. Both backend and frontend ports were “not served” despite them working perfectly fine from the previous task that I had completed.  I had to troubleshoot issues with missing dependencies and syntax errors in my code. I also had to fix issues with the frontend Docker container failing to start due to missing packages. I lost count on how many times I hit that Docker Compose up / down command. Despite these setbacks, I persisted in my troubleshooting efforts and eventually was able to resolve the issues and get my Docker setup running smoothly.

These are some of the errors that I faced:-

NameError: name 'app' is not defined
This error occurred in the Flask backend application, specifically in the app.py file, at line 55 where the "@app.before_first_request" decorator is being used. The error message indicated that the "app" variable was not defined before it. To fix this error, one needs to ensure that the Flask "app" instance is properly imported and defined before using it in the file. This can be done by checking the import statements and the code syntax.

sh: 1: react-scripts: not found
This error occurred in the React frontend application, specifically in the Docker container, where the command "react-scripts" was not found or installed. This error can be caused by missing or incomplete dependencies for the React application, incorrect working directory of the terminal session, or the "react-scripts" package is not included in the "dependencies" or "devDependencies" section of the project's "package.json" file.
To fix this error, one needs to ensure that all the required dependencies for the React application are installed properly, set the current working directory of the terminal session to the root directory of the React application where the "node_modules" directory is located, and add the "react-scripts" package to the "dependencies" or "devDependencies" section of the project's "package.json" file.

Containers: Logs: aws-bootcamp-cruddur-2023-backend-flask-1 task ignored
This error occurred in the VS Code editor while trying to view the logs of the backend Flask container. The error message indicates that the task neither specifies a command nor a dependsOn property, and it will be ignored.
To fix this error, one needs to ensure that the task definition includes a valid command or dependsOn property that specifies the container to view the logs. This can be done by checking the task definition in the VS Code editor and ensuring that it includes the required properties.

Overall, this week was a valuable learning experience, as I gained a deeper understanding of observability and logging best practices. I also developed my troubleshooting and problem-solving skills, which will be valuable in my future work.
