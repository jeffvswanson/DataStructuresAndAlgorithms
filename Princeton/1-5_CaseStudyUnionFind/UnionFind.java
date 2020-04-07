/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class UnionFind {
    private int[] id;  // access to component id (site indexed)
    private int count; // number of components

    public UnionFind(int N) {
        // Initialize component id array.
        count = N;
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public int count() {
        return count;
    }

    public boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    public int find(int p) {
        // Component identifier for p (0 to N-1)
        return id[p];
    }

    public void union(int p, int q) {
        // add connection between p and q
        int pID = find(p);
        int qID = find(q);

        // Nothing to to if p and q are already in the rame component.
        if (pID == qID) return;

        // Change values from id[p] to id [q].
        for (int i = 0; i < id.length; i++) {
            if (id[i] == pID) {
                id[i] = qID;
            }
        }
        count--;
    }

    public static void main(String[] args) {
        // Solve dynamic connectivity problem on StdIn.
        int N = StdIn.readInt();  // Read number of sites.
        UnionFind uf = new UnionFind(N);  // Initialize N components.
        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt(); // Read pair to connect.
            if (uf.connected(p, q)) continue; // Ignore if connected.
            uf.union(p, q); // Combine components.
            StdOut.println(p + " " + q);
        }
        StdOut.println(uf.count() + " components");
    }
}
