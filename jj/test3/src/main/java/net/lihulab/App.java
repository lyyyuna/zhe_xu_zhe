package net.lihulab;

/**
 * Hello world!
 *
 */
public class App<T>
{
    public static <T> App<T> getData() {
        return new App<T>();
    }
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
