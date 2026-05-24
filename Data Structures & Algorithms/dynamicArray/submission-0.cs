public class DynamicArray {
    
   private int capacity;
   private int[] arr;
   private int size;

    public DynamicArray(int capacity) {
         this.capacity = capacity;
         this.size=0;
         this.arr = new int[this.capacity];

    }

    public int Get(int i) {
       
       return arr[i];

    }

    public void Set(int i, int n) {

          arr[i]=n;


    }

    public void PushBack(int n) {

        if(size==capacity)
        {
           Resize();

        }
        arr[size]=n;
        size++;


    }

    public int PopBack() {

             if(size>0)
             {
                size--;
             } 
        return arr[size];

    }

    private void Resize() {
        capacity*=2;
        int[] temp = new int[capacity];

        for(int i=0;i<size;i++)
        {
            temp[i]=arr[i];
        }
        arr=temp;

    }

    public int GetSize() {

        return size;

    }

    public int GetCapacity() {

        return capacity;

    }
}
