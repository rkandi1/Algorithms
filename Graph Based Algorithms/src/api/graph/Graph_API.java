package api.graph;

import api.graph.Bag;
import java.util.ArrayList;
import java.lang.ArrayIndexOutOfBoundsException;

/**
 * This is an example Graph API that uses the Adjacency Matrix
 * @author RohanKandi1
 *
 * Necessary Functions:
 * Adding an Edge.
 * Iterating through the edges.
 */

public class Graph_API {
	private int V;
	private ArrayList<Bag<Integer>> adj;
	
	public Graph_API(int V) {
		this.V = V;
		adj = new ArrayList<>(5);
		for(int i=0; i<V; i++) {
			adj.add(new Bag<>());
		}
	}
	
	public boolean hasEdge(int v1, int v2) {
		for(int vertex: adj.get(v1-1)) {
			if(vertex == v2) {
				return true;
			}
		}
		return false;
	}
	
	public int getSize() {
		return this.V;
	}
	
	public int adjSize(int v) {
		return this.adj.get(v-1).size();
	}
	
	public boolean addEdge(int v1, int v2) {
		if(v1 > this.V || v2 > this.V) {
			System.out.println("The node doesn't exist.");
			return false;
		}
		else if(this.hasEdge(v1, v2)) {
			return false;
		}
		adj.get(v2-1).add(v1);
		adj.get(v1-1).add(v2);
		return true;
	}
	
	public Iterable<Integer> adjacent(int v){
		if(v > 0 && v <= this.V) {
			return adj.get(v-1);
		} else {
			throw new ArrayIndexOutOfBoundsException(
					"The number passed is greater than the number of vertices");
		}
	}
}

