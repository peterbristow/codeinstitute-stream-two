import collections
import re

import MySQLdb as _mySql

# only needs to compile one time so we put here!
float_match = re.compile(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$').match


def is_number(string):
    return bool(float_match(string))


class MySQLDatabase:
    def __init__(self, database_name, username, password, host='localhost'):
        try:
            self.db = _mySql.connect(db=database_name,
                                     host=host,
                                     user=username,
                                     passwd=password)

            self.database_name = database_name

            print "Connected to MySQL!"
        except _mySql.Error, e:
            print e

    def __del__(self):
        if hasattr(self, 'db'):  # close our connection to free it up in the pool
            self.db.close()
            print "MySQL Connection closed"

    def get_available_tables(self):
        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES;")

        self.tables = cursor.fetchall()

        cursor.close()

        return self.tables

    def get_columns_for_table(self, table_name):
        cursor = self.db.cursor()
        cursor.execute("SHOW COLUMNS FROM `%s`" % table_name)

        columns = cursor.fetchall()

        cursor.close()

        return columns

    def convert_to_named_tuples(self, cursor):
        results = None

        names = " ".join(d[0] for d in cursor.description)
        klass = collections.namedtuple('Results', names)

        try:
            results = map(klass._make, cursor.fetchall())
        except _mySql.ProgrammingError:
            pass

        return results

    def select(self, table, columns=None, named_tuples=False, **kwargs):
        """
        select(table_name, [list of column names])
        """
        sql_str = "SELECT "

        # add columns or just the wildcard
        if not columns:
            sql_str += " * "
        else:
            for column in columns:
                sql_str += "%s, " % column

            sql_str = sql_str[:-2]  # remove the last comma!

        # add the table to select from
        sql_str += " FROM `%s`.`%s`" % (self.database_name, table)

        # there a JOIN clause attached
        if kwargs.has_key('join'):
            sql_str += " JOIN %s" % kwargs.get('join')

        # there a WHERE clause attached
        if kwargs.has_key('where'):
            sql_str += " WHERE %s" % kwargs.get('where')

        # there a ORDER BY clause attached
        if kwargs.has_key('order_by'):
            sql_str += " ORDER BY %s" % kwargs.get('order_by')

        # there a GROUP BY clause attached
        if kwargs.has_key('group_by'):
            sql_str += " GROUP BY %s" % kwargs.get('group_by')

        # there a LIMIT clause attached
        if kwargs.has_key('limit'):
            sql_str += " LIMIT %s" % kwargs.get('limit')

        sql_str += ";"  # finalise our sql string
        print sql_str
        cursor = self.db.cursor()

        cursor.execute(sql_str)

        if named_tuples:
            results = self.convert_to_named_tuples(cursor)
        else:
            results = cursor.fetchall()

        cursor.close()

        return results

    def delete(self, table, **wheres):
        sql_str = "DELETE FROM `%s`.`%s`" % (self.database_name, table)

        if wheres is not None:
            first_where_clause = True
            for where, term in wheres.iteritems():
                if first_where_clause:
                    # this is the first WHERE clause
                    sql_str += " WHERE `%s`.`%s`%s" % (table, where, term)
                    first_where_clause = False
                else:
                    # this is an additional clause so use AND
                    sql_str += " AND `%s`.`%s`%s" % (table, where, term)

        sql_str += ";"
        print sql_str
        cursor = self.db.cursor()
        cursor.execute(sql_str)
        self.db.commit()
        cursor.close()

    def insert(self, table, **column_values):
        """
        insert(table_name, **keyword values)
        :param table: table_name
        """
        sql_str = "INSERT INTO `%s`.`%s` " % (self.database_name, table)

        if column_values is not None:
            columns = "("
            values = "("
            for column_name, value in column_values.iteritems():
                columns += "`%s`, " % column_name

                # # CHECK how we should ADD this TO the columns string
                # if is_number(value):
                #     # its a NUMBER so we dont ADD ''
                #     values += "%s, " % value
                # else:
                #     # its a DATE OR a string so ADD the ''
                #     values += "'%s', " % value

                values += "'%s', " % value

            columns = columns[:-2]  # strip off the spare ', from the end
            values = values[:-2]  # same here too

            columns += ") VALUES"  # add the connecting key word and brace
            values += ");"  # add the brace and like terminator

            sql_str += "%s %s" % (columns, values)
            print sql_str
        cursor = self.db.cursor()
        cursor.execute(sql_str)
        self.db.commit()
        cursor.close()

    def update(self, table, where=None, **column_values):
        sql_str = "UPDATE `%s`.`%s` SET " % (self.database_name, table)
        print sql_str
        if column_values is not None:
            for column_name, value in column_values.iteritems():
                sql_str += "`%s`=" % column_name

                # check how we should add this to the columns string
                if is_number(value):
                    # its a number so we don't add ''
                    sql_str += "%s, " % value
                else:
                    # its a date or a string so add the ''
                    sql_str += "'%s', " % value

        sql_str = sql_str[:-2]  # strip off the last , and space character

        if where:
            sql_str += " WHERE %s" % where

        cursor = self.db.cursor()
        cursor.execute(sql_str)
        self.db.commit()
        cursor.close()
