# coding=utf-8
from database.mysql import MySQLDatabase
from settings import database

if __name__ == "__main__":
    db = MySQLDatabase(database.get('name'),
                       database.get('username'),
                       database.get('password'),
                       database.get('host'))

    # print db.get_available_tables()
    # print
    print db.get_columns_for_table('people')
    print
    print db.get_columns_for_table('profiles')
    print
    print db.get_columns_for_table('orders')
    print

    # # select a tables worth of data
    # results = db.select('people')
    # for row in results:
    #     print row

    # selecting columns with named tuples
    # results = db.select('people', columns=['id', 'first_name'], named_tuples=True)
    # for row in results:
    #     print row.id, row.first_name

    # use CONCAT and SUM to get a persons full name and total spend
    # people = db.select('people',
    #                     columns=["concat(first_name, ' ', second_name) as full_name",
    #                              "SUM(amount) as total_spend"],
    #                     named_tuples=True,
    #                     where="people.id=1",
    #                     join="orders ON people.id=orders.person_id")
    # for person in people:
    #     print person.full_name, " spent ", person.total_spend

    # # inserting records
    # db.insert('orders', person_id=1, amount=20.00)
    # # select a tables worth of data to see the inserted row
    # results = db.select('orders')
    # for row in results:
    #     print row

    # # updating a record
    # person = db.select('people', named_tuples=True)[0]  # first person found
    # db.update('profiles',
    #           where="person_id=%s" % person.id,
    #           address="2a another street")
    # # select a tables worth of data to see the updated row
    # results = db.select('profiles')
    # for row in results:
    #     print row

    # # Delete a record
    # person = db.select('people', named_tuples=True)[0]
    # db.delete('orders',
    #           person_id="=%s" % person.id,
    #           id="=14")
    # # select a tables worth of data to see if the row was deleted
    # results = db.select('orders')
    # for row in results:
    #     print row

    # results = db.select('people',
    #                     columns=['concat(first_name, " spends ", AVG(orders.amount)) AS fn'],
    #                     named_tuples=True,
    #                     join="orders ON people.id=orders.person_id",
    #                     where="person_id=1"
    #                     )
    # for row in results:
    #     print row.fn

    # Create a new person in the people table and add in a profile row and two orders of random value.
    # db.insert('people',
    #           first_name='Peter',
    #           second_name='Bristow',
    #           DOB='1973/06/16')
    # results = db.select('people',
    #                     columns=['id'],
    #                     named_tuples=True,
    #                     where="first_name='Peter' AND second_name='Bristow'"
    #                     )
    # for row in results:
    #     print row.id
    #     person_id = row.id
    # person_id = row.id
    # db.insert('profiles', person_id="%s" % person_id, address='Fleet')
    # db.insert('orders', person_id="%s" % person_id, amount=23.00)

    # Use select to get a full name and the minimum amount they have spent.
    # results = db.select('people',
    #                     columns=['concat(first_name, " ", second_name) AS full_name'],
    #                     named_tuples=True,
    #                     where="id=1"
    #                     )
    # for row in results:
    #     print row.full_name
    print
