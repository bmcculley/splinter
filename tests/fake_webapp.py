from flask import Flask
from flask import request

EXAMPLE_APP = "http://localhost:5000/"

EXAMPLE_HTML = """\
<html>
  <head>
    <title>Example Title</title>
    <style>
        .draggable {
            display: block;
            background-color: #0000ff;
            width: 100px;
            height: 30px;
        }

        .droppable {
            display: block;
            background-color: #ccc;
            width: 200px;
            height: 50px;
        }
    </style>
    <script type="text/javascript" src="/static/jquery.min.js"></script>
    <script type="text/javascript" src="/static/jquery-ui-1.8.16.custom.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            $(".draggable").draggable();
            $(".droppable").droppable({
                drop: function() {
                    $('.dragged').html('yes');
                }
            });
            $("body").dblclick(function(){
                $("body").css("background-color", "#ff0000");
            });
            $(".should-be-visible-after-double-click").hide();
            $(".db-button").dblclick(function(){
                $(".should-be-visible-after-double-click").show();
            });
           $(".add-async-element").click(function() {
                setTimeout(function() {
                    $('body').append('<h4 id="async-header" value="async-header-value" class="async-element">async elment</h4>');
                    $('body').append('<input type="text" name="async-input" class="async-input" />');
                }, 1200 );
                setTimeout(function() {
                    $('body').append('<h5 id="async-header2" class="async-element2">async elment2</h5>');
                    $('body').append('<input type="text" name="async-input2" class="async-input2" />');
                }, 2400 );
           });

           $('.right-clicable').bind('contextmenu', function(){
                $(this).html('right clicked');
           });

           $(".remove-async-element").click(function() {
                setTimeout(function() {
                    $('.async-element').remove();
                    $('.async-input').remove();
                }, 1200 );
                setTimeout(function() {
                    $('.async-element2').remove();
                    $('.async-input2').remove();
                }, 2400 );
           });

           $(".add-element-mouseover").mouseover(function () {
                $('body').append('<label for="what-is-your-name" class="over-label">What is your name?</label>');
                $('body').append('<input type="text" id="what-is-your-name" class="over-input" name="whatsname" />');
           });

           $(".add-element-mouseover").mouseout(function () {
                $('.over-label').remove();
                $('.over-input').remove();
           });
        });
    </script>
  </head>
  <body>
    <h1 id="firstheader">Example Header</h1>
    <h1 id="firstheader">Example Last Header</h1>
    <form action="name" method="GET">
        <label for="query">Query</label>
        <input type="text" name="query" value="default value" />
        <input type="text" name="query" value="default last value" />
        <label for="send">Send</label>
        <input type="submit" name="send" />
        <input type="radio" name="gender" value="M" id="gender-m" /> Male
        <input type="radio" name="gender" value="F" id="gender-f" /> Female
        <input type="checkbox" name="some-check" value="choice" />
        <input type="checkbox" name="checked-checkbox" value="choosed" checked="checked" />
        <select name="uf">
            <option value="mt">Mato Grosso</option>
            <option value="rj">Rio de Janeiro</option>
        </select>
    </form>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" name="upload" />
    </form>
    <a href="http://example.com/">Link for Example.com</a>
    <a href="http://example.com/last">Link for Example.com</a>
    <a href="http://example.com/">Link for last Example.com</a>
    <div id="visible">visible</div>
    <div id="invisible" style="display:none">invisible</div>
    <a href="http://localhost:5000/foo">FOO</a>
    <a href="http://localhost:5000/foo">A wordier (and last) link to FOO</a>
    <a class='add-async-element' href="#">add async element</a>
    <a class='remove-async-element' href="#">remove async element</a>
    <a class='add-element-mouseover' href="#">addelement (mouseover)</a>
    <iframe id="iframemodal" src="/iframe"></iframe>
    <div id="inside">
        <h2>inside</h2>
        <form>
            <input id="visible" name="upload" type="text" value="crazy diamond" />
        </form>
    </div>
    <a href="#" class="db-button">double click button</a>
    <div class="should-be-visible-after-double-click">should-be-visible-after-double-click</div>
    <div class="right-clicable">no right click</div>
    <div class='draggable'>draggable</div>
    <div class='droppable'>droppable</div>
    <div class='dragged'>no</div>
  </body>
</html>"""

EXAMPLE_IFRAME_HTML = """\
<html>
  <head>
    <title>Example Title</title>
  </head>
  <body>
    <h1 id="firstheader">IFrame Example Header</h1>
  </body>
</html>"""

EXAMPLE_ALERT_HTML = """\
<html>
  <head>
    <title>Alert Example Title</title>
    <script type="text/javascript" src="/static/jquery.min.js"></script>
    <script type="text/javascript">
      $(document).ready(function(){
        $('.alerta').click(function() { alert('This is an alert example.'); });

        $('.pergunta').click(function() { nome = prompt('What is your name?'); alert(nome); });
      })
    </script>
  </head>
  <body>
    <h1 class="alerta">Alert Example Title</h1>
    <h2 class="pergunta">Prompt Example Subtitle</h2>
  </body>
</html>
"""

EXAMPLE_TYPE_HTML = """\
<html>
    <head>
        <script type="text/javascript">
        window.onload = function(f) {
            var number = 0;
            var name_input = document.getElementById('type-input-id');
            name_input.onkeyup = function(e) {
                showSuggest();
            };
            function showSuggest() {
                var hidden_suggest = document.getElementById('suggest');
                hidden_suggest.innerHTML += 'Hi, I am here #' + number + '! ';
                number++;
            };
        };
        </script>
    </head>
    <body>
        <form method="GET" action="">
            <input name="type-input" value="" id="type-input-id"/>
        </form>

        <span id="suggest"></span>
    </body>
</html>
"""

app = Flask(__name__)


@app.route('/')
def index():
    return EXAMPLE_HTML


@app.route('/iframe')
def iframed():
    return EXAMPLE_IFRAME_HTML


@app.route('/alert')
def alertd():
    return EXAMPLE_ALERT_HTML


@app.route('/type')
def type():
    return EXAMPLE_TYPE_HTML


@app.route('/name', methods=['GET'])
def get_name():
    return "My name is: Master Splinter"

@app.route('/useragent', methods=['GET'])
def get_user_agent():
    return request.user_agent.string

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        buffer = []
        buffer.append("Content-type: %s" % f.content_type)
        buffer.append("File content: %s" % f.stream.read())

        return '|'.join(buffer)

@app.route('/foo')
def foo():
    return "BAR!"


def start_flask_app(host, port):
    """Runs the server."""
    app.run(host=host, port=port)
    app.config['DEBUG'] = False
    app.config['TESTING'] = False

if __name__ == '__main__':
    app.run()
