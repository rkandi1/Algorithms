package client;

import api.graph.Graph_API;

public class ConnectedComponents {
	private boolean[] marked;
	private int[] id;
	private int count;
	
	public ConnectedComponents(Graph_API G) {
		this.marked = new boolean[G.getSize()];
		this.id = new int[G.getSize()];
		
		for(int i=0; i<this.id.length; i++) {
			if(!this.marked[i]) {
				dFS(G, i);
				count++;
			}
		}
	}
	
	public int numberOfComponents() {
		return count;
	}
	
	public int vertexId(int v) {
		if(v > id.length) {
			return -1;
		} else {
			return id[v-1];
		}
	}
	
	private void dFS(Graph_API G, int v) {
		marked[v] = true;
		id[v] =count;
		for(int w: G.adjacent(v)) {
			if(!marked[w]) {
				dFS(G, w);
			}
		}
	}
}
