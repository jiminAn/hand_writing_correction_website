# [Full-Stack] About Express.js Server

#### **Setup Express Server**

1. **Setup a new or existing npm package**

   ```
   npm init
   ```

   - But if you don't want to answer some questions, you can run this command instead ```npm init -y```.
   - After answering or skipping the questions a ```package.json``` file is going to be created.
   - **What is ```package.json```?**
     - ```package.json``` file holds some basic information about your application as well as metadata(Critically important for website and database management) about our application.
     - It will also manage all the dependencies of our application.
     - Any additional package we install using NPM(Node Package Manager) will be managed here as well.

<br/>

2.  **Install Express.js**

   ```
   npm install express
   ```

   - We can see a folder appear called ```node_modules```. (But do not edit this folder)
   - **What is ```node_modules```?**
     - ```node_modules``` contains all the dependencies for Express.js and the dependencies of those dependencies(Node.js relies on to work the way it does).