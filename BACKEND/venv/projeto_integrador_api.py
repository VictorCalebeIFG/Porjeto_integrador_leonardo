from supabase import create_client, Client
from flask import Flask, jsonify

app = Flask(__name__)

url: str = ("https://tsbqxxhiznjlmogugaix.supabase.co")
key: str = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzYnF4eGhpem5qbG1vZ3VnYWl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI1MDU4MjIsImV4cCI6MjAyODA4MTgyMn0.6X5st_P8sMYnUSzKZNUHnxpSyPGq2Bba7mbsCIlZ4rE")
supabase: Client = create_client(url, key)


def get_user_id_by_email(email):
    query_result = supabase.table('User').select('id').eq('email', email).execute()
    data = query_result.data
    return data[0]['id']

@app.route('/user', methods=['GET'])
def get_users():
    query_result = supabase.table('User').select('*').execute()
    data = query_result.data
    return jsonify({'user': data})

@app.route('/user/<string:user_email>', methods=['GET'])
def get_users_by_email(user_email):
    query_result = supabase.table('User').select('*').eq('email', user_email).execute()
    data = query_result.data
    return jsonify({'user': data})

@app.route('/user/<string:name>/<string:email>/<string:password>', methods=['POST'])
def create_user(name, email, password):
    try:
        supabase.table('User').insert({'name': name, 'email': email, 'password': password}).execute()
        return jsonify({'message': 'User created'})
    except:
        return jsonify({'message': 'User already exists'})

@app.route('/checkpassword/<string:email>/<string:password>', methods=['POST'])
def check_user_password(email, password):
    query_result = supabase.table('User').select('password').eq('email', email).execute()
    data = query_result.data
    if data[0]['password'] == password:
        return jsonify({'message': 'Password matches'})
    else:
        return jsonify({'message': 'Password does not match'})

@app.route('/createpost/<string:email>/<string:title>/<string:description>/<string:price>/<string:deadline>', methods=['POST'])
def create_post(email, title, description, price, deadline):
    user_id = get_user_id_by_email(email)
    supabase.table('Post').insert({'user_id': user_id, 'title': title, 'description': description, 'price': price, 'deadline': deadline}).execute()
    return jsonify({'message': 'Post created'})

@app.route('/post', methods=['GET'])
def get_posts():
    query_result = supabase.table('Post').select('*').execute()
    data = query_result.data
    return jsonify({'post': data})

if __name__ == '__main__':
    app.run(debug=True)

