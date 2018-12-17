package net.lihulab;


import org.junit.Assert;
import org.junit.Test;

public class SingletonTest {

    @Test
    public void testsingle() {
        Assert.assertSame(Singleton.getInstance(), Singleton.getInstance());
    }

}
