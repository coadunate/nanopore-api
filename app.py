from flask import Flask
from flask_restful import Api
from resources import ReadTableResource
from resources import ReadResource
from resources import EventResource
#from resources import FrontEndResource

app = Flask(__name__)
api = Api(app)


api.add_resource(ReadTableResource, '/tabledata', endpoint='tabledata')
api.add_resource(ReadResource, '/readdata/<string:qname>', endpoint='readdata')
api.add_resource(EventResource, '/eventdata/<string:qname>', endpoint='eventdata')


@app.route('/')
def index():
		render_template('./app/index.html')

if __name__ == '__main__':
    app.run(host='192.168.64.11',port=80,debug=True)
