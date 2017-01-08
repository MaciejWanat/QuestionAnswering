# coding: utf-8

"""
Domain specific language for DBpedia quepyExample.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

# Setup the Keywords for this application
HasKeyword.relation = "rdfs:label"
HasKeyword.language = "en"

# ---- basic.py -----
class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True


class IsPerson(FixedType):
    fixedtype = "foaf:Person"


class IsPlace(FixedType):
    fixedtype = "dbpedia:Place"


class IsCountry(FixedType):
    fixedtype = "dbpedia-owl:Country"


class DefinitionOf(FixedRelation):
    relation = "rdfs:comment"
    reverse = True


class IsMemberOf(FixedRelation):
    relation = "dbpedia-owl:bandMember"
    reverse = True


class UTCof(FixedRelation):
    relation = "dbpprop:utcOffset"
    reverse = True

# ----- people.py ------

class BirthDateOf(FixedRelation):
    relation = "dbpprop:birthDate"
    reverse = True


class BirthPlaceOf(FixedRelation):
    relation = "dbpedia-owl:birthPlace"
    reverse = True


class LocationOf(FixedRelation):
    relation = "dbpedia-owl:location"
    reverse = True
