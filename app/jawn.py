from app import db, parser, models
from flask import jsonify
from flask.ext.restful import Resource, fields


class Registration(Resource):
    def get(self):
        return 'bleh', 200

    def post(self):
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
        args = parser.parse_args()
        user = models.User(args['username'],
                           args['name'],
                           args['password'],
                           args['email'])
        db.session.add(user)
        db.session.commit()
        user_in_db = models.User.query.filter_by(
            username=args['username']).all()
        return jsonify(user_in_db=user_in_db), 201
