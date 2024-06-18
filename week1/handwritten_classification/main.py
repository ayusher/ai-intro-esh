from flask import Flask
from flask_restful import Resource, Api
import pickle
# add imports as needed


app = Flask(__name__)
api = Api(app)


# load the model from the pickle file


class HandwrittenDigitSVC(Resource):

    def get(self):
        return {
            'name': 'Handwritten Digit SVC',
            # 'test_accuracy': ...,
            # any other information you want to include
        }

    def post(self):
        # get the image from the request.files
        # preprocess the image as needed
        # return the prediction from your trained SVC model

        return {
            'prediction': 0
        }

 
api.add_resource(HandwrittenDigitSVC, '/svc')

if __name__ == '__main__':
    app.run(debug=True)
