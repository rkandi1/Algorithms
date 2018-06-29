package api.graph;

public class Pair<Item1, Item2>{
	private Item1 item1;
	private Item2 item2;
	
	public Pair(Item1 one, Item2 two) {
		item1 = one;
		item2  = two;
	}
	
	public Item1 getFirst() {
		return item1;
	}
	
	public Item2 getSecond() {
		return item2;
	}
	
	public String toString() {
		return "<" + this.item1 + ", " + this.item2 + ">";
	}
}
