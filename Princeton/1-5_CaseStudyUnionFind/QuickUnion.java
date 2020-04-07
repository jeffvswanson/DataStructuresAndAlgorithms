/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class QuickUnion {
    private int[] id;  // access to component id (site indexed)
    private int count; // number of components

    public QuickUnion(int N) {
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
        // Find component name.
        while (p != id[p]) p = id[p];
        return p;
    }

    public void union(int p, int q) {
        // Give p and q the ssame root.
        int i = find(p);
        int j = find(q);
        if (i == j) return;

        id[i] = j;
        count--;
    }

    public static void main(String[] args) {
        // Solve dynamic connectivity problem on StdIn.
        int N = StdIn.readInt();  // Read number of sites.
        QuickUnion qu = new QuickUnion(N);  // Initialize N components.
        while (!StdIn.isEmpty()) {
            int p = StdIn.readInt();
            int q = StdIn.readInt(); // Read pair to connect.
            if (qu.connected(p, q)) continue; // Ignore if connected.
            qu.union(p, q); // Combine components.
            StdOut.println(p + " " + q);
        }
        StdOut.println(qu.count() + " components");
    }
}
