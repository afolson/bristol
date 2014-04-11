from app import app, db, parser
from flask.ext import restful


class Registration(restful.Resource):
    def get(self):
        return 'bleh', 200

    def post(self):
        args = parser.parse_args()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        user = User(args['username'],
                    args['name'],
                    args['password'],
                    args['email'])
        db.session.add(user)
        db.session.commit()
        return User.query.filter_by(username=args['username']).first(), 201

#api.add_resource(Registration, '/api/registration/')