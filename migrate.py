
import mysql.connector
import config

def genSQL(cursor, sourceTable, targetTable):
    return ""

def migrate(cursor, sourceTable, targetTable):
    print("Migration completes.")

def main():
    dbHost = config.MysqlConfig["DB_HOST"]
    dbUser = config.MysqlConfig["DB_USER"]
    dbPassword = config.MysqlConfig["DB_PASSWORD"]
    dbSchema = config.MysqlConfig["DB_SCHEMA"]

    print("Migrating data for database at '%s', schema '%s'." % (dbHost, dbSchema))

    # mydb = mysql.connector.connect(
    #     host=dbHost,
    #     user=dbUser,
    #     passwd=dbPassword
    # )
    # cursor = mydb.cursor()

    cursor = None # Test Purpose

    while True:
        sourceTable = input("What is the source table for migration? ")
        targetTable = input("What is the target table for migration? ")
        migrate(cursor, sourceTable, targetTable)
        isContinue = input("Do you want to continue migration?[y/N] ")
        print(isContinue)
        if isContinue == "N" or isContinue == "n":
            break

if __name__ == "__main__":
    main()
