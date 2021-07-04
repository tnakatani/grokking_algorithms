"""Ch.8 Greedy algorithm
Given a list of radio stations, each with coverage over different states,
derive the least number of radio stations needed to cover all necessary states.
"""

import logging
from typing import Dict, Set

# Make a list of states you want to cover
states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# Make a hash table of radio stations and which states they cover
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"},
}


def greedy_algorithm(universe: Set[str], collections: Dict[str, Set[str]]) -> Set[str]:
    """Given a set of elements (universe) and a collection with each containing a set of elements,
    identifies the smallest sub-collection whose union equals the universe.
    """
    final_collection = set()
    total_elements_covered = set()
    while universe:
        optimal_collection = None
        elements_covered = set()
        for collection, elements_in_collection in collections.items():
            # get set of uncovered elements that this collection covers
            covered = universe & elements_in_collection
            # if collection covers more elements than current optimal_collection, replace it.
            if len(covered) > len(elements_covered):
                logging.info(
                    f"Collection {collection} has more elements ({covered}) than already covered. "
                    "Updating elements covered set."
                )
                optimal_collection = collection
                elements_covered = covered
                total_elements_covered.update(elements_in_collection)
                logging.info(f"Elements covered: {total_elements_covered}")
        # update elements that are still needed
        universe -= elements_covered
        # add optimal collection to final collection
        final_collection.add(optimal_collection)
    return final_collection


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    print(greedy_algorithm(states, stations))
