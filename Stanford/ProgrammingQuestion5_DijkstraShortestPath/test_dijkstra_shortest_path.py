# test_dijkstra_shortest_path.py

import dijkstra_shortest_path as dsp
import unittest

from collections import defaultdict

class TestPQ5(unittest.TestCase):
    def test_setup(self):
        expected = defaultdict(list)
        expected[1] = [(80,982), (163,8164), (170,2620), (145,648), (200,8021), (173,2069), (92,647), (26,4122), (140,546), (11,1913), (160,6461), (27,7905), (40,9047), (150,2183), (61,9146), (159,7420), (198,1724), (114,508), (104,6647), (30,4612), (99,2367), (138,7896), (169,8700), (49,2437), (125,2909), (117,2597), (55,6399)]
        expected[100] = [(159,6567), (137,7178), (163,9709), (190,6674), (36,8612), (142,2994), (76,1793), (67,6216), (29,1642), (56,361), (144,6605), (128,2584), (153,9522), (145,5512), (15,809), (38,1369)]
        expected[200] = [(108,9976), (103,6851), (145,2753), (41,2622), (187,6767), (190,5999), (16,2848), (194,2915), (5,4009), (172,6888), (39,4319), (176,1709), (60,3269), (138,678), (43,8943), (98,2690), (1,8021), (104,7083), (154,229), (91,1988), (67,475), (76,4623), (195,8114), (37,7541), (54,4899)]

        got = dsp.setup()

        for key in expected.keys():
            self.assertEqual(expected[key], got[key])

        if 0 or 201 in got:
            self.assertEqual(0, 201, "Keys exist in dictionary which should not be there.")

    def test_breadth_first_search(self):

        expected = [1, 2]
        given = defaultdict(list)
        given[1] = [(2, 4)]
        given[3] = [(2, 4)]

        got = dsp.breadth_first_search(given, expected[0])

        self.assertEqual(expected, got)

    def test_find_shortest_path(self):

        graph = defaultdict(list)
        graph[1] = [(2,3), (3,4), (4,5), (5,6)]
        graph[2] = [(3,3), (4,1)]
        graph[3] = [(5,1)]
        graph[4] = [(5,3)]
        graph[5] = [(2,3)]
        source_node = 1

        expected = [0, 3, 4, 4, 5]

        got = dsp.find_shortest_path(graph, source_node)

        self.assertEqual(got, expected)

if __name__ == "__main__":
    unittest.main()