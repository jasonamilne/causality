"""
A module for implementing various randomization techniques for Randomized Controlled Trials (RCTs).

This module provides functions for simple randomization, block randomization, stratified randomization,
covariate-adaptive randomization, permuted block randomization, cluster randomization, and minimization.
These methods ensure unbiased allocation of participants to different study groups.

Typical usage example:

  participants = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
  groups = ['Treatment', 'Control']
  randomizer = Randomizations(participants, groups, seed=42)

  simple_groups = randomizer.simple_randomization()
  block_groups = randomizer.block_randomization(block_size=4)
  stratified_groups = randomizer.stratified_randomization(strata)
  covariate_groups = randomizer.covariate_adaptive_randomization(covariates)
  permuted_block_groups = randomizer.permuted_block_randomization(block_sizes=[2, 4])
  cluster_groups = randomizer.cluster_randomization(clusters)
  minimized_groups = randomizer.minimization(covariates)
  randomizer.randomization_check(simple_groups)
"""

import random
import numpy as np
from collections import defaultdict

class Randomizations:
    def __init__(self, participants, groups, seed=None):
        """Initializes the Randomizations class with participants and groups.

        Args:
            participants (list): List of participant identifiers.
            groups (list): List of group names for randomization.
            seed (int, optional): Random seed for reproducibility. Defaults to None.
        """
        self.participants = participants
        self.groups = groups
        if seed is not None:
            self.set_random_seed(seed)

    def set_random_seed(self, seed):
        """Sets the random seed for reproducibility.

        Args:
            seed (int): The random seed value.
        """
        random.seed(seed)
        np.random.seed(seed)
    
    def simple_randomization(self):
        """Performs simple randomization of participants into groups.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned participants as values.
        """
        random.shuffle(self.participants)
        return {group: self.participants[i::len(self.groups)] for i, group in enumerate(self.groups)}
    
    def block_randomization(self, block_size):
        """Performs block randomization of participants into groups with a specified block size.

        Args:
            block_size (int): The size of each block.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned participants as values.
        """
        blocks = [self.participants[i:i + block_size] for i in range(0, len(self.participants), block_size)]
        randomized_blocks = []
        for block in blocks:
            random.shuffle(block)
            randomized_blocks.extend(block)
        return {group: randomized_blocks[i::len(self.groups)] for i, group in enumerate(self.groups)}

    def stratified_randomization(self, strata):
        """Performs stratified randomization based on predefined strata.

        Args:
            strata (dict): A dictionary with strata names as keys and lists of participants as values.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned participants as values.
        """
        stratified_groups = dict((group, []) for group in self.groups)
        for stratum, members in strata.items():
            random.shuffle(members)
            allocation = {group: members[i::len(self.groups)] for i, group in enumerate(self.groups)}
            for group, members in allocation.items():
                stratified_groups[group].extend(members)
        return stratified_groups

    def covariate_adaptive_randomization(self, covariates):
        """Performs covariate-adaptive randomization to balance covariates across groups.

        Args:
            covariates (dict): A dictionary with participant identifiers as keys and covariate values as values.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned participants as values.
        """
        group_allocations = dict({group: [] for group in self.groups})
        for participant in self.participants:
            covariate_values = covariates[participant]
            imbalance_scores = {group: np.sum([covariates[p] == covariate_values for p in group_allocations[group]]) for group in self.groups}
            min_imbalance_group = min(imbalance_scores, key=imbalance_scores.get)
            group_allocations[min_imbalance_group].append(participant)
        return group_allocations

    def permuted_block_randomization(self, block_sizes):
        """Performs permuted block randomization using varying block sizes.

        Args:
            block_sizes (list): A list of block sizes to use for permutation.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned participants as values.
        """
        blocks = []
        for block_size in block_sizes:
            blocks.extend([self.participants[i:i + block_size] for i in range(0, len(self.participants), block_size)])
        randomized_blocks = []
        for block in blocks:
            random.shuffle(block)
            randomized_blocks.extend(block)
        return {group: randomized_blocks[i::len(self.groups)] for i, group in enumerate(self.groups)}

    def cluster_randomization(self, clusters):
        """Performs cluster randomization where clusters of participants are randomized.

        Args:
            clusters (dict): A dictionary with cluster names as keys and lists of participant identifiers as values.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned clusters as values.
        """
        cluster_list = list(clusters.keys())
        random.shuffle(cluster_list)
        cluster_allocation = {group: cluster_list[i::len(self.groups)] for i, group in enumerate(self.groups)}
        participant_allocation = defaultdict(list)
        for group, cluster_keys in cluster_allocation.items():
            for cluster in cluster_keys:
                participant_allocation[group].extend(clusters[cluster])
        return dict(participant_allocation)

    def minimization(self, covariates):
        """Performs minimization to balance predefined covariates across groups.

        Args:
            covariates (dict): A dictionary with participant identifiers as keys and covariate values as values.

        Returns:
            dict: A dictionary with group names as keys and lists of assigned participants as values.
        """
        group_allocations = {group: [] for group in self.groups}
        for participant in self.participants:
            covariate_values = covariates[participant]
            imbalance_scores = {group: np.sum([covariates[p] == covariate_values for p in group_allocations[group]]) for group in self.groups}
            min_imbalance_group = min(imbalance_scores, key=imbalance_scores.get)
            group_allocations[min_imbalance_group].append(participant)
        return group_allocations

    def randomization_check(self, groups):
        """Checks and prints the sizes of the groups after randomization.

        Args:
            groups (dict): A dictionary with group names as keys and lists of assigned participants as values.

        Returns:
            dict: A dictionary with group names as keys and the count of participants in each group as values.
        """
        group_sizes = {group: len(members) for group, members in groups.items()}
        print(f"Group sizes: {group_sizes}")
        return group_sizes

# Example Usage
if __name__ == "__main__":
    participants = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
    groups = ['Treatment', 'Control']
    randomizer = Randomizations(participants, groups, seed=42)

    # Simple randomization
    simple_groups = randomizer.simple_randomization()
    print("Simple Randomization:", simple_groups)

    # Block randomization with block size 4
    block_groups = randomizer.block_randomization(block_size=4)
    print("Block Randomization:", block_groups)

    # Stratified randomization
    strata = {
        'young': ['P1', 'P2', 'P3', 'P4'],
        'old': ['P5', 'P6', 'P7', 'P8']
    }
    stratified_groups = randomizer.stratified_randomization(strata)
    print("Stratified Randomization:", stratified_groups)

    # Covariate-adaptive randomization
    covariates = {
        'P1': 'A', 'P2': 'B', 'P3': 'A', 'P4': 'B',
        'P5': 'A', 'P6': 'B', 'P7': 'A', 'P8': 'B'
    }
    covariate_groups = randomizer.covariate_adaptive_randomization(covariates)
    print("Covariate-Adaptive Randomization:", covariate_groups)

    # Permuted block randomization with varying block sizes
    permuted_block_groups = randomizer.permuted_block_randomization(block_sizes=[2, 4])
    print("Permuted Block Randomization:", permuted_block_groups)

    # Cluster randomization
    clusters = {
        'cluster1': ['P1', 'P2'],
        'cluster2': ['P3', 'P4'],
        'cluster3': ['P5', 'P6'],
        'cluster4': ['P7', 'P8']
    }
    cluster_groups = randomizer.cluster_randomization(clusters)
    print("Cluster Randomization:", cluster_groups)

    # Minimization
    covariates_minimization = {
        'P1': 'A', 'P2': 'B', 'P3': 'A', 'P4': 'B',
        'P5': 'A', 'P6': 'B', 'P7': 'A', 'P8': 'B'
    }
    minimized_groups = randomizer.minimization(covariates_minimization)
    print("Minimization:", minimized_groups)

    # Check randomization balance
    randomizer.randomization_check(simple_groups)
