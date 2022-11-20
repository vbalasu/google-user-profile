from chalice import Chalice, Response

app = Chalice(app_name='google-user-profile')


@app.route('/')
def index():
    with open('chalicelib/index.html') as f:
        return Response(body=f.read(), status_code=200, headers={'Content-Type': 'text/html'})

@app.route('/validate/{token}')
def validate(token):
    from google.oauth2 import id_token
    from google.auth.transport import requests
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), '697856052963-e8smtnj173ddlfs56dh29nv0lntne5ul.apps.googleusercontent.com')
        userid = idinfo['sub']
    except ValueError:
        return Response(body='Invalid token', status_code=403)
    try:
        record_login(idinfo)
    except:
        return Response(body='Login error', status_code=403)
    return idinfo

def record_login(idinfo):
    import requests
    users_url = "https://home.cloudmatica.com/api/users"
    response = requests.post(users_url, json={'data': idinfo})
    return response


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
