import java.util.ArrayList;
import java.util.NoSuchElementException;

public class PowerOfTwoMaxHeap {
    private final int childrenPerNode;
    private final ArrayList<Integer> heap;

    public PowerOfTwoMaxHeap(int powerExponent) {
        if (powerExponent < 0) {
            throw new IllegalArgumentException("Power exponent must be non-negative.");
        }
        this.childrenPerNode = 1 << powerExponent; // 2^powerExponent
        this.heap = new ArrayList<>();
    }

    public void insert(int value) {
        heap.add(value);
        siftUp(heap.size() - 1);
    }

    public int popMax() {
        if (heap.isEmpty()) {
            throw new NoSuchElementException("Heap is empty.");
        }

        int max = heap.get(0);
        int lastValue = heap.remove(heap.size() - 1);

        if (!heap.isEmpty()) {
            heap.set(0, lastValue);
            siftDown(0);
        }

        return max;
    }

    private void siftUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / childrenPerNode;
            if (heap.get(index) > heap.get(parentIndex)) {
                swap(index, parentIndex);
                index = parentIndex;
            } else {
                return;
            }
        }
    }

    private void siftDown(int index) {
        int size = heap.size();
        while (true) {
            int maxIndex = index;

            for (int i = 1; i <= childrenPerNode; i++) {
                int childIndex = childrenPerNode * index + i;
                if (childIndex < size && heap.get(childIndex) > heap.get(maxIndex)) {
                    maxIndex = childIndex;
                }
            }

            if (maxIndex == index) {
                break;
            }

            swap(index, maxIndex);
            index = maxIndex;
        }
    }

    private void swap(int i, int j) {
        int tmp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, tmp);
    }

    // Optional: for testing or debugging
    public ArrayList<Integer> toList() {
        return new ArrayList<>(heap);
    }
}
