from flaskblog import app

#To run the application in debug mode
if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
