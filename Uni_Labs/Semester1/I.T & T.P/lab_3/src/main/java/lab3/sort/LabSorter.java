package lab3.sort;

public class LabSorter {

    /**
     * Метод для сортировки массива целых чисел.
     *
     * @param source исходный массив для сортировки.
     * @return отсортированный массив
     */
    public int[] sort(int[] source) 
    {
        int[] sortedArray = source.clone();


        for (int i = 0; i < sortedArray.length - 1; i++) 
        {
            for (int j = 0; j < sortedArray.length - i - 1; j++) 
            {
                if (sortedArray[j] > sortedArray[j + 1]) 
                {
                    int temp = sortedArray[j];
                    sortedArray[j] = sortedArray[j + 1];
                    sortedArray[j + 1] = temp;
                }
            }
        }

        return sortedArray;
    }
}

