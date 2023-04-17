from flask import Flask

app = Flask(__name__) # always do this set up!
app.secret_key = "dojoandninjas420" #ONLY DEVS ON PROJECT should know this key

DATABASE = "dojo_and_ninjas_schema"
