PS C:\Users\ianma> ccloud quickstart
logged in to "Universitas Teknologi Digital Indonesia" (org-355j3) as Ian Madiana
? Create a new cluster? Yes
Press [Enter] to use default values.
Enter [Ctrl+C] at any step to exit the quickstart.

[Set up a free CockroachDB Serverless cluster]
? Cluster Name [? for help] (vivid-ape)

? Cluster Name vivid-ape
? Cloud Provider GCP
Retrieving available regions: succeeded
? Cloud Provider Region asia-southeast1
? Are you ready to create this cluster? Yes
Creating cluster: succeeded
? Connect to cluster? Yes
Press [Enter] to use default values.
Enter [Ctrl+C] at any step to exit the quickstart.

[Connect to free CockroachDB Serverless cluster]
Retrieving clusters: succeeded
Retrieving SQL users: succeeded
? Username Create New SQL User
? Username [? for help]

X Sorry, your reply was invalid: Username must start with a letter, number, or underscore; must contain only letters, numbers, dashes, periods, or underscores; and must be between 1 and 63 characters. Type in a new username and hit <Enter>.
? Username [? for help] dragon-maid

? Username dragon-maid
? Password [? for help] ************
? Database (defaultdb)

? Database defaultdb
? Cert Path [? for help] (~/.postgresql/root.crt)

? Cert Path ~/.postgresql/root.crt
? Would you like to connect to cluster? Yes
? How would you like to connect? General connection string
Looking up cluster ID: succeeded
Creating SQL user: succeeded
Success! Created SQL user
 name: dragon-maid
 cluster: 7f0bf067-b264-4e5a-8dff-bae0e68633d1
Retrieving cluster info: succeeded
postgresql://dragon-maid:n9%21Juw0Q9Skb@vivid-ape-5314.8nk.cockroachlabs.cloud:26257/defaultdb?application_name=ccloud&sslmode=verify-full
PS C:\Users\ianma> export DATABASE_URL="postgresql://dragon-maid:n9%21Juw0Q9Skb@vivid-ape-5314.8nk.cockroachlabs.cloud:26257/defaultdb?application_name=ccloud&sslmode=verify-full"
export: The term 'export' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
PS C:\Users\ianma> cd hello-world-python-psycopg2
PS C:\Users\ianma\hello-world-python-psycopg2> python example.py
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
PS C:\Users\ianma\hello-world-python-psycopg2> set DATABASE_URL="postgresql://dragon-maid:n9%21Juw0Q9Skb@vivid-ape-5314.8nk.cockroachlabs.cloud:26257/defaultdb?application_name=ccloud&sslmode=verify-full"