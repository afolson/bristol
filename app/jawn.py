from app import db, parser, models
from flask.ext import restful


class Registration(restful.Resource):
    def get(self):
        return 'bleh', 200

    def post(self):
        args = parser.parse_args()
        parser.add_argument('rate',
                            type=int,
                            help='Rate to charge for this resource')
        user = models.User(args['username'],
                           args['name'],
                           args['password'],
                           args['email'])
        db.session.add(user)
        db.session.commit()
        return models.User.query.filter_by(
            username=args['username']).first(), 201
