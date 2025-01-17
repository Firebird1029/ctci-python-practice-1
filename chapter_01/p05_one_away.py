# O(N)
import time
import unittest


def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)  # noqa
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def oneAwayBrandon(a: str, b: str) -> bool:
    n, m = len(a), len(b)
    if n <= 1 and m <= 1:
        return True
    if abs(n - m) > 1:
        return False
    if n > m:
        return oneAwayBrandon(b, a)
    edited = False
    i = j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            if edited:
                return False
            if i == n - 1 or j == m - 1:
                if n != m:
                    return False
            else:
                if a[i+1] == b[j+1]:
                    edited = True
                    i += 1
                    j += 1
                # unnecessary due to line 49
                # elif a[i+1] == b[j]:
                #     edited = True
                #     i += 1
                elif a[i] == b[j+1]:
                    edited = True
                    j += 1
                else:
                    return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [are_one_edit_different, oneAwayBrandon]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
