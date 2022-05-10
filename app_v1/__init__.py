'''
On the spot assignment

Description

The data is present in a JSON file which can be accessed by the frontend by making an API call.
Design the REST API using Python and Django.
The API needs to have pagination and sort params (based on rank) so that when called it can return data in whatever way frontend requires.
The data is present in a JSON file which can be accessed by the frontend by making an API call. => { "name": "John Doe", "score": 100 }
Please note that the rank needs to be generated dynamically. Logic for rank calculation with an example:

 If there are three users A, B and C with the score 10, 10, 20 respectively then the rank will be:

 C: 1, A: 2, B: 2


The maximum possible score is 100

Tech Stack:
Backend: Django
Database: Postgres
Resource File: testdata.json

'''