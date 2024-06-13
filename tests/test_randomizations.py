import src.randomizations as rdz
from collections import Counter
import pytest

@pytest.fixture
def randomizer():
    participants = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
    groups = ['Treatment', 'Control']
    return rdz.Randomizations(participants, groups, seed=42)

def test_correct_distribution(randomizer):
    """Test that participants are correctly distributed among groups."""
    randomized_groups = randomizer.simple_randomization()
    total_participants = sum(len(participants) for participants in randomized_groups.values())
    assert total_participants == len(randomizer.participants), "Not all participants are distributed among groups"

def test_no_duplicates(randomizer):
    """Test that no participants are duplicated across groups."""
    randomized_groups = randomizer.simple_randomization()
    all_assigned = [participant for group in randomized_groups.values() for participant in group]
    assert len(all_assigned) == len(set(all_assigned)), "There are duplicate participants across groups"

def test_no_missing_participants(randomizer):
    """Test that no participants are missing after randomization."""
    randomized_groups = randomizer.simple_randomization()
    all_assigned = [participant for group in randomized_groups.values() for participant in group]
    assert sorted(all_assigned) == sorted(randomizer.participants), "Some participants are missing after randomization"

def test_randomness():
    """Test the randomness of the allocation."""
    participants = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
    groups = ['Treatment', 'Control']
    allocations = []
    for _ in range(100):
        rand_instance = rdz.Randomizations(participants.copy(), groups, seed=None)
        randomized_groups = rand_instance.simple_randomization()
        allocations.append(tuple(randomized_groups['Treatment']))

    allocation_counter = Counter(allocations)
    assert len(allocation_counter) > 1, "Randomization does not appear random; all allocations are the same"

def test_repeatability_with_seed():
    """Test that the randomization is repeatable with the same seed."""
    participants = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
    groups = ['Treatment', 'Control']
    randomizer1 = rdz.Randomizations(participants.copy(), groups, seed=42)
    randomizer2 = rdz.Randomizations(participants.copy(), groups, seed=42)
    randomized_groups1 = randomizer1.simple_randomization()
    randomized_groups2 = randomizer2.simple_randomization()
    assert randomized_groups1 == randomized_groups2, "Randomization with the same seed does not produce the same result"

def test_uneven_distribution():
    """Test handling of uneven number of participants."""
    participants = ['P1', 'P2', 'P3', 'P4', 'P5']
    groups = ['Treatment', 'Control']
    rand_instance = rdz.Randomizations(participants, groups, seed=42)
    randomized_groups = rand_instance.simple_randomization()
    assert len(randomized_groups['Treatment']) + len(randomized_groups['Control']) == len(participants), "Not all participants are distributed among groups"
