# coding: utf-8

from quepy.dsl import FixedType, HasKeyword, FixedRelation

# Setup the Keywords for this application
HasKeyword.relation = "rdfs:label"
HasKeyword.language = "en"

class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True

class DefinitionOf(FixedRelation):
    relation = "rdfs:comment"
    reverse = True

# ----- people.py ------

class IsPerson(FixedType):
    fixedtype = "foaf:Person"


class BirthDateOf(FixedRelation):
    relation = "dbpprop:birthDate"
    reverse = True


class BirthPlaceOf(FixedRelation):
    relation = "dbpedia-owl:birthPlace"
    reverse = True


class LocationOf(FixedRelation):
    relation = "dbpedia-owl:location"
    reverse = True
