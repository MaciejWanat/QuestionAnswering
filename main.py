#!/usr/bin/env python
# coding: utf-8

#Main script for DBpedia quepy.

import datetime

import quepy
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
dbpedia = quepy.install("dbpedia")


def print_define(results, target, metadata=None):
    for result in results["results"]["bindings"]:
        if result[target]["xml:lang"] == "en":
            print result[target]["value"]
            print


def print_enum(results, target, metadata=None):
    used_labels = []

    for result in results["results"]["bindings"]:
        if result[target]["type"] == u"literal":
            if result[target]["xml:lang"] == "en":
                label = result[target]["value"]
                if label not in used_labels:
                    used_labels.append(label)
                    print label


def print_age(results, target, metadata=None):
    assert len(results["results"]["bindings"]) == 1

    birth_date = results["results"]["bindings"][0][target]["value"]
    year, month, days = birth_date.split("-")

    birth_date = datetime.date(int(year), int(month), int(days))

    now = datetime.datetime.utcnow()
    now = now.date()

    age = now - birth_date
    print "{} years old".format(age.days / 365)


#handler print function
print_handlers = {
        "define": print_define,
        "enum": print_enum,
        "age": print_age,
    }

# first communicate
print('Hey! I can look for answer of any question you got in dbpedia.\n'
        'My regexes matches questions about people.\n')

# main loop
while 1:

        question = raw_input("Whats on your mind?\n")
        target, query, metadata = dbpedia.get_query(question)

        if isinstance(metadata, tuple):
            query_type = metadata[0]
            metadata = metadata[1]
        else:
            query_type = metadata
            metadata = None

        if query is None:
            print "Im afraid I coulnd't find any answer :(\n"
            continue

        #print query    #query attributes print

        if target.startswith("?"):
            target = target[1:]
        if query:
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            if not results["results"]["bindings"]:
                print "No answer found :("
                continue

        print
        print_handlers[query_type](results, target, metadata)