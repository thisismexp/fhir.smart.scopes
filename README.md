# fhir.smart.scopes
A simple python class allowing for [SMART on FHIR scopes](http://hl7.org/fhir/smart-app-launch/STU2.1/scopes-and-launch-context.html#scopes-for-requesting-fhir-resources)
to used as they were Python set objects. This implementation is based on
Smart App Launch Implementation Guide (v2.1.0: STU 2.1) which is based on 
FHIR R4. For example:
```python
>>> a = scopes('launch offline_access patient/Medication.rs')
>>> b = scopes('patient/Medication.cruds')
>>> a & b
patient/Medication.rs
>>> a | b
patient/Medication.cruds offline_access launch
```
Currently finer grained query parameters within scopes are not supported.
~~Support for finer grained constraints using search parameters is rather limited
since it is not trivial to e.g. combine different search parameters and 
preserve their overall intention (feel free to open a PR with ideas).~~


## Interface 
Create by using the type constructor with ether nothing, a space seperated string or an iterable.


## Constructors
see https://python-reference.readthedocs.io/en/latest/docs/sets/
-[x] set()
 Returns a set type initialized from iterable.

-[x] not supported ~~{} set comprehension Returns a set based on existing iterables.~~

-[x] not supported  ~~literal syntax
Initializes a new instance of the set type.~~

## Methods
### Adding Elements
-[x] add
Adds a specified element to the set.

-[x] update
Adds specified elements to the set.

### Deleting
-[x] discard
Removes an element from the set.

-[x] remove
Removes an element from the set (raises KeyError if not found).

-[x] pop
Removes and returns an arbitrary element from the set.

-[x] clear
Removes all elements from the set.

### Information
-[x] issuperset
Returns a Boolean stating whether the set contains the specified set or iterable.

-[x] issubset
Returns a Boolean stating whether the set is contained in the specified set or iterable.

-[x] isdisjoint
Returns a Boolean stating whether the set contents do not overlap with the specified set or iterable.
Set Operations

-[x] difference
Returns a new set with elements in the set that are not in the specified iterables.

-[x] intersection
Returns a new set with elements common to the set and the specified iterables.

-[x] symmetric_difference
Returns a new set with elements in either the set or the specified iterable but not both.

-[x] union
Returns a new set with elements from the set and the specified iterables.

### Set Operations Assignment
-[x] (implicit by set class) difference_update
Updates the set, removing elements found in the specified iterables.

-[x] (implicit by set class) intersection_update
Updates the set, keeping only elements found in it and the specified iterables.

-[x] (implicit by set class) symmetric_difference_update
Updates the set, keeping only elements found in either set or the specified iterable, but not in both.

### Copying
-[x] copy
Returns a copy of the set.

## Set Operators
### Adding Elements
-[x] |= (update)
Adds elements from another set.

### Relational Operators
-[x] (implicit by set class) == (is equal)
Returns a Boolean stating whether the set has the same elements as the other set.

-[x] (implicit by set class) != (is not equal)
Returns a Boolean stating whether the set has different elements as the other set.

-[x] (implicit by set class) <= (issubset)
Returns a Boolean stating whether the set is contained in the other set.

-[x] (implicit by set class) < (issubset proper)
Returns a Boolean stating whether the set is contained in the specified set and that the sets are not equal.

-[x] (implicit by set class) ' >= (issuperset)
Returns a Boolean stating whether the set contains the other set.

-[x] (implicit by set class) ' > (issuperset proper)
Returns a Boolean stating whether the set contains the other set and that the sets are not equal.
Set Operations

-[x] ' - (difference)
Returns a new set with elements in the set that are not in the other set.

-[x] & (intersection)
Returns a new set with elements common to the set and the other set.

-[x] ^ (symmetric_difference)
Returns a new set with elements in either the set or the other set but not both.

-[x] | (union)
Returns a new set with elements from the set and the other set.

### Set Operations Assignment
-[x] (implicit by set class) -= (difference_update)
Updates the set, removing elements found in the other set.

-[x] (implicit by set class) &= (intersection_update)
Updates the set, keeping only elements found in it and the other set.

-[x] (implicit by set class) ^= (symmetric_difference_update)
Updates the set, keeping only elements found in either set or the other set, but not in both.

## Functions
-[x] len
Returns an int type specifying number of elements in the collection.

-[ ] min
Returns the smallest item from a collection.

-[ ] max
Returns the largest item in an iterable or the largest of two or more arguments.

-[ ] sum
Returns a total of the items contained in the iterable object.

-[ ] sorted
Returns a sorted list from the iterable.

-[ ] reversed
Returns a reverse iterator over a sequence.

-[ ] all
Returns a Boolean value that indicates whether the collection contains only values that evaluate to True.

-[ ] any
Returns a Boolean value that indicates whether the collection contains any values that evaluate to True.

-[ ] enumerate
Returns an enumerate object.

-[ ] zip
Returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.