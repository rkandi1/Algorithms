package client;

import api.graph.Graph_API;
import api.graph.Pair;
import java.util.ArrayList;


public class GraphSearch {
	public int[] edgeTo;
	private boolean[] marked;
	
	public GraphSearch(Graph_API G) {
		this.edgeTo = new int[G.getSize()];
		this.marked = new boolean[G.getSize()];
	}
	
	public void dFS(Graph_API G, int source) {
		int prev = -1;
		int curr = source;
		this.edgeTo[source-1] = prev;
		this.marked[source-1] = true;
		while(true) {
			Iterable<Integer> adj_list = G.adjacent(curr);
			boolean broke = false;
			for(int w: adj_list) {
				if(!marked[w-1]) {
					this.edgeTo[w-1] = curr;
					this.marked[w-1] = true;
					System.out.println(curr);
					System.out.println("Created path between " + w + " and " + curr);
					prev = curr;
					curr = w;
					broke = true;
					break;
				}
			}
			if(broke) {
				continue;
			}
			System.out.println("=========================================");
			System.out.print("Falling back to ");
			curr = prev;
			System.out.print("curr = " + curr);
			if(curr!=-1)
			{
				prev = edgeTo[curr-1];
			} else {
				prev = -2;
			}
			System.out.println(" and prev = " + prev);
			System.out.println("=========================================");
			if(curr == -1) {
				return;
			}
		}
	}
	
	public int treeDiameter(Graph_API G, int root) {
		int[] adjTreeLen = new int[G.adjSize(root)];
		int index = 0;
		for(int w: G.adjacent(root)) {
			adjTreeLen[index] = 1 + this.treeDiameterHelper(G, w, root);
			index++;
		}
		
		int max1 = 0;
		int max2 = 0;
		for(int len: adjTreeLen) {
			if(len >= max1) {
				max2 = max1;
				max1 = len;
			}
		}
		
		return max1 + max2;
	}
	
	private Pair<String, Integer> treeDiameterHelper(Graph_API G, int curr, int parent) {
		int maxDepth = 0;
		String diameterValues = Integer.toString(curr);
		for(int w: G.adjacent(curr)) {
			if(w!=parent) {
				int subHeight = 1 + treeDiameterHelper(G, w, curr).getSecond();
				if(subHeight > maxDepth) {
					maxDepth = subHeight;
					
				}
			}
		}
		return new Pair<>(diameterValues, maxDepth);
	}
	
//	public int centerOfTree(Graph_API G, int v) {
//		
//	}
	
	public ArrayList<Integer> eulerCycle(Graph_API G, int v) {
		ArrayList<Integer> path = new ArrayList<>(G.getSize());
	}
	
	public static void main(String[] args) {
		Graph_API newGraph = new Graph_API(13);
//		newGraph.addEdge(1, 6);
//		newGraph.addEdge(1, 2);
//		newGraph.addEdge(1, 3);
//		newGraph.addEdge(1, 7);
//		newGraph.addEdge(4, 5);
//		newGraph.addEdge(4, 6);
//		newGraph.addEdge(5, 7);
//		newGraph.addEdge(5, 6);
//		newGraph.addEdge(8, 9);
//		newGraph.addEdge(10, 11);
//		newGraph.addEdge(10, 13);
//		newGraph.addEdge(10, 12);
//		newGraph.addEdge(12, 13);
		
		GraphSearch dfs = new GraphSearch(newGraph);
//		dfs.dFS(newGraph, 1);
//		System.out.println("\n\n\n============================");
//		for(int i=0; i<dfs.edgeTo.length; i++) {
//			System.out.println(i+1 +": " + dfs.edgeTo[i]);
//		}
		
		newGraph.addEdge(1, 2);
		newGraph.addEdge(1, 3);
		newGraph.addEdge(1, 4);
		newGraph.addEdge(2, 5);
		newGraph.addEdge(2, 6);
		newGraph.addEdge(3, 7);
		newGraph.addEdge(4, 8);
		newGraph.addEdge(7, 9);
		newGraph.addEdge(9, 12);
		newGraph.addEdge(3, 10);
		newGraph.addEdge(3, 11);
		
		System.out.println("Longest path of graph: " + dfs.treeDiameter(newGraph, 3));
	}
}
