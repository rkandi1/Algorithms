package api.graph;

public class DigraphAPI {
	private final int V; // Size of the graph
	private final Bag<Integer>[] adj; // Adjacency List
	
	public DigraphAPI(int V) {
		this.V = V;
		this.adj = new Bag[V];
		for(int i=0; i<V; i++) {
			adj[i] = new Bag<>();
		}
	}
	
	public boolean addEdge(int vout, int vin) {
		adj[vout-1].add(vin);
		return true;
	}
	
	public Iterable<Integer> adjacent(int v) {
		return adj[v];
	}
	
	public int getSize() {
		return this.V;
	}
}
