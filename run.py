from flaskblog import create_app

# can pass in config classes here
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
