from flask import Flask, render_template, jsonify
import pytumblr


app = Flask(__name__)


@app.route("/")
def index():
    posts = tumblr_get_posts()
    return render_template('index.html', posts=posts)


@app.route("/posts")
def posts():
    client = tumblr_authenticate()
    posts = tumblr_get_posts(client)
    return jsonify(posts)
    #return render_template('posts.html', posts=posts)


def tumblr_authenticate():
    return pytumblr.TumblrRestClient(
        'bTmZgAuglMqiz4QatFaxzR9ukMsyDFm4jqcgeYzdVNELH4AXrM',
        'n2CT8ykDoc5XbseIRwSVR63NG8OrTN6qf3gtw2ThB5vWNmuazf',
        'OWa3h5PbEqtVRj2EMikfVTAJQUkq6Eucuucgfxdw4lPMObTfau',
        'fWyZotV1iT1Co0RqV5KZMEXGVoQYqy9S8uOzNOpk5euFs339DJ'
    )


def tumblr_get_posts(client=False):
    if not client:
        client = tumblr_authenticate()
    return client.posts('prismhousecreative')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
