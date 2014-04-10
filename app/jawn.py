from app import app
from flask.ext import restful


class Registration(restful.Resource):
    def get(self):
        return 'bleh', 200

    def post(self):
        args = parser.parse_args()
        user = User(args['username'],
                    args['name'],
                    args['password'],
                    args['email'])
        db.session.add(user)
        db.session.commit()
        return User.query.filter_by(username=args['username']).first(), 201

#api.add_resource(Registration, '/api/registration/')