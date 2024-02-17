from admin import Admin

uri = Admin('uri', 'gakuru', 'gakuruuri', 'urigakuru@live.co.uk', 'ikinu')
uri.describe_user()
uri.greet_user()

uri_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
uri.privileges.privileges = uri_privileges

print(f"\nThe admin {uri.username} has these privileges: ")
uri.privileges.show_privileges()