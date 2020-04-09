/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class WeightedQuickUnionFind {
    private int[] id;  // parent link (site indexed)
    private int[] sz;  // size of component for roots (site indexed)
    private int count;  // number of components

    public WeightedQuickUnionFind(int N) {
        count = N;
        id = new int[N];
        for (int i = 0; i < N; i++) {
            sz = new int[N];
        }
        for (int i = 0; i < N; i++) {
            sz[i] = 1;
        }
    }

    public int count() {
        return count;
    }

    public boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    public int find(int p) {
        // Follow links to find a root
        while (p != id[p]) {
            p = id[p];
        }
        return p;
    }

    public void union(int p, int q) {
        int i = find(p);
        int j = find(q);
        if (i == j) return;

        // Make smaller root point to larger one.
        if (sz[i] < sz[j]) {
            id[i] = j;
            sz[j] += sz[i];
        }
        else {
            id[j] = i;
            sz[i] += sz[j];
        }
        count--;
    }

    public static void main(String[] args) {
        // Solve dynamic connectivity problem on StdIn.
        int N = StdIn.readInt();  // Read number of sites.
        WeightedQuickUnionFind wf = new WeightedQuickUnionFind(N);  // Initialize N components.
        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt(); // Read pair to connect.
            if (wf.connected(p, q)) continue; // Ignore if connected.
            wf.union(p, q); // Combine components.
            StdOut.println(p + " " + q);
        }
        StdOut.println(wf.count() + " components");
    }
}
