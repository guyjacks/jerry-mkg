from flask import Flask, render_template, jsonify, redirect, flash, request
from flask.ext.mail import Mail, Message
import pytumblr
from forms import ContactForm


app = Flask(__name__)
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#mail = Mail(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    recipients = ['guy.jacks@gmail.com']
    posts = tumblr_get_posts()
    """
    form = ContactForm()
    if form.validate_on_submit():
        flash("Thank you.  I'll get back to you soon")
        subject = form.subject.data
        message = form.message.data + '\n\n' + 'from: ' + form.name.data + '\n\n' + 'phone: ' + form.phone.data
        sender = (form.name.data, form.email)
        msg = Message(subject=subject,
                      recipients=recipients,
                      body=message,
                      sender=sender)
        mail.send(msg)
        """
    #return render_template('index.html', posts=posts, form=form)
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
