import unittest

import treelib

from mutwo import common_generators
from mutwo import zimmermann_generators


class PitchBasedContextFreeGrammarTests(unittest.TestCase):
    def setUp(cls):
        cls.pitch_based_context_free_grammar = (
            zimmermann_generators.PitchBasedContextFreeGrammar.from_constraints(
                prime_number_to_maximum_exponent_dict={
                    3: 1,
                    5: 1,
                },
                maximum_cent_deviation=550,
            )
        )

    def test_from_constraints(self):
        expected_rule_tuple = (
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("4/5"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("3/4"),
                    zimmermann_generators.JustIntonationPitchTerminal("16/15"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("4/5"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("16/15"),
                    zimmermann_generators.JustIntonationPitchTerminal("3/4"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("5/4"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("4/3"),
                    zimmermann_generators.JustIntonationPitchTerminal("15/16"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("5/4"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("15/16"),
                    zimmermann_generators.JustIntonationPitchTerminal("4/3"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("4/3"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("5/4"),
                    zimmermann_generators.JustIntonationPitchTerminal("16/15"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("4/3"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("16/15"),
                    zimmermann_generators.JustIntonationPitchTerminal("5/4"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("3/4"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("4/5"),
                    zimmermann_generators.JustIntonationPitchTerminal("15/16"),
                ),
            ),
            common_generators.ContextFreeGrammarRule(
                zimmermann_generators.JustIntonationPitchNonTerminal("3/4"),
                (
                    zimmermann_generators.JustIntonationPitchTerminal("15/16"),
                    zimmermann_generators.JustIntonationPitchTerminal("4/5"),
                ),
            ),
        )
        for expected_rule, real_rule in zip(
            expected_rule_tuple,
            self.pitch_based_context_free_grammar.context_free_grammar_rule_tuple,
        ):
            self.assertEqual(expected_rule.left_side, real_rule.left_side)
            self.assertEqual(expected_rule.right_side, real_rule.right_side)

    def test_resolve(self):
        start = zimmermann_generators.JustIntonationPitchNonTerminal("3/4")
        resolution = self.pitch_based_context_free_grammar.resolve(start, limit=1)

        expected_tree = treelib.Tree()
        start_data = (start,)
        root = expected_tree.create_node(
            tag=self.pitch_based_context_free_grammar._data_to_tag(start_data),
            data=start_data,
        )
        leaf0_data = (
            zimmermann_generators.JustIntonationPitchTerminal("4/5"),
            zimmermann_generators.JustIntonationPitchTerminal("15/16"),
        )
        leaf1_data = (
            zimmermann_generators.JustIntonationPitchTerminal("15/16"),
            zimmermann_generators.JustIntonationPitchTerminal("4/5"),
        )
        expected_tree.create_node(
            tag=self.pitch_based_context_free_grammar._data_to_tag(leaf0_data),
            data=leaf0_data,
            parent=root,
        )
        expected_tree.create_node(
            tag=self.pitch_based_context_free_grammar._data_to_tag(leaf1_data),
            data=leaf1_data,
            parent=root,
        )

        for expected_leaf, real_leaf in zip(
            expected_tree.leaves(), resolution.leaves()
        ):
            self.assertEqual(expected_leaf.data, real_leaf.data)
            self.assertEqual(expected_leaf.tag, real_leaf.tag)


if __name__ == "__main__":
    unittest.main()
