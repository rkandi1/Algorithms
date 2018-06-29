package api.graph;

import java.util.Iterator;
/*
 * Necessary Functions:
 * A linked list implementation except no option to delete an element
 */
public class Bag<Item> implements Iterable<Item>{
	private Node<Item> first;
	private int number;
	
	static class Node<U>{
		Node(U item){
			this.item = item;
		}
		U item;
		Node<U> next;
	}
	
	public Bag() {
		first = null;
		number = 0;
	}
	
	public boolean isEmpty() {
		return first == null;
	}
	
	public int size() {
		return number;
	}
	
	public void add(Item item) {
		Node<Item> oldFirst = first;
		Node<Item> currNode = new Node<>(item);
		currNode.next = oldFirst;
		first = currNode;
		number++;
	}
	
	public Item getFirst() {
		return first.item;
	}
	
	@Override
	public Iterator<Item> iterator() {
		return new ListIterator<Item>(first);
	}
	
	class ListIterator<T extends Item> implements Iterator<T>{
		Node<T> current;
		
		ListIterator(Node<T> first){
			 current = first;
		}
		
		@Override
		public boolean hasNext() {
			return (current != null);
		}

		@Override
		public T next() {
			Node<T> oldCurrent = current;
			current = current.next;
			return oldCurrent.item;
		}
		
	}
	
	public String toString() {
		String result = "";
		Node<Item> curr = this.first;
		while(curr != null) {
			result += curr.item + ", ";
			curr = curr.next;
		}
		return result;
	}
}
