from app import db, parser, models
from flask.ext import restful


class Registration(restful.Resource):
    def get(self):
        return 'bleh', 200

    def post(self):
        args = parser.parse_args()
        parser.add_argument('username',
                            type=str,
                            help='User Name.')
        parser.add_argument('name',
                            type=str,
                            help='Full Name.')
        parser.add_argument('password',
                            type=str,
                            help='Password.')
        parser.add_argument('email',
                            type=str,
                            help='Email.')
        user = models.User(args['username'],
                           args['name'],
                           args['password'],
                           args['email'])
        db.session.add(user)
        db.session.commit()
        return models.User.query.filter_by(
            username=args['username']).first(), 201
