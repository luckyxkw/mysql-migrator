#!/usr/bin/python
import mysql.connector
import config

def genMigrateColumns(cursor, sourceTable, targetTable):
    sourceColumns = set()
    targetColumns = set()
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s';" % sourceTable)
    for x in cursor:
	    sourceColumns.add(x[0])
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s';" % targetTable)
    for x in cursor:
	    targetColumns.add(x[0])
    for x in sourceColumns.copy():
	    if x not in targetColumns:
		    sourceColumns.remove(x)
    return ','.join(sourceColumns)

def migrate(cursor, sourceTable, targetTable):
    migrateColumns = genMigrateColumns(cursor, sourceTable, targetTable)
    sql = "INSERT INTO %s(%s) SELECT %s from %s;" % (targetTable, migrateColumns, migrateColumns, sourceTable)
    print("Migration sql is: " + sql)
    cursor.execute(sql)

def main():
    dbHost = config.MysqlConfig["DB_HOST"]
    dbUser = config.MysqlConfig["DB_USER"]
    dbPassword = config.MysqlConfig["DB_PASSWORD"]
    dbSchema = config.MysqlConfig["DB_SCHEMA"]
    print("Migrating data for database at '%s', schema '%s'." % (dbHost, dbSchema))

    conn = mysql.connector.connect(
        host=dbHost,
        user=dbUser,
        passwd=dbPassword
    )
    cursor = conn.cursor()
    cursor.execute("USE %s;" % dbSchema)

    while True:
        sourceTable = raw_input("What is the source table for migration? ")
        targetTable = raw_input("What is the target table for migration? ")
        migrate(cursor, sourceTable, targetTable)
        isContinue = raw_input("Do you want to migrate one more table?[y/N] ")
        print(isContinue)
        if isContinue == "N" or isContinue == "n":
            break
    
    conn.commit()
    conn.close()
    print("Migration completes.")

if __name__ == "__main__":
    main()
