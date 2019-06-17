from web import db, Account

data = Account.query.all()

print(data)