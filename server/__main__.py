"""
Serve app
"""


from server import create_app

if __name__ == "__main__":
    print('Serving app')
    app = create_app()
    app.run(debug=True, port=8080)
