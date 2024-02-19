from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'CTF Player')
    return render_template_string(f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Blog</title>
        <style>
            body {{
                background-color: #000;
                color: #fff;
                font-family: 'Courier New', monospace;
                margin: 0;
                padding: 0;
                text-align: center;
            }}
            header {{
                background-color: #004d40;  /* Deep teal green */
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }}
            nav ul {{
                list-style-type: none;
                padding: 0;
                margin: 0;
            }}
            nav ul li {{
                display: inline;
                margin-right: 20px;
            }}
            nav ul li a {{
                color: white;
                text-decoration: none;
                font-weight: bold;
                font-size: 18px;
                transition: color 0.3s;
            }}
            nav ul li a:hover {{
                color: #00796b;  
            }}
            section {{
                margin-top: 50px;
            }}
            h1 {{
                font-size: 36px;
                margin-bottom: 20px;
                color: #004d40; 
            }}
            p {{
                font-size: 18px;
                color: #fff;
            }}
            h2 {{
                font-size: 24px;
                margin-bottom: 10px;
                color: #004d40; 
            }}
            h3 {{
                font-size: 20px;
                margin-bottom: 10px;
                color: #004d40; 
            }}
            a {{
                font-size: 14px;
                color: #fff;
                text-decoration: none;
                transition: color 0.3s;
            }}
            a:hover {{
                color: #00796b; 
            }}
            footer {{
                margin-top: 50px;
                background-color: #004d40;  
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }}
            .post-card {{
                width: 300px;
                margin: 10px;
                padding: 20px;
                background-color: #00796b;  
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s;
            }}
            .post-card:hover {{
                transform: scale(1.05);
            }}
        </style>
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="#hint1">Hint: </a></li>
                    <li><a href="#hint2">Jinja Templating</a></li>
                    <li><a href="#hint3">Engine</a></li>
                </ul>
            </nav>
        </header>

        <section id="home">
            <h1>Welcome to My Blog!</h1>
            <p>Hello {name}! This is a place where I share my thoughts and experiences.</p>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>I am a passionate writer and love to explore various topics. I enjoy long walks on the beach, but I can't see in the dark.</p>
        </section>

        <section id="blog">
            <h2>Latest Blog Posts</h2>
            <div style="display: flex; flex-wrap: wrap; justify-content: center;">
                <div class="post-card">
                    <h3>Slick Rick</h3>
                    <p>News Just In: No more gritz</p>
                    <a href="#" style="color: #fff;">Read More</a>
                </div>
                <div class="post-card">
                    <h3>Beaking News Again....</h3>
                    <p>When in doubt Meme it out: <iframe src="https://giphy.com/embed/hvT5KWdFkUOklHCxXk" width="100" height="100" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></p>
                </div>
            </div>
        </section>
    </body>
    </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
